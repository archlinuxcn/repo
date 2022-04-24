# Maintainer: mark.blakeney at bullet-systems dot net
# Contributor: Tod Jackson <tod.jackson@gmail.com>
# Contributor: Özgür Sarıer <echo b3pndXJzYXJpZXIxMDExNjAxMTE1QGdtYWlsLmNvbQo= | base64 -d>
# Contributor: user6553591 <Message on Reddit>
# Contributor: P. Badredin <p dot badredin at gmail dot com>
# Contributor: Justin Blanchard <UncombedCoconut at gmail dot com>
# Contributor: Auguste Pop < auguste [at] gmail [dot] com >

pkgname=stockfish
pkgver=15
pkgrel=1
epoch=1
pkgdesc="A strong chess engine written by Tord Romstad, Marco Costalba, Joona Kiiski"
arch=('x86_64' 'i686' 'armv7h')
url="https://stockfishchess.org/"
license=('GPL3')
depends=('glibc')
source=("$pkgname-$pkgver.zip::https://github.com/official-stockfish/Stockfish/archive/sf_$pkgver.zip")
sha512sums=('96e0e5bc11d678c39b4b16286a6e1ec511fd75bcae704422fd65907930dda33bad28aa9b7d24d1d4092cc765dcc2a1fbe3d047916a26a0016e465788512c0913')

build() {
  cd "Stockfish-sf_${pkgver}/src"

  if [[ "$CARCH" == "armv7h" ]]; then
    _arch=armv7
  elif [[ "$CARCH" == "aarch64" ]]; then
    _arch=armv8
  elif [[ "$CARCH" == "i686" ]]; then
    _arch=x86-32
  elif grep -wq bmi2 /proc/cpuinfo; then
    _arch=x86-64-bmi2
  elif grep -w popcnt /proc/cpuinfo | grep -wqv cr8_legacy; then
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
