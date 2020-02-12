# Maintainer: Jakob Gahde <j5lx@fmail.co.uk>

pkgname=ocaml-ppx_tools_versioned
pkgver=5.2.3
pkgrel=1
pkgdesc="Tools for authors of ppx rewriters and other syntactic tools (with ocaml-migrate-parsetree support)"
arch=('x86_64')
license=('MIT')
url="https://github.com/ocaml-ppx/ppx_tools_versioned"
depends=('ocaml' 'ocaml-migrate-parsetree')
makedepends=('dune')
options=('!strip')
source=("https://github.com/ocaml-ppx/ppx_tools_versioned/archive/${pkgver}.tar.gz")
sha512sums=('af20aa0031b9c638537bcdb52c75de95f316ae8fd455a38672a60da5c7c6895cca9dbecd5d56a88c3c40979c6a673a047d986b5b41e1e84b528b7df5d905b9b1')

build() {
  cd "${srcdir}/ppx_tools_versioned-${pkgver}"

  dune build --profile release
}

package() {
  cd "${srcdir}/ppx_tools_versioned-${pkgver}"

  dune install --destdir "${pkgdir}"
  install -Dm644 "LICENSE" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
  mv "${pkgdir}/usr/doc" "${pkgdir}/usr/share/"
}
