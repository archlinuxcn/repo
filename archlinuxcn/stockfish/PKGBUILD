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
pkgver=19
pkgrel=1
epoch=1
pkgdesc="A strong UCI chess engine"
arch=('x86_64' 'i686' 'armv7h' 'aarch64')
url="https://stockfishchess.org/"
license=('GPL-3.0')
depends=('glibc' 'gcc-libs')
_net_name="nn-1a298aa575a0.nnue" # From EvalFileDefaultName in src/evaluate.h
source=("$pkgname-$pkgver.zip::https://github.com/official-stockfish/Stockfish/archive/sf_$pkgver.zip"
        "https://tests.stockfishchess.org/api/nn/${_net_name}")
sha512sums=('49e073b15cf56d1aab7e2e23d883e5d1737b3176441051ca42c2214f8b606b919b95c7a7ca47051e133c02a49d77f68ebb072398a1ed18b8f7a27fcb1773a2d0'
            '136a0f9725da7b692894a080d03d61bbfc67dcabf2f869b008891dbf042dfacb74c75df12a48bb9a9c736ce3accd670a55afae5ee40f090a0b86558e459c70bb')

prepare() {
  ln -sf "${srcdir}/${_net_name}" "Stockfish-sf_${pkgver}/src"
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
