#!/hint/bash

source '/opt/flutter-engine/base.incl'

readonly _cache_home=${XDG_CACHE_HOME:-$HOME/.cache}
readonly _engine_path="${srcdir}/flutter-engine"
readonly _dart_sdk="$_engine_path/out/host_arch_release/dart-sdk"
FLUTTER_TARGET_CPU="${FLUTTER_TARGET_CPU:-x64}"

if [[ ! -v _engine_version ]]; then
	_engine_version="$(yq -er .environment.flutter 'pubspec.yaml')"

	if [[ -z "$_engine_version" ]]; then
		local _pubspec="$(find "${srcdir}" -path "${srcdir}/flutter" -prune -o -path "${srcdir}/flutter-engine" -prune -o -name 'pubspec.yaml' -print -quit)"
		if [[ -n "$_pubspec" ]]; then
			_engine_version="$(yq -er .environment.flutter "$_pubspec")"
		fi
	fi
fi

if [[ -n "$_engine_version" ]]; then
	git -C "${srcdir}/flutter-engine" checkout -f "$_engine_version"
	git -C "${srcdir}/flutter" checkout -f "$_engine_version"
fi

readonly _cached_flutter_dir="${_engine_version+"$_cache_home/flutter-engine/$FLUTTER_TARGET_CPU/$_engine_version"}"

pushd "${srcdir}"
	sed -i 's|"$FLUTTER_ROOT/bin/internal/update_dart_sdk.sh"|#|' "${srcdir}/flutter/bin/internal/shared.sh"
	sed -i -E 's|_wait_for_lock$|#_wait_for_lock|' "${srcdir}/flutter/bin/internal/shared.sh"
	sed -i 's|--no-enable-mirrors "$SCRIPT_PATH"|--no-enable-mirrors "$SCRIPT_PATH" $ARCH_FLUTTER_OPTS|' \
		"${srcdir}/flutter/bin/internal/shared.sh"
	sed -i 's|exec "$DART" --disable-dart-dev --packages="$FLUTTER_TOOLS_DIR/.dart_tool/package_config.json" $FLUTTER_TOOL_ARGS "$SNAPSHOT_PATH" "$@"|exec "$DART" --disable-dart-dev --packages="$FLUTTER_TOOLS_DIR/.dart_tool/package_config.json" $FLUTTER_TOOL_ARGS "$SNAPSHOT_PATH" $ARCH_FLUTTER_OPTS "$@"|' \
		"${srcdir}/flutter/bin/internal/shared.sh"
	rm -rf "${srcdir}/flutter/bin/cache/dart-sdk" || true
	mkdir -p "${srcdir}/flutter/bin/cache"
	_ln "$_dart_sdk" "${srcdir}/flutter/bin/cache/dart-sdk"

	install -Dm755 <(cat << EOF
#!/usr/bin/env sh

$_dart_sdk/bin/dart "\$@"
EOF
	) "${srcdir}/flutter/bin/dart"

	git clone --depth=1 --single-branch 'https://chromium.googlesource.com/chromium/tools/depot_tools.git' "${srcdir}/depot_tools"
popd

export \
	PATH+=":${srcdir}/depot_tools" \
	DEPOT_TOOLS_UPDATE=0 \
	VPYTHON_BYPASS='manually managed python not supported by chrome operations'

_prepare_flutter_engine() {
	pushd "${srcdir}"
	
	cat >.gclient <<EOF
solutions = [
	{
		"name": "src/flutter",
		"url": "file://${srcdir}/flutter-engine${_engine_version+"@$_engine_version"}",
		"managed": False,
		"custom_deps": {},
		"custom_vars": {}
	}
]
EOF
	
	#--nohooks \
	gclient.py sync -D -R \
		--with_branch_heads \
		--with_tags \
		--output-json='gclient-sync.json' \
		--shallow
	
	cd 'src'
	
	sed -i 's|prefix = rebased_clang_dir|prefix= ""|g' 'build/toolchain/linux/BUILD.gn' # use system clang
	sed -i 's|}/|}|g' 'build/toolchain/linux/BUILD.gn' # use system clang
	sed -i 's|rebase|#|g' 'build/toolchain/linux/BUILD.gn'
	
	sed -i 's|$wayland_dir|//third_party/angle/third_party/wayland|' \
		'third_party/angle/BUILD.gn' \
		'third_party/angle/src/common/vulkan/BUILD.gn' \
		'third_party/angle/src/third_party/volk/BUILD.gn'
	
	sed -i 's|import("//build/config/chromecast_build.gni")||' 'third_party/angle/src/tests/BUILD.gn'
	sed -i '/-Wno-deprecated-literal-operator/d' 'build/config/compiler/BUILD.gn'
	sed -i '/G_DEFINE_AUTOPTR_CLEANUP_FUNC(PangoLayout, g_object_unref)/d' 'flutter/shell/platform/linux/fl_accessible_text_field.cc'
	
	cat > 'third_party/dart/build/dart/prebuilt_dart_sdk.gni' <<-EOF
		import("../executable_suffix.gni")
		_dart_root = rebase_path("../..")
		#_prebuilt_dart_exe = ""
		#_prebuilt_dart_exe_trial = ""
		prebuilt_dart_exe_works = true
EOF
	
	#_ln "${srcdir}/emsdk" 'buildtools/emsdk'
	popd
}

_build_flutter_engine() {
	pushd "${srcdir}"
	
	gclient.py sync -D -R \
		--with_branch_heads \
		--with_tags \
		--output-json='gclient-sync.json' \
		--shallow
	
	cd 'src'
	
	local outdir
	if [[ -z "$_cached_flutter_dir" ]]; then
		outdir="${srcdir}/flutter-out/host_arch_release"
	else
		outdir="${_cached_flutter_dir}/out/host_arch_release"
		_ln "${_cached_flutter_dir}/out" "${srcdir}/flutter-out"
	fi
	
	gn gen --no-prebuilt-dart-sdk -qv "$outdir" --args="$(cat <<-EOF
		target_os = "linux"
		target_cpu = "$FLUTTER_TARGET_CPU"
		dart_use_crashpad = false
		dart_use_fallback_root_certificates = true
		dart_use_compressed_pointers = true
		dart_vm_code_coverage = false
		dart_debug = false
		dart_runtime_mode = "release"
		is_debug = false
		exclude_kernel_service = false
		is_clang = true
		skia_use_piex = false
		target_sysroot = "/"
		verify_sdk_hash = false
		enable_unittests = false
		flutter_runtime_mode = "release"
	EOF
	)" || { >&2 echo '`gn gen` command failed.'; return 1; }
	
	sed -i 's|ldflags}|ldflags} -fuse-ld=lld|g' "$outdir/toolchain.ninja" # use system linker
	ninja -v -C "$outdir" || { >&2 echo 'Flutter engine build failed.'; return 1; }
	
	#export PATH+=":${srcdir}/src/flutter/lib/web_ui/dev"
	#felt build
	
	popd
}

_install_flutter_engine() {
	pushd "${srcdir}"
	
	rm -rf 'flutter-out/host_arch_release/'{gen,obj,lib.unstripped,exe.unstripped}
	ln -s 'host_arch_release' "flutter-out/arch_release"
	ln -s 'host_arch_release' "flutter-out/host_release"
	
	popd
}

if [[ -n "$_cached_flutter_dir" ]]; then
	if [[ ! -L "$_cached_flutter_dir/out/arch_release" ]]; then
		_prepare_flutter_engine && \
		_build_flutter_engine && \
		_install_flutter_engine || \
			{ return 1; }
	fi
	
	_ln "$_cached_flutter_dir/out" "${srcdir}/flutter-engine/out"
else
	_prepare_flutter_engine && \
	_build_flutter_engine && \
	_install_flutter_engine || \
		{ return 1; }
	_ln "${srcdir}/flutter-out" "${srcdir}/flutter-engine/out"
fi

_setup_env
