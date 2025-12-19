# Maintainer: Yuzu Vita <g311571057 at gmail dot com>
pkgname=ktlint-compose-rules
pkgver=0.5.3
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
sha256sums=('f946582029dd276fb857b626aea3be66811a9501006f2f39c38c593d669b29a4')
package() {
    install -Dm644 ${pkgname}-${pkgver}.jar -t "${pkgdir}/usr/share/${pkgname}/"
}
