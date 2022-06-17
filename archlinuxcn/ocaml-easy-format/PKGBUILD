# Author: Bruno Pagani <archange@archlinux.org>
# Maintainer: Zhiwei Chen <condy0919@gmail.com>

_pkgname=easy-format
pkgname=ocaml-${_pkgname}
pkgver=1.3.4
pkgrel=1
pkgdesc="Pretty-printing library for OCaml"
arch=('x86_64')
url="https://github.com/ocaml-community/${_pkgname}"
license=('BSD')
options=('!strip' 'staticlibs')
provides=('ocaml-easy-format')
depends=('glibc')
makedepends=('dune')
source=(${url}/releases/download/${pkgver}/${_pkgname}-${pkgver}.tbz )
sha256sums=('1dbf051e9f68574dde6e2e254a66b9c524ca425e80b36e99af96ed964ab610c3')

build() {
    cd "${srcdir}/${_pkgname}-${pkgver}"
    dune build -p easy-format
}

package() {
    cd ${_pkgname}-${pkgver}
    DESTDIR="${pkgdir}" dune install --prefix="/usr" --libdir="/usr/lib/ocaml"

    install -Dm644 LICENSE -t "${pkgdir}"/usr/share/licenses/${pkgname}/
    rm -rf "${pkgdir}"/usr/doc
}
