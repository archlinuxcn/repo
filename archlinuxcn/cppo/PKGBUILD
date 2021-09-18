# Maintainer: Hans-Nikolai Viessmann <hans AT viess DOT mn>
# Contributor: Jakob Gahde <j5lx@fmail.co.uk>
# Contributor: Bruno Pagani <archange@archlinux.org>

pkgname=cppo
pkgver=1.6.8
pkgrel=1
pkgdesc="C-style preprocessor for OCaml"
arch=('x86_64')
url="https://github.com/ocaml-community/cppo"
license=('BSD')
depends=('glibc')
optdepends=('ocamlbuild: ocamlbuild plugin')
makedepends=('dune' 'ocamlbuild')
source=("https://github.com/ocaml-community/cppo/archive/refs/tags/v${pkgver}.tar.gz")
sha256sums=('7e056d50bb194b7f628d2547667262ceb814b1fe9ea666240bfaf1396727be53')

build() {
  cd "${srcdir}/${pkgname}-${pkgver}"

  dune build --profile release
}

check() {
  cd "${srcdir}/${pkgname}-${pkgver}"

  dune runtest
}

package() {
  cd "${srcdir}/${pkgname}-${pkgver}"
  DESTDIR="${pkgdir}" dune install --prefix "/usr" --libdir "lib/ocaml"

  install -Dm644 LICENSE.md "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE.md"
  mv "${pkgdir}/usr/doc" "${pkgdir}/usr/share/"
}
