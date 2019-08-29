# Maintainer: carstene1ns <arch carsten-teibes de> - http://git.io/ctPKG
# Contributor: trya <tryagainprod@gmail.com>
# Contributor: Ronald van Haren <ronald.archlinux.org>
# Contributor: damir <damir.archlinux.org>

pkgname=lib32-muparser
pkgver=2.2.6.1
pkgrel=1
pkgdesc="Fast math parser library (32 bit)"
arch=('x86_64')
url="http://muparser.beltoforion.de/"
license=('MIT')
depends=('muparser' 'lib32-gcc-libs')
makedepends=('gcc-multilib')
source=(muparser-$pkgver.tar.gz::"https://github.com/beltoforion/muparser/archive/v$pkgver.tar.gz")
sha256sums=('d2562853d972b6ddb07af47ce8a1cdeeb8bb3fa9e8da308746de391db67897b3')

build() {
  cd muparser-$pkgver

  export CC="gcc -m32"
  export CXX="g++ -m32"
  export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
  ./configure --prefix=/usr --libdir=/usr/lib32 --disable-samples
  make
}

package() {
  make -C muparser-$pkgver DESTDIR="$pkgdir" install
  # remove headers already present in muparser package
  rm -rf "$pkgdir"/usr/include
  # license
  install -d "$pkgdir"/usr/share/licenses
  ln -s muparser "$pkgdir"/usr/share/licenses/$pkgname
}
