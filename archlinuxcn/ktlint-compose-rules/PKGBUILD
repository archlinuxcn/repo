# Maintainer: Yuzu Vita <g311571057 at gmail dot com>
pkgname=ktlint-compose-rules
pkgver=0.6.0
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
sha256sums=('76169e3c475dc0b2af01d920316d6fd2ee6c26cf94174707948fb0bb99adb25b')
package() {
    install -Dm644 ${pkgname}-${pkgver}.jar -t "${pkgdir}/usr/share/${pkgname}/"
}
