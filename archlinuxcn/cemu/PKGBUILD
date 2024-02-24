# Maintainer: Jeremy Kescher <jeremy@kescher.at>

pkgname=cemu
pkgver=2.0.487
pkgrel=2
pkgdesc='Software to emulate Wii U games and applications on PC'
arch=(x86_64)
url=https://cemu.info
license=(MPL2)
options+=(!strip)
depends=(
	# unbundled vcpkg
	'boost-libs>=1.79' 'fmt' 'libzip>=1.9.2' 'libpng>=1.6.37' 'pugixml>=1.12.1' 'sdl2>=2.0.22' 'wxwidgets-gtk3>=3.2' 'wayland' 'wayland-protocols'
	'llvm-libs>=12'
)
makedepends=(
	# build setup
	git 'cmake>=3.21.1' 'clang>=12' 'llvm>=12' ninja
	# unbundled vcpkg
	'boost>=1.79' 'glslang>=14' 'glm>=0.9.9.8' rapidjson
	# direct cemu dependencies
	nasm 'vulkan-headers>=1.3.240'
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
	git+https://github.com/cemu-project/Cemu#tag=v2.0-66
	# submodules
	git+https://github.com/mozilla/cubeb#commit=dc511c6b3597b6384d28949285b9289e009830ea
	git+https://github.com/ocornut/imgui#commit=8a44c31c95c8e0217f6e1fc814cbbbcca4981f14
	git+https://github.com/Exzap/ZArchive#commit=d2c717730092c7bf8cbb033b12fd4001b7c4d932
	# cubeb submodules
	git+https://github.com/arsenm/sanitizers-cmake#commit=aab6948fa863bc1cbe5d0850bc46b9ef02ed4c1a
	git+https://github.com/google/googletest#commit=800f5422ac9d9e0ad59cd860a2ef3a679588acb4
)
sha256sums=('SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP')

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
}

build() {
	# Upstream prefers a build with clang+llvm and Ninja.

	cd Cemu
	rm -f build/CMakeCache.txt
	local cmake_args=(
		-B build
		-G Ninja
		-Wno-dev
		-DCMAKE_BUILD_TYPE=Release
		-DCMAKE_C_COMPILER=clang
		-DCMAKE_CXX_COMPILER=clang++
		-DCMAKE_CXX_FLAGS="$CXXFLAGS -w"
		-DENABLE_VCPKG=OFF
		-DPORTABLE=OFF
	)
	cmake "${cmake_args[@]}"
	cmake --build build
}

package() {
	cd Cemu
	install -D bin/Cemu_release "$pkgdir/usr/bin/cemu"

	mkdir -p "$pkgdir/usr/share/cemu"

	GLOBIGNORE=bin/Cemu_release
	cp -r bin/* "$pkgdir/usr/share/cemu"
	unset GLOBIGNORE

	install -Dm644 src/resource/logo_icon.png -T "$pkgdir/usr/share/icons/hicolor/128x128/apps/cemu.png"
	sed -i -e '/^Icon=/cIcon=cemu' -e '/^Exec=Cemu/cExec=cemu' dist/linux/info.cemu.Cemu.desktop
	install -Dm644 dist/linux/info.cemu.Cemu.desktop -T "$pkgdir/usr/share/applications/cemu.desktop"
}
