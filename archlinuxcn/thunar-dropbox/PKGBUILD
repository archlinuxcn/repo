# Contributor: Maato <maato softwarebakery com>
pkgname='thunar-dropbox'
pkgver=0.2.1
pkgrel=1
pkgdesc="Plugin for thunar that adds context-menu items for dropbox."
arch=('i686' 'x86_64')
url="http://www.softwarebakery.com/maato/thunar-dropbox.html"
license=('GPL3')
depends=('thunar')
makedepends=('pkg-config' 'python2')
install=thunar-dropbox.install
source=(http://www.softwarebakery.com/maato/files/thunar-dropbox/$pkgname-$pkgver.tar.bz2)
md5sums=('52bb2caa26afaf80835a56b9ad3d2155')

build() {
  cd "$srcdir/$pkgname-$pkgver"

  python2 waf configure --prefix=/usr || return 1
  python2 waf build || return 1
}

package() {
  cd "$srcdir/$pkgname-$pkgver"
  python2 waf install --destdir=$pkgdir || return 1
}
