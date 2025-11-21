# Maintainer: Yuzu Vita <g311571057 at gmail dot com>
pkgname=ktlint-compose-rules
pkgver=0.4.28
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
sha256sums=('a985a7f54344acf05066ded20437ef3fd4d8c567f27157278dbc9aa13754bb35')
package() {
    install -Dm644 ${pkgname}-${pkgver}.jar -t "${pkgdir}/usr/share/${pkgname}/"
}
