# Maintainer: AaronP <aaronbpaden at that google place dot com>
pkgname=fex
pkgver=2.0.0
pkgrel=1
pkgdesc="Flexible field/token extraction"
url="https://github.com/jordansissel/fex"
arch=('x86_64' 'i686')
license=("Apache License 2.0")
source=("https://github.com/jordansissel/fex/archive/v2.0.0.tar.gz")
sha256sums=('b023711ddab9e656c077921c94d4346e21ab60d8c6d80b00191f3d581f4dfd7c')

build() {
  cd "${pkgname}-${pkgver}"
  make
}

package() {
  cd "${pkgname}-${pkgver}"
  pod2man -c "" -r "" fex.pod > fex.1
  make PREFIX=/usr DESTDIR="${pkgdir}" install
  install -Dm644 LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
# vim:set ts=2 sw=2 et:
