# Maintainer: Mort Yao <soi@mort.ninja>
# Co-Maintainer: Felix Golatofski <contact@xdfr.de>
# Co-Maintainer: Xunarui Qi <me@xuanruiqi.com>
# Contributor: Serge Zirukin <ftrvxmtrx@gmail.com>
# Contributor: Sergei Lebedev <superbobry@gmail.com>
# Contributor: Guillem Rieu <guillemr@gmx.net>
# Contributor: Sergey Plaksin <serp256@gmail.com>
# Contributor: Nicolas Pouillard <nicolas.pouillard@gmail.com>

pkgname=ocaml-menhir
pkgver=20230608
pkgrel=1
pkgdesc="Menhir is a LR(1) parser generator for the OCaml."
arch=("x86_64")
url="http://cristal.inria.fr/~fpottier/menhir/"
license=('GPL' 'QPL')
depends=('ocaml>=4.03.0')
makedepends=('dune>=2.8.0' 'ocaml-findlib')
options=(!strip !makeflags)
source=("https://gitlab.inria.fr/fpottier/menhir/-/archive/${pkgver}/menhir-${pkgver}.tar.gz")
sha256sums=('56fef644e71721d6a95b6f2ab1afd9a032be0d9f92b53b851aab35d9e110a9a0')

build() {
  cd "$srcdir/${pkgname/ocaml-/}-$pkgver"
  dune build
}

package() {
  cd "$srcdir/${pkgname/ocaml-/}-$pkgver"
  dune install --destdir="${pkgdir}" --prefix="/usr" \
       --libdir="$(ocamlfind printconf destdir)"

  install -dm755 "${pkgdir}/usr/share/"
  mv "${pkgdir}/usr/doc" "${pkgdir}/usr/share/"
}

