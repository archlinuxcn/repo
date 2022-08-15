# Maintainer: Mort Yao <soi@mort.ninja>
# Co-Maintainer: Felix Golatofski <contact@xdfr.de>
# Co-Maintainer: Xunarui Qi <me@xuanruiqi.com>
# Contributor: Serge Zirukin <ftrvxmtrx@gmail.com>
# Contributor: Sergei Lebedev <superbobry@gmail.com>
# Contributor: Guillem Rieu <guillemr@gmx.net>
# Contributor: Sergey Plaksin <serp256@gmail.com>
# Contributor: Nicolas Pouillard <nicolas.pouillard@gmail.com>

pkgname=ocaml-menhir
pkgver=20220210
pkgrel=1
pkgdesc="Menhir is a LR(1) parser generator for the OCaml."
arch=("x86_64")
url="http://cristal.inria.fr/~fpottier/menhir/"
license=('GPL' 'QPL')
depends=('ocaml>=4.02.3')
makedepends=('dune>=2.0' 'ocaml-findlib')
options=(!strip !makeflags)
source=("https://gitlab.inria.fr/fpottier/menhir/-/archive/${pkgver}/menhir-${pkgver}.tar.gz")
sha256sums=('4e27165777d9466c26a129c1c4ed60eb06875cbf6fda9a9e971d234e5ef7a314')

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

