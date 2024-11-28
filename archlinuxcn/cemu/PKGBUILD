# Maintainer: Jeremy Kescher <jeremy@kescher.at>

pkgname=cemu
_major=2
_minor=4
_patch=0
pkgver=$_major.$_minor
cemu_tag="v$pkgver"
pkgrel=1
pkgdesc='Software to emulate Wii U games and applications on PC'
arch=(x86_64)
url=https://cemu.info
license=(MPL2)
options+=(!strip)
depends=(
	# unbundled vcpkg
	'boost-libs>=1.79' 'fmt<12' 'libzip>=1.9.2' 'libpng>=1.6.37' 'pugixml>=1.12.1' 'sdl2>=2.0.22' 'wxwidgets-gtk3>=3.2' 'wayland' 'wayland-protocols'
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
	# Cemu submodules
	git+https://github.com/mozilla/cubeb.git#commit=dc511c6b3597b6384d28949285b9289e009830ea
	git+https://github.com/ocornut/imgui.git#commit=8a44c31c95c8e0217f6e1fc814cbbbcca4981f14
	git+https://github.com/Exzap/ZArchive.git#commit=d2c717730092c7bf8cbb033b12fd4001b7c4d932
	# cubeb submodules
	git+https://github.com/arsenm/sanitizers-cmake.git#commit=aab6948fa863bc1cbe5d0850bc46b9ef02ed4c1a
	git+https://github.com/google/googletest.git#commit=800f5422ac9d9e0ad59cd860a2ef3a679588acb4
)
sha512sums=('ecf9de9425c45b870273955dc311f30aab2eeb60a3e2c29a8f5f525fd3540f51eceb29bbe688726082d02d83eb6340b97356301a987f6f198aa97bcd0133dba4'
            '770a67624181e4c7f05c88c3f1a10dc14012d4967d5bf95f48af1a5bd7a90dd5d8242a868dbe74d8beb043365eababd0d62768b74ccc9867c0c4fd1883849828'
            '0c3d10999772aa92e97aa3082f10e6ebba93f2a738e402f9833f350eb525b71afca178bf834db3bbe965eb0073f249f68b5c8124176add0af997f1c897282803'
            '6ac14841ef983fe5202b23ea5c647959a04b9815bb187c0a0141fb14fb3e2edf8ce14b0c43474774d5ff779284f365981e6d45cc011612e5cd8fb429b3accf5e'
            '587d4d3dea948ce2aac33d3250cab0fe322ae892dc4f7261a56ad467c42a3d782d67113dc09ca7e5aff6d92dc9f0879c16dacb6531a4f3c5e5c62a3d6bfe6ab6'
            '8b65394aaf76a693a95cc493c57df3db61a7ac3474ec36596de5c36dd15b11a051ea46e74058bad184e521712dac570aa3b623c1028305f89ebbdde45457ded8')

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
		-DEMULATOR_VERSION_MAJOR="$_major"
		-DEMULATOR_VERSION_MINOR="$_minor"
		-DEMULATOR_VERSION_PATCH="$_patch"
	)
	cmake "${cmake_args[@]}"
	cmake --build build
}

package() {
	cd Cemu
	install -D bin/Cemu_release "$pkgdir/usr/bin/Cemu"
	ln -s 'Cemu' "$pkgdir/usr/bin/cemu"

	mkdir -p "$pkgdir/usr/share/Cemu"

	GLOBIGNORE=bin/Cemu_release
	cp -r bin/* "$pkgdir/usr/share/Cemu"
	unset GLOBIGNORE

	install -Dm644 src/resource/logo_icon.png -T "$pkgdir/usr/share/icons/hicolor/128x128/apps/info.cemu.Cemu.png"
	install -Dm644 dist/linux/info.cemu.Cemu.desktop -T "$pkgdir/usr/share/applications/Cemu.desktop"
}
