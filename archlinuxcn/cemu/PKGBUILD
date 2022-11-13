# Maintainer: Jeremy Kescher <jeremy@kescher.at>

pkgname=cemu
pkgver=2.0.223
pkgrel=1
pkgdesc='Software to emulate Wii U games and applications on PC (with cutting edge Linux patches)'
arch=(x86_64)
url=https://cemu.info
license=(MPL2)
options+=(!strip)
depends=(
	# unbundled vcpkg
	'fmt>=9.1' 'sdl2>=2.0.22' 'pugixml>=1.12.1' 'libzip>=1.9.2' 'libpng>=1.6.37' 'wxwidgets-gtk3>=3.2'
)
makedepends=(
	git 'cmake>=3.21.1'
	# clang
	$([[ $CC+$CXX == *clang* ]] && echo 'clang>=12 llvm>=12')
	# unbundled vcpkg
	rapidjson 'boost>=1.79' 'glslang>=11.8' 'glm>=0.9.9.8'
	# cemu
	nasm 'vulkan-headers>=1.3.225'
	# wxwidgets
	glu
	# cubeb optional
	libpulse
)
optdepends=(
	'alsa-lib: Audio output'
	'vulkan-driver: Vulkan graphics'
)
install=cemu.install
source=(
	git+https://github.com/cemu-project/Cemu#commit=138510106c63ff697d31fe8e57391e245e477b5c # v2.0-14
	# submodules
	git+https://github.com/mozilla/cubeb#commit=dc511c6b3597b6384d28949285b9289e009830ea
	git+https://github.com/ocornut/imgui#commit=8a44c31c95c8e0217f6e1fc814cbbbcca4981f14
	git+https://github.com/Exzap/ZArchive#commit=d2c717730092c7bf8cbb033b12fd4001b7c4d932
	# cubeb submodules
	git+https://github.com/arsenm/sanitizers-cmake#commit=aab6948fa863bc1cbe5d0850bc46b9ef02ed4c1a
	git+https://github.com/google/googletest#commit=800f5422ac9d9e0ad59cd860a2ef3a679588acb4
	# upstream proposed patches
	overlay.diff # 6aa7a0c7b2003f625bfecd64f6143a10605234b2 (https://github.com/cemu-project/Cemu/pull/142)
	gui.diff # ffed93a69bb8f38a7c81624411bf8be0b45b8646 (https://github.com/cemu-project/Cemu/pull/439)
)
sha256sums=('SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'f25d13fe76cc6a0b475f0131211a951288160ddae92cd7a815f5aea61d7cfc0f'
            'dcb405fd9b77d73eee4a9591c606a5b7d121999b936920520518e70dcb16ea0e')

pkgver() {
	cd Cemu
	MAJ=$(awk -F'\t' '/LEAD/ {print $NF; exit}' src/Common/version.h)
	MIN=$(awk -F'\t' '/MAJOR/ {print $NF; exit}' src/Common/version.h)
	PAT=$(git rev-list --count HEAD)
	sed -i "/#define EMULATOR_VERSION_MINOR/s/[0-9]\+/$PAT/;s/-/./" src/Common/version.h
	echo "$MAJ.$MIN.$PAT"
}

prepare() {
	cd Cemu

	# cemu submodules
	for submodule in dependencies/{cubeb,imgui,ZArchive}; do
		git config submodule.$submodule.url "file://$srcdir/${submodule##*/}"
		git submodule--helper update --init $submodule
	done
	pushd dependencies/cubeb > /dev/null
	for submodule in {cmake/sanitizers-cmake,googletest}; do
		git config submodule.$submodule.url "file://$srcdir/${submodule##*/}"
		git submodule--helper update --init $submodule
	done
	popd > /dev/null

	# unbundled fmt
	sed -i '/FMT_HEADER_ONLY/d' src/Common/precompiled.h

	# cubeb fix
	sed -i '/find_package(cubeb)/d' CMakeLists.txt

	# glm fix
	sed -i 's/glm::glm/glm/' src/Common/CMakeLists.txt src/input/CMakeLists.txt

	# Dir names will be changed to "Cemu" in this package with 2.1
	# Needs notice in post_install() then
	sed -i 's/GetAppName()/"cemu"/' src/gui/CemuApp.cpp

	# gamelist column width improvement
	sed -i '/InsertColumn/s/kListIconWidth/&+8/;/SetColumnWidth/s/last_col_width/&-1/' src/gui/components/wxGameList.cpp

	rm -rf src/util/SystemInfo
	git apply "$srcdir/overlay.diff"
	sed -i '/add_library/aSystemInfo/SystemInfo.cpp SystemInfo/SystemInfoLinux.cpp' src/util/CMakeLists.txt

	git apply "$srcdir/gui.diff"
}

build() {
	# prefer clang (faster)
	if [[ $(clang --version 2> /dev/null | sed -E '1!d;s/^clang version ([0-9]+)\.[0-9]+\.[0-9]+$/\1/') -ge 12 ]] &&
	   [[ $(llvm-config --version 2> /dev/null | sed -E 's/^([0-9]+)\.[0-9]+\.[0-9]+$/\1/') -ge 12 ]]; then
		[[ -z $CC  ]] && export CC=$(which clang)
		[[ -z $CXX ]] && export CXX=$(which clang++)
	fi

	cd Cemu
	rm -f build/CMakeCache.txt
	cmake -B build \
	      $(which ninja &> /dev/null && echo '-G Ninja') \
	      -DCMAKE_CXX_FLAGS="$CXXFLAGS -w" -Wno-dev \
	      -DENABLE_VCPKG=OFF \
	      -DPORTABLE=OFF \
	      -DCMAKE_BUILD_TYPE=Release
	$(which ninja 2> /dev/null || which make) -C build $([[ "$MAKEFLAGS" == *-j* ]] && echo "$MAKEFLAGS" || echo -j $(nproc))
}

package() {
	cd Cemu
	install -D bin/Cemu_release "$pkgdir/usr/bin/cemu"

	mkdir -p "$pkgdir/usr/share/cemu"

	GLOBIGNORE=bin/Cemu_release
	cp -r bin/* "$pkgdir/usr/share/cemu"
	unset GLOBIGNORE

	install -Dm644 src/resource/logo_icon.png -T "$pkgdir/usr/share/icons/hicolor/128x128/apps/cemu.png"
	# https://github.com/cemu-project/Cemu/issues/92
	sed -i -e '/^Icon=/cIcon=cemu' -e '/^Exec=/cExec=env GDK_BACKEND=x11 cemu' dist/linux/info.cemu.Cemu.desktop
	install -Dm644 dist/linux/info.cemu.Cemu.desktop -T "$pkgdir/usr/share/applications/cemu.desktop"
}
