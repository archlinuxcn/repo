# Author: Bruno Pagani <archange@archlinux.org>
# Maintainer: Zhiwei Chen <condy0919@gmail.com>

_pkgname=easy-format
pkgname=ocaml-${_pkgname}
pkgver=1.3.2
pkgrel=6
pkgdesc="Pretty-printing library for OCaml"
arch=('x86_64')
url="https://github.com/ocaml-community/${_pkgname}"
license=('BSD')
options=('!strip' 'staticlibs')
provides=('ocaml-easy-format')
depends=('glibc')
makedepends=('dune')
source=(${url}/releases/download/${pkgver}/${_pkgname}-${pkgver}.tbz compile.patch)
sha256sums=('3440c2b882d537ae5e9011eb06abb53f5667e651ea4bb3b460ea8230fa8c1926'
            'ef631f2298d6ac15762f35a6eb3ff7e018d12cc86f4073e514bef24ebb212ecc')

build() {
    cd "${srcdir}/${_pkgname}-${pkgver}"
    patch src/easy_format.ml ${srcdir}/compile.patch
    dune build -p easy-format
}

package() {
    cd ${_pkgname}-${pkgver}
    DESTDIR="${pkgdir}" dune install --prefix=/usr --libdir="lib/ocaml"

    install -Dm644 LICENSE -t "${pkgdir}"/usr/share/licenses/${pkgname}/
    rm -rf "${pkgdir}"/usr/doc
}
