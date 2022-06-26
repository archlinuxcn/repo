# Author: Zhiwei Chen <condy0919@gmail.com>

pkgname=camlp-streams
pkgver=5.0
pkgrel=1 
pkgdesc='The Stream and Genlex libraries for use with Camlp4 and Camlp5'
arch=('x86_64')
url='https://github.com/ocaml/camlp-streams'
license=('LGPL')
options=('!strip' 'staticlibs')
provides=('camlp-streams')
makedepends=('dune')
source=("$url/archive/refs/tags/v${pkgver}.zip")
sha256sums=('b1ce2fa2727a2b71be5fe2e37c470d9e7879b6456ed33d6685692c7c1ebb14fa')

build() {
    cd ${pkgname}-${pkgver}
    dune build
}

package() {
    cd ${pkgname}-${pkgver}

    DESTDIR="${pkgdir}" dune install --prefix=/usr --libdir="$(ocamlfind printconf destdir)"

    rm -r "${pkgdir}"/usr/doc
}
