# Maintainer: Jakob Gahde <j5lx@fmail.co.uk>
# Contributor: Serge Zirukin <ftrvxmtrx@gmail.com>
# Contributor: Sergei Lebedev <superbobry@gmail.com>
# Contributor: serp <serp 256 at gmail dot com>

_pkgname=react
pkgname=ocaml-${_pkgname}
pkgver=1.2.1
pkgrel=1
pkgdesc="An OCaml module for functional reactive programming"
arch=('i686' 'x86_64')
url="http://erratique.ch/software/react"
license=('BSD')
depends=('ocaml')
makedepends=('ocamlbuild' 'ocaml-findlib' 'ocaml-topkg' 'opam')
source=("http://erratique.ch/software/${_pkgname}/releases/${_pkgname}-${pkgver}.tbz")
md5sums=('ce1454438ce4e9d2931248d3abba1fcc')

build() {
  cd "${srcdir}/${_pkgname}-${pkgver}"

  ocaml pkg/pkg.ml build
}

package() {
  cd "${srcdir}/${_pkgname}-${pkgver}"

  opam-installer --prefix=${pkgdir}/usr \
    --libdir=${pkgdir}$(ocamlc -where) \
    --docdir=${pkgdir}/usr/share/doc

  install -dm755 "${pkgdir}/usr/share/licenses/${pkgname}"
  mv "${pkgdir}/usr/share/doc/react/LICENSE.md" \
    "${pkgdir}/usr/share/licenses/${pkgname}/"
}
