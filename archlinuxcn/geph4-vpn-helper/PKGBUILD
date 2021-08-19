# Maintainer: Dct Mei <dctxmei@yandex.com>

pkgname=geph4-vpn-helper
pkgver=0.1.4
pkgrel=1
pkgdesc="A command-line Geph4 toolset"
arch=('x86_64')
url="https://github.com/geph-official/geph4"
license=('GPL3')
groups=('geph4')
depends=('gcc-libs' 'geph4-client')
makedepends=('rust')
conflicts=('geph4-vpn-helper-git')
source=("${pkgname}-${pkgver}.tar.gz::${url}/archive/geph4-vpn-helper-v${pkgver}.tar.gz"
        "geph4-vpn-helper.service")
sha256sums=('952440d5945db031ee615c83cb9492dc35021845b7ba2872f0eceef9f82c0e5d'
            'ae990333a1eebd5d5bb57ebd4a930db84d08a2c7db541d349de119280473e043')

build() {
    cd "${srcdir}"/"${groups}-${pkgname}-v${pkgver}"/
    cargo build --release --manifest-path=geph4-vpn-helper/Cargo.toml
}

package() {
    cd "${srcdir}"/"${groups}-${pkgname}-v${pkgver}"/
    install -Dm 644 LICENSE.md "${pkgdir}"/usr/share/licenses/geph4-vpn-helper/LICENSE
    install -Dm 755 target/release/geph4-vpn-helper -t "${pkgdir}"/usr/bin/
    install -Dm 644 "${srcdir}"/geph4-vpn-helper.service -t "${pkgdir}"/usr/lib/systemd/system/
}
