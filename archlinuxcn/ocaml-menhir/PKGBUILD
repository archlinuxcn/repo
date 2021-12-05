# Maintainer: Mort Yao <soi@mort.ninja>
# Co-Maintainer: Felix Golatofski <contact@xdfr.de>
# Co-Maintainer: Xunarui Qi <me@xuanruiqi.com>
# Contributor: Serge Zirukin <ftrvxmtrx@gmail.com>
# Contributor: Sergei Lebedev <superbobry@gmail.com>
# Contributor: Guillem Rieu <guillemr@gmx.net>
# Contributor: Sergey Plaksin <serp256@gmail.com>
# Contributor: Nicolas Pouillard <nicolas.pouillard@gmail.com>

pkgname=ocaml-menhir
pkgver=20211128
pkgrel=1
pkgdesc="Menhir is a LR(1) parser generator for the OCaml."
arch=("x86_64")
url="http://cristal.inria.fr/~fpottier/menhir/"
license=('GPL' 'QPL')
depends=('ocaml>=4.02.3')
makedepends=('dune>=2.0')
options=(!strip !makeflags)
source=("https://gitlab.inria.fr/fpottier/menhir/-/archive/${pkgver}/menhir-${pkgver}.tar.gz")
sha256sums=('7f29f717b67ff31ad3dbabb17996f5171e6bba417f6fff1458dbdee71966c126')

build() {
  cd "$srcdir/${pkgname/ocaml-/}-$pkgver"
  dune build
}

package() {
  cd "$srcdir/${pkgname/ocaml-/}-$pkgver"
  dune install --prefix "${pkgdir}/usr" \
       --libdir "lib/ocaml"
}

