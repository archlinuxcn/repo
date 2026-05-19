# Maintainer: Yuzu Vita <g311571057 at gmail dot com>
pkgname=ktlint-compose-rules
pkgver=0.5.9
pkgrel=1
pkgdesc="Lint rules for ktlint/detekt aimed to contribute to a healthier usage of Compose. Actively maintained and evolved fork of the Twitter Compose rules"
arch=(any)
url="https://github.com/mrmans0n/compose-rules"
license=(Apache-2.0)
groups=()
depends=()
optdepends=(
    'ktlint: ktlint cli'
    'detekt-cli: detekt cli'
    'intellij-idea-community-edition'
    'intellij-idea-ultimate-edition'
)
source=("${pkgname}-${pkgver}.jar::${url}/releases/download/v${pkgver}/ktlint-compose-${pkgver}-all.jar")
sha256sums=('d4c7589b0dc0e4e20549fbca3bd44a5cd56a06e5936d6cd0cb6581a340801b9e')
package() {
    install -Dm644 ${pkgname}-${pkgver}.jar -t "${pkgdir}/usr/share/${pkgname}/"
}
