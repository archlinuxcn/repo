#Maintainer: Wayne Hartmann (DH4) <wayne@bitstorm.pw>

pkgname=ttf-wps-fonts
pkgver=1.0
pkgrel=2
pkgdesc="Symbol fonts required by wps-office."
arch=(any)
depends=(fontconfig xorg-font-utils)
source=($pkgname::git+https://github.com/wayne-hartmann/ttf-wps-fonts.git)
install=$pkgname.install
md5sums=('SKIP')

package() {
  install -d "$pkgdir/usr/share/fonts/wps-fonts"
  install -m644 "$srcdir/$pkgname/"*.{ttf,TTF} "$pkgdir/usr/share/fonts/wps-fonts/"
}
