# Maintainer: Dct Mei <dctxmei@yandex.com>

pkgbase=geph4
pkgname=('geph4-binder'
         'geph4-bridge'
         'geph4-client'
         'geph4-exit'
         'geph4-vpn-helper')
pkgver=4.2.3
pkgrel=1
pkgdesc="A command-line Geph4 toolset"
arch=('x86_64')
url="https://github.com/geph-official/geph4"
license=('GPL3')
groups=('geph4')
depends=('gcc-libs')
makedepends=('rust')
source=("${pkgbase}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz"
        "geph4-binder.default"
        "geph4-bridge.default"
        "geph4-client.default"
        "geph4-exit.default"
        "geph4-binder.service"
        "geph4-bridge.service"
        "geph4-client.service"
        "geph4-exit.service"
        "geph4-vpn-helper.service")
sha256sums=('1d6578a21df81bf4f7b061db5a76be41f1597ebc977974c24f9db59441f0cf46'
            '96e495d1f5d6cb61c7953c70035125febf0063fa0e8d0bb47bc314d326c93b55'
            '3def2cd4cce25ad38cadc3b20913d3c45df16b89d0903b7cd88da77d57f86938'
            '01b1ec9c4a5fe499d015cc5da62b46245f6bb9acc30afa5ec1f982650e331223'
            '2daf5117a98d4529225712cb9f4828f4f5269a591565745497df0eb10068ba2a'
            '7c8c2b2e2f24a45a2d216af90d1b370a25d1f4fe3501f341bf18b7b68a7fa93a'
            '08bcd5c7d8a44f7ee05315ce745658a59bf48f0c5475b231c75120858ddf39ef'
            '3599ecabf51e9405eb3afdc0c653060e8da9d6cbe83a4f4ce14c46017f520022'
            '04b096c9e99f655c7f7e9e13082be2a487e255c2366471ad9c9e3216be389774'
            '806ed9538c92e659e2c0f70f8f5620f37e2f7df15b39a9bdea301b65c5cbcf5f')

build() {
    cd "${srcdir}"/"${pkgbase}-${pkgver}"/
    cargo build --release --manifest-path=geph4-binder/Cargo.toml
    cargo build --release --manifest-path=geph4-bridge/Cargo.toml
    cargo build --release --manifest-path=geph4-client/Cargo.toml
    cargo build --release --manifest-path=geph4-exit/Cargo.toml
    cargo build --release --manifest-path=geph4-vpn-helper/Cargo.toml
}

package_geph4-binder() {
    conflicts=('geph4-binder-git')
    backup=('etc/default/geph4-binder')
    cd "${srcdir}"/"${pkgbase}-${pkgver}"/
    install -Dm 644 LICENSE.md "${pkgdir}"/usr/share/licenses/geph4-binder/LICENSE
    install -Dm 755 target/release/geph4-binder -t "${pkgdir}"/usr/bin/
    install -Dm 644 "${srcdir}"/geph4-binder.default "${pkgdir}"/etc/default/geph4-binder
    install -Dm 644 "${srcdir}"/geph4-binder.service -t "${pkgdir}"/usr/lib/systemd/system/
}

package_geph4-bridge() {
    conflicts=('geph4-bridge-git')
    backup=('etc/default/geph4-bridge')
    cd "${srcdir}"/"${pkgbase}-${pkgver}"/
    install -Dm 644 LICENSE.md "${pkgdir}"/usr/share/licenses/geph4-bridge/LICENSE
    install -Dm 755 target/release/geph4-bridge -t "${pkgdir}"/usr/bin/
    install -Dm 644 "${srcdir}"/geph4-bridge.default "${pkgdir}"/etc/default/geph4-bridge
    install -Dm 644 "${srcdir}"/geph4-bridge.service -t "${pkgdir}"/usr/lib/systemd/system/
}

package_geph4-client() {
    conflicts=('geph4-client-git')
    backup=('etc/default/geph4-client')
    cd "${srcdir}"/"${pkgbase}-${pkgver}"/
    install -Dm 644 LICENSE.md "${pkgdir}"/usr/share/licenses/geph4-client/LICENSE
    install -Dm 755 target/release/geph4-client -t "${pkgdir}"/usr/bin/
    install -Dm 644 "${srcdir}"/geph4-client.default "${pkgdir}"/etc/default/geph4-client
    install -Dm 644 "${srcdir}"/geph4-client.service -t "${pkgdir}"/usr/lib/systemd/system/
}

package_geph4-exit() {
    conflicts=('geph4-exit-git')
    backup=('etc/default/geph4-exit')
    cd "${srcdir}"/"${pkgbase}-${pkgver}"/
    install -Dm 644 LICENSE.md "${pkgdir}"/usr/share/licenses/geph4-exit/LICENSE
    install -Dm 755 target/release/geph4-exit -t "${pkgdir}"/usr/bin/
    install -Dm 644 "${srcdir}"/geph4-exit.default "${pkgdir}"/etc/default/geph4-exit
    install -Dm 644 "${srcdir}"/geph4-exit.service -t "${pkgdir}"/usr/lib/systemd/system/
}

package_geph4-vpn-helper() {
    depends+=('geph4-client')
    conflicts=('geph4-vpn-helper-git')
    cd "${srcdir}"/"${pkgbase}-${pkgver}"/
    install -Dm 644 LICENSE.md "${pkgdir}"/usr/share/licenses/geph4-vpn-helper/LICENSE
    install -Dm 755 target/release/geph4-vpn-helper -t "${pkgdir}"/usr/bin/
    install -Dm 644 "${srcdir}"/geph4-vpn-helper.service -t "${pkgdir}"/usr/lib/systemd/system/
}
