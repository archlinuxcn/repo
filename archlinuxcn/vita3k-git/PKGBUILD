# Maintainer: Severin Kaderli <severin@kaderli.dev>
# Contributor: aimileus < $(echo YWltaWxpdXNAcHJvdG9ubWFpbC5jb20K | base64 -d)
_pkgname=vita3k
pkgname="${_pkgname}-git"
pkgver=r1388.0dea8bf9
pkgrel=1
pkgdesc="Experimental PlayStation Vita emulator"
arch=('x86_64')
url="https://vita3k.org/"
license=('GPL2')
makedepends=(
	'boost'
	'cmake'
	'gcc8'
	'git'
	'python2'
	'vulkan-headers'
)
depends=(
	'boost-libs'
	'gtk3'
	'sdl2'
	'vulkan-icd-loader'
)
provides=('vita3k')
conflicts=('vita3k')
source=(
	"git+https://github.com/vita3k/vita3k.git"
)
md5sums=(
	'SKIP'
)

pkgver() {
	cd "${_pkgname}"
	printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
}

prepare() {
	cd "${_pkgname}"
	git submodule update --recursive --init
}

build() {
	cd "${_pkgname}"

	export CC="/usr/bin/gcc-8"
	export CXX="/usr/bin/g++-8"

	mkdir -p build
	cd build/
	cmake -DCMAKE_BUILD_TYPE=Release -DUSE_VULKAN=ON ..
	make UNICORN_QEMU_FLAGS="--python=/usr/bin/python2"
}

package() {
	cd "${_pkgname}"

	install -d -m 755 "${pkgdir}/usr/bin/"
	install -d -m 755 "${pkgdir}/opt/vita3k/"

	cp -r "build/bin/"* "${pkgdir}/opt/vita3k/"
	ln -s "/opt/vita3k/Vita3K" "${pkgdir}/usr/bin/vita3k"

	# These folders needs 777 permissions because vita3k creates files in them
	chmod 777 "${pkgdir}/opt/vita3k/"
	chmod 777 "${pkgdir}/opt/vita3k/data"

	install -Dm644 "README.md" "${pkgdir}/usr/share/doc/${pkgname}/README.md"
}
