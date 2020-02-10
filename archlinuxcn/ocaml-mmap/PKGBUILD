# Maintainer: Jakob Gahde <j5lx@fmail.co.uk>

pkgname=ocaml-mmap
pkgver=1.1.0
pkgrel=1
pkgdesc="Provides a Mmap.map_file functions for mapping files in memory"
arch=('x86_64')
url="https://github.com/mirage/mmap"
license=('custom:LGPL2.1 with linking exception')
depends=('ocaml')
makedepends=('dune')
source=("https://github.com/mirage/mmap/releases/download/v${pkgver}/mmap-v${pkgver}.tbz")
sha512sums=('15e4ec2634998f321f495de5372dc75a3f4059ab7512115603ae8fd99a619c91299d34c8a12a697aa36df4ce14c90c66746b873eddf004b7bbbeaef8ec7858f5')

build() {
  cd "${srcdir}/mmap-v${pkgver}"

  dune build --profile release
}


package() {
  cd "${srcdir}/mmap-v${pkgver}"

  dune install --destdir "${pkgdir}"
  install -Dm644 "LICENSE" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
  mv "${pkgdir}/usr/doc" "${pkgdir}/usr/share/"
}
