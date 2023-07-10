# Maintainer: Infernio <infernio at icloud dot com>
pkgname=sssm
pkgver=1.2.1
pkgrel=1
pkgdesc="Simple Steam Skin Manager"
arch=('any')
url="https://github.com/Infernio/sssm"
license=('MIT')
depends=('bash' 'steam')
source=("${pkgname}_${pkgver}.tar.gz::https://github.com/Infernio/sssm/archive/${pkgver}.tar.gz")
sha256sums=('95844fe2e4518e12620090896c0dc92a4c26543fa17c283883f8efaad909b59d')

package() {
    cd "${srcdir}/${pkgname}-${pkgver}"
    install -Dm755 "sssm" "${pkgdir}/usr/bin/sssm"
    install -Dm644 "LICENSE" "${pkgdir}/usr/share/licenses/sssm/LICENSE"
}
