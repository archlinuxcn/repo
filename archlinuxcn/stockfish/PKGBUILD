# Maintainer: mark.blakeney at bullet-systems dot net
# Contributor: Tod Jackson <tod.jackson@gmail.com>
# Contributor: Özgür Sarıer <echo b3pndXJzYXJpZXIxMDExNjAxMTE1QGdtYWlsLmNvbQo= | base64 -d>
# Contributor: user6553591 <Message on Reddit>
# Contributor: P. Badredin <p dot badredin at gmail dot com>
# Contributor: Justin Blanchard <UncombedCoconut at gmail dot com>
# Contributor: Auguste Pop < auguste [at] gmail [dot] com >

pkgname=stockfish
pkgver=13
pkgrel=1
epoch=1
pkgdesc="A strong chess engine written by Tord Romstad, Marco Costalba, Joona Kiiski"
arch=('x86_64' 'i686' 'armv7h')
url="https://stockfishchess.org/"
license=('GPL3')
depends=('glibc')
source=("$pkgname-$pkgver.zip::https://github.com/official-stockfish/Stockfish/archive/sf_$pkgver.zip")
sha512sums=('9940b6513db5c59ea69aade090f02e6ddd267d7b2a23aba304611f3ed1a33735038ec58a1479141c42b2749b193d96f3ca93590f26baaf335400e83e7e039993')

build() {
  cd "Stockfish-sf_${pkgver}/src"

  if [[ "$CARCH" == "armv7h" ]]; then
    _arch=armv7
  elif [[ "$CARCH" == "i686" ]]; then
    _arch=x86-32
  elif grep -q bmi2 /proc/cpuinfo; then
    _arch=x86-64-bmi2
  elif grep -q popcnt /proc/cpuinfo; then
    _arch=x86-64-modern
  else
    _arch=x86-64
  fi

  make build ARCH="$_arch" COMP=gcc
}

package() {
  cd "Stockfish-sf_${pkgver}/src"
  make PREFIX="$pkgdir/usr" install
}

# vim:set ts=2 sw=2 et:
