# Maintainer: Jakob Gahde <j5lx@fmail.co.uk>

pkgname=ocaml-ocplib-endian
pkgver=1.0
pkgrel=1
pkgdesc="Optimised functions to read and write int16/32/64 from strings, bytes and bigarrays"
arch=('x86_64')
url="https://www.typerex.org/ocplib-endian.html"
license=('custom:LGPL2.1 with linking exception')
depends=('ocaml')
makedepends=('ocaml-findlib' 'ocamlbuild' 'cppo')
source=("https://github.com/OCamlPro/ocplib-endian/archive/${pkgver}.tar.gz")
sha512sums=('a08fd58ec5e72510c40e8b75e0ee8327ee658f479e45dd4632bc04e3907d04aaa3684df3b993ab63fc2a6c1f1a4fb32784e9b5258730d3b89a716300522d8d7f')

build() {
  cd "${srcdir}/ocplib-endian-${pkgver}"

  ./configure --disable-debug
  make build
}


package() {
  cd "${srcdir}/ocplib-endian-${pkgver}"

  export OCAMLFIND_DESTDIR="${pkgdir}$(ocamlfind printconf destdir)"
  install -dm755 "${OCAMLFIND_DESTDIR}"
  make install
  install -Dm644 "COPYING.txt" "${pkgdir}/usr/share/licenses/${pkgname}/COPYING.txt"
}
