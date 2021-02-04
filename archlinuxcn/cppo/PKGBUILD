# Maintainer: Hans-Nikolai Viessmann <hans AT viess DOT mn>
# Contributor: Jakob Gahde <j5lx@fmail.co.uk>
# Contributor: Bruno Pagani <archange@archlinux.org>

pkgname=cppo
pkgver=1.6.7
pkgrel=1
pkgdesc="C-style preprocessor for OCaml"
arch=('x86_64')
url="https://github.com/ocaml-community/cppo"
license=('BSD')
depends=('glibc')
optdepends=('ocamlbuild: ocamlbuild plugin')
makedepends=('dune' 'ocamlbuild')
source=("https://github.com/ocaml-community/cppo/releases/download/v${pkgver}/${pkgname}-v${pkgver}.tbz")
sha512sums=('9722b50fd23aaccf86816313333a3bf8fc7c6b4ef06b153e5e1e1aaf14670cf51a4aac52fb1b4a0e5531699c4047a1eff6c24c969f7e5063e78096c2195b5819')

build() {
  cd "${srcdir}/${pkgname}-v${pkgver}"

  dune build --profile release
}

check() {
  cd "${srcdir}/${pkgname}-v${pkgver}"

  dune runtest
}

package() {
  cd "${srcdir}/${pkgname}-v${pkgver}"
  DESTDIR="${pkgdir}" dune install --prefix "/usr" --libdir "lib/ocaml"

  install -Dm644 LICENSE.md "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE.md"
  mv "${pkgdir}/usr/doc" "${pkgdir}/usr/share/"
}
