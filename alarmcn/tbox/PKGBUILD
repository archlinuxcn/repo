# Maintainer: George Hu <integral@archlinux.org>

pkgname=tbox
pkgver=1.8.0
pkgrel=1
pkgdesc="A glib-like multi-platform C library"
arch=('x86_64' 'aarch64' 'riscv64')
url="https://github.com/tboox/${pkgname}"
license=('Apache-2.0')
depends=('glibc')
provides=('libtbox.so')
source=("${pkgname}-${pkgver}.tar.gz::${url}/archive/refs/tags/v${pkgver}.tar.gz")
sha256sums=('3b919f61055b75fe9cb3796477468f6fe7524801d429e6ac48933ddde9caafbd')

build() {
	cd "${pkgname}-${pkgver}/"
	./configure --prefix=/usr --kind=shared --demo=false
	make
}

package() {
	DESTDIR="${pkgdir}" make -C "${pkgname}-${pkgver}" install
}
