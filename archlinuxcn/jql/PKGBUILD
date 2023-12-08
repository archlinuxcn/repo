# Maintainer: Gleb Buzin <qufiwefefwoyn@gmail.com>
# Contributor: Vlad Frolov <frolvlad@gmail.com>

pkgname=jql
pkgver=7.1.1
pkgrel=1
pkgdesc="A JSON Query Language CLI tool"
url="https://github.com/yamafaktory/jql"
depends=('gcc-libs')
makedepends=('cargo')
arch=('i686' 'x86_64')
license=('MIT')
source=(${pkgname}-${pkgver}.tar.gz::https://github.com/yamafaktory/jql/archive/jql-v${pkgver}.tar.gz)
sha512sums=('fc584952a29f82e0aff7b075f3f803e9758834710f0d2f4dbd515353b34d45ff2dde52785d0618298654b00803458c6ee0543954e7e3fe718c825d0f4feab2e0')

build() {
  cd "${pkgname}-${pkgname}-v${pkgver}"
  cargo build --release --locked
}

check() {
  cd "${pkgname}-${pkgname}-v${pkgver}"
  cargo test --release --locked
}

package() {
  cd "${pkgname}-${pkgname}-v${pkgver}"
  install -Dm755 \
    "target/release/jql" \
    -t "${pkgdir}/usr/bin"
  install -Dm644 README.md -t "${pkgdir}/usr/share/doc/${pkgname}"
  install -Dm644 LICENSE-MIT -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
