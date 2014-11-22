# Maintainer: masutu <masutu dot arch at gmail dot com>
# Contributor: Igor Hlina <srigi (at) srigi (dot) sk>
pkgname=cdu
pkgver=0.37
pkgrel=1
pkgdesc="du like command but display a pretty histogram with optional colors"
arch=('any')
url="http://arsunik.free.fr/prog/cdu.html"
license=('GPL')
depends=('perl')
source=(http://arsunik.free.fr/pkg/$pkgname-$pkgver.tar.gz)
md5sums=('625e8e62c00552e3fe054ac0af8392c0')
install=${pkgname}.install

build() {
  cd "$srcdir/$pkgname-$pkgver"
  make
}

package() {
  cd "$srcdir/$pkgname-$pkgver"
  install -D -m755 cdu $pkgdir/usr/bin/cdu
  install -D -m644 cdu.1 $pkgdir/usr/share/man/man1/cdu.1
}

# vim:set ts=2 sw=2 et:
