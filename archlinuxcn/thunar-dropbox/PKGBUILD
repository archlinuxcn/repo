# Maintainer: Jeinzi <jeinzi at gmx dot de>
# Contributer: Maato <maato at softwarebakery dot com>

pkgname='thunar-dropbox'
pkgver=0.3.0
pkgrel=1
pkgdesc="Plugin for thunar that adds context-menu items for dropbox."
arch=('i686' 'x86_64')
url="https://github.com/Jeinzi/thunar-dropbox"
license=('GPL3')
depends=('thunar')
makedepends=('python2')
source=("$pkgname-$pkgver.zip::https://github.com/Jeinzi/thunar-dropbox/archive/$pkgver.zip")
sha256sums=('776e563aac7b3a5f136e82fee13eb083d6446a44ddcea0c228017133c2180a81')

build() {
  cd "$srcdir/$pkgname-$pkgver"

  python2 waf configure --prefix=/usr || return 1
  python2 waf build || return 1
}

package() {
  cd "$srcdir/$pkgname-$pkgver"
  python2 waf install --destdir=$pkgdir || return 1
}
