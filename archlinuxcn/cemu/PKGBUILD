# Maintainer: Jeremy Kescher <jeremy@kescher.at>

pkgname=cemu
_major=2
_minor=4
_patch=0
pkgver=$_major.$_minor
cemu_tag="v$pkgver"
pkgrel=2
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
	git+https://github.com/mozilla/cubeb.git#commit=2071354a69aca7ed6df3b4222e305746c2113f60
	git+https://github.com/ocornut/imgui.git#commit=f65bcf481ab34cd07d3909aab1479f409fa79f2f
	git+https://github.com/Exzap/ZArchive.git#commit=d2c717730092c7bf8cbb033b12fd4001b7c4d932
	# cubeb submodules
	git+https://github.com/arsenm/sanitizers-cmake.git#commit=aab6948fa863bc1cbe5d0850bc46b9ef02ed4c1a
	git+https://github.com/google/googletest.git#commit=800f5422ac9d9e0ad59cd860a2ef3a679588acb4
	# Fix glslang 15 linking issue in Cafe
	fix-glslang-link.patch
)
sha512sums=('ecf9de9425c45b870273955dc311f30aab2eeb60a3e2c29a8f5f525fd3540f51eceb29bbe688726082d02d83eb6340b97356301a987f6f198aa97bcd0133dba4'
            '01a7e5c89668300beb9c6a75b955b01696a2ad3e3e9137333610743000f202bd7dc2a017aeace8f44936a517041f1652e0fa8fc2ac7a5f138585fb3575570d7a'
            'c7afdacbbb714e2e770955d5b7f9306a1b952a278c9e48f13d2bd1fb21d45e0c7d08a7e6af66a562bd585b21c10c7f486cbf8d302aaa32c91722b50246c2e125'
            '6ac14841ef983fe5202b23ea5c647959a04b9815bb187c0a0141fb14fb3e2edf8ce14b0c43474774d5ff779284f365981e6d45cc011612e5cd8fb429b3accf5e'
            '587d4d3dea948ce2aac33d3250cab0fe322ae892dc4f7261a56ad467c42a3d782d67113dc09ca7e5aff6d92dc9f0879c16dacb6531a4f3c5e5c62a3d6bfe6ab6'
            '8b65394aaf76a693a95cc493c57df3db61a7ac3474ec36596de5c36dd15b11a051ea46e74058bad184e521712dac570aa3b623c1028305f89ebbdde45457ded8'
            '4b03379373bc0394e3bdae23a69588774295c620547a03c47f55cb0b9e63aa4cad200f0add7d907273e944d467fcc685bd75d673c077afab7e9f1a9bfc98b235')

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

	git apply "${srcdir}/fix-glslang-link.patch"
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
