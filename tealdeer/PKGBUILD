# Maintainer: Maxim Andersson <thesilentboatman@gmail.com>

pkgname=tealdeer
pkgver=0.4.0
pkgrel=1
pkgdesc="An implementation of tldr in Rust"
arch=('i686' 'x86_64')
url="https://github.com/dbrgn/tealdeer"
license=('MIT' 'Apache')
makedepends=('rust' 'cargo')
provides=('tldr')
conflicts=('tldr' 'nodejs-tldr' 'nodejs-tldr-git' 'tldr-cpp-client' 'tldr-git' 'tldr-python-client')
source=("${pkgname}-${pkgver}.tar.gz::https://crates.io/api/v1/crates/${pkgname}/${pkgver}/download")
sha256sums=('356292978f1ac7f8b829caba9900f46b8784d93f722c1390b3a8588c76860693')

build() {
  cd "${srcdir}/${pkgname}-${pkgver}"

  cargo build --release
}

package() {
  cd "${srcdir}/${pkgname}-${pkgver}"

  install -D target/release/tldr -t "${pkgdir}/usr/bin"
}

# vim:set ts=2 sw=2 et:
