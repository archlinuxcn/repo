# Maintainer: Mort Yao <soi@mort.ninja>
# Co-Maintainer: Felix Golatofski <contact@xdfr.de>
# Contributor: Serge Zirukin <ftrvxmtrx@gmail.com>
# Contributor: Sergei Lebedev <superbobry@gmail.com>
# Contributor: Guillem Rieu <guillemr@gmx.net>
# Contributor: Sergey Plaksin <serp256@gmail.com>
# Contributor: Nicolas Pouillard <nicolas.pouillard@gmail.com>

pkgname=ocaml-menhir
pkgver=20210419
pkgrel=1
pkgdesc="Menhir is a LR(1) parser generator for the OCaml."
arch=("x86_64")
url="http://cristal.inria.fr/~fpottier/menhir/"
license=('GPL' 'QPL')
depends=('ocaml>=4.02.3')
makedepends=('dune>=2.0')
options=(!strip !makeflags)
source=("https://gitlab.inria.fr/fpottier/menhir/-/archive/${pkgver}/menhir-${pkgver}.tar.gz")
sha256sums=('6b75a92276f1cdc8f1ea5030adad344a10bfce9077de274f621f5ef2c3428920')

build() {
  cd "$srcdir/${pkgname/ocaml-/}-$pkgver"

  dune build
}

package() {
  cd "$srcdir/${pkgname/ocaml-/}-$pkgver"

  dune install --prefix "${pkgdir}/usr" \
       --libdir "lib/ocaml"
}
