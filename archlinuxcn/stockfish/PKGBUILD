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
pkgver=17.1
pkgrel=1
epoch=1
pkgdesc="A strong UCI chess engine"
arch=('x86_64' 'i686' 'armv7h' 'aarch64')
url="https://stockfishchess.org/"
license=('GPL-3.0')
depends=('glibc' 'gcc-libs')
# Check EvalFileDefaultName{Big,Small} in src/evaluate.h and change accordingly
_net_name_big=('1c0000000000')
_net_name_small=('37f18f62d772')
source=("$pkgname-$pkgver.zip::https://github.com/official-stockfish/Stockfish/archive/sf_$pkgver.zip"
        "https://tests.stockfishchess.org/api/nn/nn-${_net_name_big}.nnue"
        "https://tests.stockfishchess.org/api/nn/nn-${_net_name_small}.nnue")
sha512sums=('67745a8af08bd5c7b06872c3fec95ac2537cfd261cd61466542243d3d5e76b688965de696b84a17d369d3dc68af8a52614b4c9446e7bd5c4a5d6bbfd4ecb2e9e'
            '8f0aca52f6ce9b229eea6ab97c72ad74207d7c74cca8b35fb94ca349773bbe66d729b0d4bf7475a22cce2b5ebec0b605dd7625b98c2b6d0ce24227fddb969d7c'
            'bf4d01f8cbff94dbff484636dd0351cd66f37eeaea7b7dbe16a3bfe231ae78cfabdeed040b789b64049c6063ef0dca21e4a4f332b99e49a52993e8595e372839')

prepare() {
  ln -sf "${srcdir}/nn-${_net_name_big}.nnue" "Stockfish-sf_${pkgver}/src"
  ln -sf "${srcdir}/nn-${_net_name_small}.nnue" "Stockfish-sf_${pkgver}/src"
}

build() {
  cd "Stockfish-sf_${pkgver}/src"

  if [[ "$CARCH" == "armv7h" ]]; then
    _arch=armv7
  elif [[ "$CARCH" == "aarch64" ]]; then
    if grep -wq asimddp /proc/cpuinfo; then
      _arch=armv8-dotprod
    else
      _arch=armv8
    fi
  elif [[ "$CARCH" == "i686" ]]; then
    _arch=x86-32
  elif grep -wq avx512dq /proc/cpuinfo && grep -wq avx512vl /proc/cpuinfo && grep -wq avx512_vnni /proc/cpuinfo; then
    # 256 bit operands are faster on most hardware
    _arch=x86-64-vnni256
  elif grep -wq avx512f /proc/cpuinfo && grep -wq avx512bw /proc/cpuinfo; then
    _arch=x86-64-avx512
  elif grep -wq bmi2 /proc/cpuinfo; then
    if grep -wq GenuineIntel /proc/cpuinfo; then
      _arch=x86-64-bmi2
    elif grep -wq AuthenticAMD /proc/cpuinfo && [[ "$(grep --max-count=1 'cpu family' /proc/cpuinfo | sed -e 's/^.*: //')" -ge 25 ]]; then
      _arch=x86-64-bmi2
    else
      # On AMD, bmi2 is emulated before Zen 3, so that using it is a slowdown
      _arch=x86-64-avx2
    fi
  elif grep -wq avx2 /proc/cpuinfo; then
    _arch=x86-64-avx2
  elif grep -wq sse4_1 /proc/cpuinfo && grep -wq popcnt /proc/cpuinfo; then
    _arch=x86-64-sse41-popcnt
  elif grep -wq ssse3 /proc/cpuinfo; then
    _arch=x86-64-ssse3
  elif grep -wq pni /proc/cpuinfo && grep -wq popcnt /proc/cpuinfo; then
    _arch=x86-64-sse3-popcnt
  else
    _arch=x86-64
  fi

  if [[ "$CC" = "gcc" ]]
  then
    _COMP=gcc
  elif [[ "$CC" = "clang" ]]
  then
    _COMP=clang
  else
    _COMP=
  fi

  COMP=${_COMP} make ARCH="$_arch" profile-build
}

package() {
  cd "Stockfish-sf_${pkgver}/src"
  make PREFIX="$pkgdir/usr" install
}

# vim:set ts=2 sw=2 et:
