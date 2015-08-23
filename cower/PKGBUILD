# Maintainer: Dave Reisner <d@falconindy.com>

pkgname=cower
pkgver=13
pkgrel=1
pkgdesc="A simple AUR agent with a pretentious name"
arch=('i686' 'x86_64')
url="http://github.com/falconindy/cower"
license=('MIT')
depends=('curl' 'openssl' 'pacman' 'yajl')
makedepends=('perl')
source=("http://code.falconindy.com/archive/$pkgname/$pkgname-$pkgver.tar.gz"{,.sig})
validpgpkeys=('487EACC08557AD082088DABA1EB2638FF56C0C53')  # Dave Reisner
md5sums=('741c05e6865dafc5fff72a186ee5daf9'
         'SKIP')

build() {
  cd "$pkgname-$pkgver"

  make
  sed '/^$/q' cower.c >LICENSE
}

package() {
  cd "$pkgname-$pkgver"

  make PREFIX=/usr DESTDIR="$pkgdir" install
  install -Dm644 LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}

# vim: ft=sh syn=sh
