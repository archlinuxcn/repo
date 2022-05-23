# Author: Bruno Pagani <archange@archlinux.org>
# Maintainer: Zhiwei Chen <condy0919@gmail.com>

_pkgname=easy-format
pkgname=ocaml-${_pkgname}
pkgver=1.3.3
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
sha256sums=('eafccae911c26ca23e4ddacee3eaa54654d20f973b8680f84b708cef43adc416')

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
