# Maintainer: xiretza <xiretza+aur@xiretza.xyz>
# Contributor: Bruce Zhang

_pkgname=SPIRV-Headers
pkgname=spirv-headers-git
epoch=1
pkgver=1.3.236.0.r4.g34d0464
pkgrel=1
pkgdesc='SPIR-V header files Git version'
arch=('any')
url='https://www.khronos.org/registry/spir-v/'
license=('custom')
source=("git+https://github.com/KhronosGroup/$_pkgname.git")
sha1sums=('SKIP')
makedepends=('git' 'cmake')
conflicts=('spirv-headers')
provides=("spirv-headers=1:$pkgver")

pkgver() {
    cd "$_pkgname"
	git describe --long --tags | sed 's/^sdk-//; s/\([^-]*-g\)/r\1/; s/-/./g'
}

build() {
	cmake -B build -S "$_pkgname" \
		-DCMAKE_INSTALL_PREFIX=/usr
	make -C build
}

package() {
	make -C build DESTDIR="$pkgdir" install
	install -Dm644 "$_pkgname/LICENSE" -t "$pkgdir/usr/share/licenses/$pkgname"
}
