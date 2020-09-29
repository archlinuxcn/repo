# Maintainer: Mort Yao <soi@mort.ninja>
# Co-Maintainer: Felix Golatofski <contact@xdfr.de>
# Contributor: Serge Zirukin <ftrvxmtrx@gmail.com>
# Contributor: Sergei Lebedev <superbobry@gmail.com>
# Contributor: Guillem Rieu <guillemr@gmx.net>
# Contributor: Sergey Plaksin <serp256@gmail.com>
# Contributor: Nicolas Pouillard <nicolas.pouillard@gmail.com>

pkgname=ocaml-menhir
pkgver=20200624
pkgrel=4
pkgdesc="Menhir is a LR(1) parser generator for the OCaml."
arch=("x86_64")
url="http://cristal.inria.fr/~fpottier/menhir/"
license=('GPL' 'QPL')
depends=('ocaml>=4.02.3')
makedepends=('dune>=2.0')
options=(!strip !makeflags)
source=("https://gitlab.inria.fr/fpottier/menhir/-/archive/${pkgver}/menhir-${pkgver}.tar.gz")
sha256sums=('cd89c21c0b5e5255d4b4ea2e51473a60aaecd4552609d14b637e79e247f65516')

build() {
  cd "$srcdir/${pkgname/ocaml-/}-$pkgver"

  dune build
}

package() {
  cd "$srcdir/${pkgname/ocaml-/}-$pkgver"

  dune install --prefix "${pkgdir}/usr" \
       --libdir "lib/ocaml"
}
