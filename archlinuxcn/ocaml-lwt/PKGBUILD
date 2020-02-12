# Maintainer: Jakob Gahde <j5lx@fmail.co.uk>
# Contributor: Serge Zirukin <ftrvxmtrx@gmail.com>
# Contributor: Sergei Lebedev <superbobry@gmail.com
# Contributor: serp <serp256 at gmail dot com>

pkgname=ocaml-lwt
pkgver=4.3.0
pkgrel=1
pkgdesc="A library for cooperative threads in OCaml"
arch=('i686' 'x86_64')
url="http://ocsigen.org/lwt/"
license=('MIT')
depends=('ocaml' 'ocaml-mmap' 'ocaml-ocplib-endian' 'ocaml-result' 'ocaml-seq'
         'ocaml-migrate-parsetree' 'ocaml-ppx_tools_versioned' 'ocaml-react'
         'libev')
makedepends=('dune' 'cppo')
source=("https://github.com/ocsigen/lwt/archive/${pkgver}.tar.gz")
sha512sums=('8e66f5b2443b2cc2889cd3f425db6e7261165603f1c31f8800540900d944dc6ae99b5cf02a29244cfd40fa4b077f238a7a788ba970734faa47deec98b55ac252')
options=('!strip' 'staticlibs')

build() {
  cd "${srcdir}/lwt-${pkgver}"

  LWT_DISCOVER_ARGUMENTS="--use-libev true" dune build --profile release
}


package() {
  cd "${srcdir}/lwt-${pkgver}"

  dune install --destdir "${pkgdir}"
  install -Dm644 "LICENSE.md" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE.md"
  mv "${pkgdir}/usr/doc" "${pkgdir}/usr/share/"
}
