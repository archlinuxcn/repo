# Author: Bruno Pagani <archange@archlinux.org>
# Maintainer: Zhiwei Chen <condy0919@gmail.com>

_pkgname=biniou
pkgname=ocaml-${_pkgname}
pkgver=1.2.2
pkgrel=1
pkgdesc="An optimized parsing and printing library for JSON"
arch=('x86_64')
url="https://github.com/ocaml-community/${_pkgname}"
license=('BSD')
options=('!strip' 'staticlibs')
provides=('ocaml-biniou')
depends=('ocaml-easy-format' 'camlp-streams')
makedepends=('dune')
source=("${url}/releases/download/${pkgver}/${_pkgname}-${pkgver}.tbz")
sha256sums=('8bf3ff17cd0ecb2d6b6d1d94cb08ef089d44caef96e9bae6be6839d428fa318f')

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
