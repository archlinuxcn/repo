# Maintainer: Xuanrui Qi <me@xuanruiqi.com>
# Contributor: Wayne Hartmann (DH4) <wayne@bitstorm.pw>

pkgname=ttf-wps-fonts
pkgver=1.0
pkgrel=4
pkgdesc="Symbol fonts required by wps-office."
arch=(any)
license=("custom")
depends=()
makedepends=()
source=("$pkgname.zip::https://github.com/IamDH4/$pkgname/archive/master.zip"
        "license.txt")
sha1sums=('cbc7d2c733b5d3461f3c2200756d4efce9e951d5'
          '6134a63d775540588ce48884e8cdc47d4a9a62f3')

package() {
  install -d "$pkgdir/usr/share/fonts/wps-fonts"
  install -m644 "$srcdir/$pkgname-master/"*.{ttf,TTF} "$pkgdir/usr/share/fonts/wps-fonts/"
  install -Dm644 "$srcdir/"license.txt "$pkgdir/usr/share/licenses/$pkgname/license.txt"
}
