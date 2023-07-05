# Maintainer: Gleb Buzin <qufiwefefwoyn@gmail.com>
# Contributor: Vlad Frolov <frolvlad@gmail.com>

pkgname=jql
pkgver=7.0.0
pkgrel=1
pkgdesc="A JSON Query Language CLI tool"
url="https://github.com/yamafaktory/jql"
depends=('gcc-libs')
makedepends=('cargo')
arch=('i686' 'x86_64')
license=('MIT')
source=(${pkgname}-${pkgver}.tar.gz::https://github.com/yamafaktory/jql/archive/jql-v${pkgver}.tar.gz)
sha512sums=('db5fb743f66f853ca69698685f520b3b710a884c757c8336bbf51bc146b2fa1cda4561702d345bf5a967f58a3b19f43d86da0a0ef884a1952298bd578ddf5f6d')

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
