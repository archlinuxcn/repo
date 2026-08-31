# Maintainer: nlsdt <nlsdt@archlinuxcn.org>
# Contributor: George Hu <integral@archlinux.org>

pkgname=piliplus-git
_srcname=PiliPlus
_pkgname=piliplus
pkgver=2.1.2.3.r1.g828de30
pkgrel=1
pkgdesc="A third-party Bilibili client developed in Flutter"
url="https://github.com/bggRGjQaUbCoE/${_srcname}"
license=('GPL-3.0-or-later')
arch=('x86_64')
depends=('gtk3' 'mpv' 'libayatana-appindicator' 'webkit2gtk-4.1')
makedepends=('git' 'clang' 'cmake' 'ninja' 'fvm' 'patchelf')
provides=("${_pkgname}")
conflicts=("${_pkgname}")
options=('!debug')
source=("git+${url}.git")
sha256sums=('SKIP')

pkgver() {
	cd "${_srcname}/"
	git describe --long --tags --abbrev=7 | sed 's/\([^-]*-g\)/r\1/;s/-/./g'
}

prepare() {
	cd "${_srcname}/"
	fvm install
	fvm flutter --disable-analytics
	fvm flutter --no-version-check pub get
}

build() {
	cd "${_srcname}/"
	local _sdk _scripts
	_sdk="$(readlink -f .fvm/flutter_sdk)"
	_scripts="${PWD}/lib/scripts"

	# 修补 flutter SDK
	local _patches=(modal_barrier text_selection mouse_cursor image_anim
	                layout_builder navigation_drawer popup_menu fab
	                null_safety_for_selectable_region selectable_region
	                editable_text text_field scroll_position scrollable
	                scrollable_gesture draggable_scrollable_sheet scaffold
	                text text_painter sliver refresh_indicator)

	printf "正在应用 Flutter 引擎补丁...\n"
	git -C "${_sdk}" reset --hard HEAD
	for _patch in "${_patches[@]}"; do
		git -C "${_sdk}" apply "${_scripts}/${_patch}.patch"
	done

	printf "正在应用 material_ui 包补丁...\n"
	local _pubcache _material _mp
	_pubcache="${PUB_CACHE:-${HOME}/.pub-cache}/hosted/pub.dev"
	rm -rf "${_pubcache}"/material_ui-*
	fvm flutter pub get
	_material="$(ls -d "${_pubcache}"/material_ui-* 2>/dev/null | sort -V | tail -1)"
	if [[ -z "${_material}" ]]; then
		printf "警告: 未找到 material_ui, 跳过其补丁。\n"
	else
		for _mp in "${_scripts}"/material/*.patch; do
			case "$(basename "${_mp}")" in
				bottom_sheet_android.patch|bottom_sheet_ios_flutter_material.patch) continue ;;
			esac
			sed -i 's/\r$//' "${_mp}"
			git -C "${_material}" apply "${_mp}"
		done
	fi

	printf "补丁应用完成, 开始构建...\n"
	if fvm flutter build linux --no-pub --release \
		--dart-define pili.name="$(grep -m1 '^version:' pubspec.yaml | sed -E 's/^version:[[:space:]]*([0-9.]+).*/\1/')" \
		--dart-define pili.code="$(git rev-list --count HEAD)" \
		--dart-define pili.hash="$(git rev-parse HEAD)" \
		--dart-define pili.time="$(date +%s)"; then
		git -C "${_sdk}" reset --hard HEAD
	else
		_rc=$?
		printf "构建失败, 正在恢复 Flutter SDK...\n"
		git -C "${_sdk}" reset --hard HEAD
		return ${_rc}
	fi
	printf "构建完成, Flutter SDK 已恢复.\n"
}

package() {
	cd "${_srcname}/"

	# 建立目录
	install -d "${pkgdir}/opt/${_pkgname}"
	install -d "${pkgdir}/usr/bin"
	# 安装文件
	install -Dm755 "build/linux/x64/release/bundle/${_pkgname}" "${pkgdir}/opt/${_pkgname}/${_pkgname}"
	cp -a "build/linux/x64/release/bundle/lib" "${pkgdir}/opt/${_pkgname}/"
	cp -a "build/linux/x64/release/bundle/data" "${pkgdir}/opt/${_pkgname}/"

	# 设置库文件的 RPATH 为 $ORIGIN
	find "${pkgdir}/opt/${_pkgname}/lib" -type f -name "*.so*" -exec \
	patchelf --set-rpath '$ORIGIN' {} \;

	# 安装图标
	cd assets
	install -Dm644 images/logo/logo.png "${pkgdir}/usr/share/icons/hicolor/512x512/apps/${_pkgname}.png"
	# 安装 .desktop
	install -Dm644 "linux/com.example.${_pkgname}.desktop" -t "${pkgdir}/usr/share/applications/"
	# 链接主程序
	ln -s "/opt/${_pkgname}/${_pkgname}" "${pkgdir}/usr/bin/${_pkgname}"
}
