# Maintainer: Jakob Gahde <j5lx@fmail.co.uk>

pkgname=ocaml-migrate-parsetree
pkgver=1.5.0
pkgrel=1
pkgdesc="Convert OCaml parsetrees between different versions"
arch=('i686' 'x86_64')
license=('custom:LGPL2.1 with linking exception')
url="https://github.com/ocaml-ppx/ocaml-migrate-parsetree"
depends=('glibc' 'ocaml' 'ocaml-result' 'ocaml-ppx_derivers')
makedepends=('dune')
options=('!strip')
source=("https://github.com/ocaml-ppx/ocaml-migrate-parsetree/releases/download/v${pkgver}/ocaml-migrate-parsetree-v${pkgver}.tbz")
sha512sums=('87fdccafae83b0437f1ccd4f3cfbc49e699bc0804596480e0df88510ba33410f31d48c7f677fe72800ed3f442a3a586d82d86aee1d12a964f79892833847b16a')

build() {
  cd "${srcdir}/ocaml-migrate-parsetree-v${pkgver}"

  dune build -p ocaml-migrate-parsetree
}

package() {
  cd "${srcdir}/ocaml-migrate-parsetree-v${pkgver}"

  dune install --destdir "${pkgdir}"
  install -Dm644 "LICENSE.md" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE.md"
  mv "${pkgdir}/usr/doc" "${pkgdir}/usr/share/"
}
