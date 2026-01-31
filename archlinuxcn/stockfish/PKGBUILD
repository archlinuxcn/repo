# Maintainer: niklas.fiekas at backscattering dot de
# Contributor: mark.blakeney at bullet-systems dot net
# Contributor: Tod Jackson <tod.jackson@gmail.com>
# Contributor: Özgür Sarıer <echo b3pndXJzYXJpZXIxMDExNjAxMTE1QGdtYWlsLmNvbQo= | base64 -d>
# Contributor: user6553591 <Message on Reddit>
# Contributor: P. Badredin <p dot badredin at gmail dot com>
# Contributor: Justin Blanchard <UncombedCoconut at gmail dot com>
# Contributor: Auguste Pop < auguste [at] gmail [dot] com >
# Contributor: SandaruKasa <echo c2FuZGFydWthc2ErYXVyQHlhLnJ1Cg== | base64 -d>
# Contributor: bagasdotme
# Contributor: HurricanePootis

pkgname=stockfish
pkgver=18
pkgrel=1
epoch=1
pkgdesc="A strong UCI chess engine"
arch=('x86_64' 'i686' 'armv7h' 'aarch64')
url="https://stockfishchess.org/"
license=('GPL-3.0')
depends=('glibc' 'gcc-libs')
# Check EvalFileDefaultName{Big,Small} in src/evaluate.h and change accordingly
_net_name_big=('c288c895ea92')
_net_name_small=('37f18f62d772')
source=("$pkgname-$pkgver.zip::https://github.com/official-stockfish/Stockfish/archive/sf_$pkgver.zip"
        "https://tests.stockfishchess.org/api/nn/nn-${_net_name_big}.nnue"
        "https://tests.stockfishchess.org/api/nn/nn-${_net_name_small}.nnue")
sha512sums=('1a0b36fc70146aefccc45a1647d04a5ac409df811a527fc7f679bb966271b5fd3348d3c9ecb3277ffcacda2dd760b6f06dbba677aa10b0553c445237e5ee544f'
            '9568d21d7b229ec9c8ee97363e94560858f3f44f4c6647ec11770f617b4a3b03cbcfa445c407f52a6104f281d43e19e0f461cc13c875218b543860ebc8411622'
            'bf4d01f8cbff94dbff484636dd0351cd66f37eeaea7b7dbe16a3bfe231ae78cfabdeed040b789b64049c6063ef0dca21e4a4f332b99e49a52993e8595e372839')

prepare() {
  ln -sf "${srcdir}/nn-${_net_name_big}.nnue" "Stockfish-sf_${pkgver}/src"
  ln -sf "${srcdir}/nn-${_net_name_small}.nnue" "Stockfish-sf_${pkgver}/src"
}

build() {
  cd "Stockfish-sf_${pkgver}/src"

  if [[ "$CC" = "gcc" ]]
  then
    _COMP=gcc
  elif [[ "$CC" = "clang" ]]
  then
    _COMP=clang
  else
    _COMP=
  fi

  COMP=${_COMP} make profile-build
}

package() {
  cd "Stockfish-sf_${pkgver}/src"
  make PREFIX="$pkgdir/usr" install
}

# vim:set ts=2 sw=2 et:
