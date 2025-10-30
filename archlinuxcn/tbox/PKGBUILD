# Maintainer: George Hu <integral@archlinux.org>

pkgname=tbox
pkgver=1.7.7
pkgrel=1
pkgdesc="A glib-like multi-platform C library"
arch=('x86_64' 'aarch64' 'riscv64')
url="https://github.com/tboox/${pkgname}"
license=('Apache-2.0')
depends=('glibc')
provides=('libtbox.so')
source=("${pkgname}-${pkgver}.tar.gz::${url}/archive/refs/tags/v${pkgver}.tar.gz")
sha256sums=('ae387dcf1952aca572516bdce4a47d04e9b411f5bf7add281247af7c874f3c3f')

build() {
	cd "${pkgname}-${pkgver}/"
	./configure --prefix=/usr --kind=shared --demo=false
	make
}

package() {
	cd "${pkgname}-${pkgver}/"
	DESTDIR="${pkgdir}" make install
}
