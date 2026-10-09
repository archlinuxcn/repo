# Maintainer: Yuzu Vita <g311571057 at gmail dot com>
pkgname=ktlint-compose-rules
pkgver=0.6.8
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
sha256sums=('a25378ec616add11d2b279a87f54ccffefea87917da13773ff753386d30c22e5')
package() {
    install -Dm644 ${pkgname}-${pkgver}.jar -t "${pkgdir}/usr/share/${pkgname}/"
}
