# Author: Bruno Pagani <archange@archlinux.org>
# Maintainer: Zhiwei Chen <condy0919@gmail.com>

_pkgname=biniou
pkgname=ocaml-${_pkgname}
pkgver=1.2.1
pkgrel=4
pkgdesc="An optimized parsing and printing library for JSON"
arch=('x86_64')
url="https://github.com/ocaml-community/${_pkgname}"
license=('BSD')
options=('!strip' 'staticlibs')
provides=('ocaml-biniou')
depends=('ocaml-easy-format')
makedepends=('dune')
source=("${url}/releases/download/${pkgver}/${_pkgname}-${pkgver}.tbz")
sha256sums=('35546c68b1929a8e6d27a3b39ecd17b38303a0d47e65eb9d1480c2061ea84335')

build() {
    cd ${_pkgname}-${pkgver}
    make all
}

check() {
    cd ${_pkgname}-${pkgver}
    make test
}

package() {
    cd ${_pkgname}-${pkgver}
    DESTDIR="${pkgdir}" dune install --prefix=/usr --libdir="$(ocamlfind printconf destdir)"
    install -Dm644 LICENSE -t "${pkgdir}"/usr/share/licenses/${pkgname}/
    rm -r "${pkgdir}"/usr/doc
}
