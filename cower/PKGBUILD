# Maintainer: Dave Reisner <d@falconindy.com>

pkgname=cower
pkgver=12
pkgrel=2
pkgdesc="A simple AUR agent with a pretentious name"
arch=('i686' 'x86_64')
url="http://github.com/falconindy/cower"
license=('MIT')
depends=('curl' 'openssl' 'pacman' 'yajl')
makedepends=('perl')
source=("http://code.falconindy.com/archive/$pkgname/$pkgname-$pkgver.tar.gz"{,.sig})
validpgpkeys=('487EACC08557AD082088DABA1EB2638FF56C0C53')  # Dave Reisner
md5sums=('e13a22c4e2595a95cf10fa4370fb0eee'
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
