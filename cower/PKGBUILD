# Maintainer: Dave Reisner <d@falconindy.com>

pkgname=cower
pkgver=18
pkgrel=1
pkgdesc="A simple AUR agent with a pretentious name"
arch=('i686' 'x86_64')
url="http://github.com/falconindy/cower"
license=('MIT')
depends=('curl' 'pacman' 'yajl')
makedepends=('perl')
source=("https://pkgbuild.com/~dreisner/sources/$pkgname/$pkgname-$pkgver.tar.gz"{,.sig})
validpgpkeys=('487EACC08557AD082088DABA1EB2638FF56C0C53')  # Dave Reisner
md5sums=('ce5993a79d7e1cc33016e06e32af03e7'
         'SKIP')

build() {
  cd "$pkgname-$pkgver"

  make
  sed '/^$/q' src/cower.c >LICENSE
}

package() {
  cd "$pkgname-$pkgver"

  make PREFIX=/usr DESTDIR="$pkgdir" install
  install -Dm644 LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}

# vim: ft=sh syn=sh
