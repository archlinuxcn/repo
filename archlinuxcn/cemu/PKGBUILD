# Maintainer: Jeremy Kescher <jeremy@kescher.at>

pkgname=cemu
pkgver=2.0.639+really+2.0.94
cemu_experimental_version=94
cemu_tag=v2.0-$cemu_experimental_version
pkgrel=1
pkgdesc='Software to emulate Wii U games and applications on PC'
arch=(x86_64)
url=https://cemu.info
license=(MPL2)
options+=(!strip)
depends=(
	# unbundled vcpkg
	'boost-libs>=1.79' 'fmt' 'libzip>=1.9.2' 'libpng>=1.6.37' 'pugixml>=1.12.1' 'sdl2>=2.0.22' 'wxwidgets-gtk3>=3.2' 'wayland' 'wayland-protocols'
	'llvm-libs>=17'
)
makedepends=(
	# build setup
	git 'cmake>=3.21.1' 'clang>=17' 'llvm>=17' ninja
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
	"git+https://github.com/cemu-project/Cemu#tag=${cemu_tag}"
	# submodules
	git+https://github.com/mozilla/cubeb.git#commit=dc511c6b3597b6384d28949285b9289e009830ea
	git+https://github.com/ocornut/imgui.git#commit=8a44c31c95c8e0217f6e1fc814cbbbcca4981f14
	git+https://github.com/Exzap/ZArchive.git#commit=d2c717730092c7bf8cbb033b12fd4001b7c4d932
	# cubeb submodules
	git+https://github.com/arsenm/sanitizers-cmake.git#commit=aab6948fa863bc1cbe5d0850bc46b9ef02ed4c1a
	git+https://github.com/google/googletest.git#commit=800f5422ac9d9e0ad59cd860a2ef3a679588acb4
)
sha512sums=('4893bce18fa752ec795d4ed3b9306367c599ab201824a4f644cdd196763bc579deeecace7c4af95973077d939daa73ff6c58661210ab2083f37ac69c10465b14'
            '770a67624181e4c7f05c88c3f1a10dc14012d4967d5bf95f48af1a5bd7a90dd5d8242a868dbe74d8beb043365eababd0d62768b74ccc9867c0c4fd1883849828'
            '0c3d10999772aa92e97aa3082f10e6ebba93f2a738e402f9833f350eb525b71afca178bf834db3bbe965eb0073f249f68b5c8124176add0af997f1c897282803'
            '6ac14841ef983fe5202b23ea5c647959a04b9815bb187c0a0141fb14fb3e2edf8ce14b0c43474774d5ff779284f365981e6d45cc011612e5cd8fb429b3accf5e'
            '587d4d3dea948ce2aac33d3250cab0fe322ae892dc4f7261a56ad467c42a3d782d67113dc09ca7e5aff6d92dc9f0879c16dacb6531a4f3c5e5c62a3d6bfe6ab6'
            '8b65394aaf76a693a95cc493c57df3db61a7ac3474ec36596de5c36dd15b11a051ea46e74058bad184e521712dac570aa3b623c1028305f89ebbdde45457ded8')

pkgver() {
	cd Cemu
	MAJ=$(awk -F'\t' '/LEAD/ {print $NF; exit}' src/Common/version.h)
	MIN=$(awk -F'\t' '/MAJOR/ {print $NF; exit}' src/Common/version.h)
	# TODO: Apply this with the next Cemu release
	# PAT=$cemu_experimental_version
	PAT=$(git rev-list --count HEAD)
	# TODO: Apply this with the next Cemu release
	# sed -i "/#define EMULATOR_VERSION_MINOR/s/[0-9]\+/$PAT/" src/Common/version.h
	sed -i "/#define EMULATOR_VERSION_MINOR/s/[0-9]\+/$cemu_experimental_version/;s/-/./" src/Common/version.h
	# TODO: Apply this with the next Cemu release
	# echo "$MAJ.$MIN.$PAT"
	echo "$MAJ.$MIN.$PAT+really+$MAJ.$MIN.$cemu_experimental_version"
}

prepare() {
	cd Cemu

	# cemu submodules
	git rm --ignore-unmatch dependencies/{Vulkan-Headers,vcpkg}
	for submodule in {cubeb,imgui,ZArchive}; do
		git config --file=.gitmodules submodule.dependencies/"${submodule}".url "$srcdir/$submodule"
	done
	git -c protocol.file.allow=always submodule update --init
	pushd dependencies/cubeb > /dev/null
	git config --file=.gitmodules submodule.googletest.url "$srcdir/googletest"
	git config --file=.gitmodules submodule.cmake/sanitizers-cmake.url "$srcdir/sanitizers-cmake"
	git -c protocol.file.allow=always submodule update --init
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
