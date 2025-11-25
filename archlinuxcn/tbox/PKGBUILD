# Maintainer: George Hu <integral@archlinux.org>

pkgname=tbox
pkgver=1.7.9
pkgrel=1
pkgdesc="A glib-like multi-platform C library"
arch=('x86_64' 'aarch64' 'riscv64')
url="https://github.com/tboox/${pkgname}"
license=('Apache-2.0')
depends=('glibc')
provides=('libtbox.so')
source=("${pkgname}-${pkgver}.tar.gz::${url}/archive/refs/tags/v${pkgver}.tar.gz")
sha256sums=('8d4bba88bb279c4ff71677d15f8bfc20dfbdc3b4eee27b540fb979fe5af65e56')

build() {
	cd "${pkgname}-${pkgver}/"
	./configure --prefix=/usr --kind=shared --demo=false
	make
}

package() {
	cd "${pkgname}-${pkgver}/"
	DESTDIR="${pkgdir}" make install
}
