# Author: Bruno Pagani <archange@archlinux.org>
# Maintainer: Zhiwei Chen <condy0919@gmail.com)

_pkgname=yojson
pkgname=ocaml-${_pkgname}
pkgver=1.7.0
pkgrel=2
pkgdesc="Low level JSON binary for OCaml"
arch=('x86_64')
url="https://github.com/ocaml-community/${_pkgname}"
license=('BSD')
options=('!strip' 'staticlibs')
provides=('ocaml-yojson')
conflicts=('ocaml-yojson')
depends=('ocaml-biniou' 'ocaml-easy-format')
makedepends=('dune' 'cppo')
source=(https://github.com/ocaml-community/${_pkgname}/releases/download/${pkgver}/${_pkgname}-${pkgver}.tbz)
sha256sums=('656fc65f794186274f8b961dc38daba9e2de2fc993829291defbda2186812cc6')

build() {
    cd ${_pkgname}-${pkgver}
    make all
}

package() {
    cd ${_pkgname}-${pkgver}

    DESTDIR="${pkgdir}" dune install --prefix=/usr --libdir="lib/ocaml"

    # remove rogue dune-package file
    rm -r "${pkgdir}"/usr/doc
    rm -r "${pkgdir}"/usr/lib/ocaml/${_pkgname}/dune-package
}
