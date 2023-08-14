# Maintainer: Gleb Buzin <qufiwefefwoyn@gmail.com>
# Contributor: Vlad Frolov <frolvlad@gmail.com>

pkgname=jql
pkgver=7.0.2
pkgrel=1
pkgdesc="A JSON Query Language CLI tool"
url="https://github.com/yamafaktory/jql"
depends=('gcc-libs')
makedepends=('cargo')
arch=('i686' 'x86_64')
license=('MIT')
source=(${pkgname}-${pkgver}.tar.gz::https://github.com/yamafaktory/jql/archive/jql-v${pkgver}.tar.gz)
sha512sums=('126243c536cbb384590076863d71fa3821d30e45b22bf83ed69da743dbe8007a520f7b5b5c1cc44b889e7172899b6880615ea587204deb1276eba022d6bca39a')

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
