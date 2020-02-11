# Maintainer: Mort Yao <soi@mort.ninja>

pkgname=ocaml-pprint
_oname=pprint
pkgver=20180523
pkgrel=1
pkgdesc="An OCaml adaptation of Wadler's and Leijen's prettier printer."
arch=('i686' 'x86_64')
url='http://gallium.inria.fr/~fpottier/pprint/doc/PPrint.OCaml.html'
license=('BSD')
makedepends=('ocamlbuild' 'ocaml-findlib')
options=('!strip' '!makeflags' 'staticlibs')
source=("http://gallium.inria.fr/~fpottier/${_oname}/${_oname}-${pkgver}.tar.gz")
sha256sums=('adf050db5b552edd37dee2050e04b9b548c201f74d8f9beb6769ece6e04e8790')

build() {
  cd "$srcdir/$_oname-$pkgver"
  make -C src
}

package() {
  cd "$srcdir/$_oname-$pkgver"
  export OCAMLFIND_DESTDIR="$pkgdir$(ocamlfind printconf destdir)"
  install -dm 755 "$OCAMLFIND_DESTDIR"
  make -C src install
}
