# Maintainer: Dct Mei <dctxmei@yandex.com>

pkgname=geph4-client
pkgver=4.4.10
pkgrel=1
pkgdesc="A command-line Geph4 toolset"
arch=('x86_64')
url="https://github.com/geph-official/geph4"
license=('GPL3')
groups=('geph4')
depends=('gcc-libs')
makedepends=('rust')
conflicts=('geph4-client-git')
backup=('etc/default/geph4-client')
source=("${pkgname}-${pkgver}.tar.gz::${url}/archive/geph4-client-v${pkgver}.tar.gz"
        "geph4-client.default"
        "geph4-client.service")
sha256sums=('4e23e8c121e7f72cebfc8953883a1b2c7c2313329c32070e91220d3aa0e0c38d'
            'fe10aa9e8ecc58e3b01487cb60c6fe970dd80343d1b715744e734077b1e14f66'
            '2aef927e466ce22796bbaec6d618f6178d0251e6d0ba1df3c526d3374dd903da')

build() {
    cd "${srcdir}"/"${groups}-${pkgname}-v${pkgver}"/
    cargo build --release --manifest-path=geph4-client/Cargo.toml
}

package() {
    cd "${srcdir}"/"${groups}-${pkgname}-v${pkgver}"/
    install -Dm 644 LICENSE.md "${pkgdir}"/usr/share/licenses/geph4-client/LICENSE
    install -Dm 755 target/release/geph4-client -t "${pkgdir}"/usr/bin/
    install -Dm 644 "${srcdir}"/geph4-client.default "${pkgdir}"/etc/default/geph4-client
    install -Dm 644 "${srcdir}"/geph4-client.service -t "${pkgdir}"/usr/lib/systemd/system/
}
