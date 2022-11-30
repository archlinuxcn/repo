# Maintainer: Gleb Buzin <qufiwefefwoyn@gmail.com>
# Contributor: Vlad Frolov <frolvlad@gmail.com>

pkgname=jql
pkgver=5.1.3
pkgrel=1
pkgdesc="A JSON Query Language CLI tool"
url="https://github.com/yamafaktory/jql"
depends=('gcc-libs')
makedepends=('cargo')
arch=('i686' 'x86_64')
license=('MIT')
source=(${pkgname}-${pkgver}.tar.gz::https://github.com/yamafaktory/jql/archive/v${pkgver}.tar.gz)
sha512sums=('99ac3671352d9945ed5b59776c3b0694560f6cb96cf45182e5a1136aef43750505a622b976295e6d84b29d3ce38fd399790e9295b602c208cdcc7d98236cfae4')

build() {
  cd "${pkgname}-${pkgver}"
  cargo build --release --locked
}

check() {
  cd "${pkgname}-${pkgver}"
  cargo test --release --locked
}

package() {
  cd "${pkgname}-${pkgver}"
  install -Dm755 \
    "target/release/jql" \
    -t "${pkgdir}/usr/bin"
  install -Dm644 README.md -t "${pkgdir}/usr/share/doc/${pkgname}"
  install -Dm644 LICENSE-MIT -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
