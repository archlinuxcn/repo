pkgname=binfmt-wine
pkgver=1.2
pkgrel=1
pkgdesc="register wine interpreter"
arch=(any)
url="http://man7.org/linux/man-pages/man8/systemd-binfmt.8.html"
license=(GPL)
depends=('wine' 'systemd')
source=("wine.conf")
md5sums=('599bc907c9ae3fa371e8032b6db735dc')
install=$pkgname.install

package () {
  cd "$srcdir"
  install -Dm 644 wine.conf "$pkgdir/usr/lib/binfmt.d/wine.conf"
}
