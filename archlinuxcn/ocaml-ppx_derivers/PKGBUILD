# Maintainer: Jakob Gahde <j5lx@fmail.co.uk>

pkgname=ocaml-ppx_derivers
pkgver=1.2.1
pkgrel=1
pkgdesc="Deriving plugin registry"
arch=('x86_64')
url="https://github.com/ocaml-ppx/ppx_derivers"
license=('BSD')
depends=('ocaml')
makedepends=('dune')
source=("https://github.com/ocaml-ppx/ppx_derivers/archive/${pkgver}.tar.gz")
sha512sums=('ef0796fe2592e653d34ba01d206d4b507429882a2aaadcb89c7f807c33a417f2871b0c94ade5c92aefd9487daa582e19d88ad5a5eaa631e8162ae12f4a0756c6')

build() {
  cd "${srcdir}/ppx_derivers-${pkgver}"

  dune build
}

package() {
  cd "${srcdir}/ppx_derivers-${pkgver}"

  install -dm755 "${pkgdir}$(ocamlfind -printconf destdir)" "${pkgdir}/usr/share"
  dune install --prefix "${pkgdir}/usr" --libdir "${pkgdir}$(ocamlfind -printconf destdir)"
  mv "${pkgdir}/usr/doc" "${pkgdir}/usr/share/"
  install -Dm644 "LICENSE.md" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE.md"
}
