# Maintainer: yangon99 <yangon99_all@outlook.com>

pkgname=clash-premium-bin
pkgver=2020.12.21
pkgrel=1
pkgdesc="Close-sourced pre-built Clash binary with TUN support"
provides=('clash')
conflicts=('clash' 'clash-tun' 'clash-dev-git')
arch=('i686' 'x86_64' 'arm' 'armv6h' 'armv7h' 'aarch64')
url="https://github.com/Dreamacro/clash/releases/tag/premium"
license=('unknown')
depends=('glibc')
install=${pkgname}.install
source=("clash@.service"
        "clash_user.service")
sha512sums=('3d4b599a972caab7238f405d57e8ec74f9d0f51bc2b51f6656305f3a46aecd4d1d5c10a16415c3c158df1e0248f0aad327ddefc168d480c2674cec29602a31a0'
            'c08d9f25b8c7656b72da975c2ab580adfc8834a61c2dfec8296f19b6964460d12cad2100becadb7478cbccffa7c4805dbed80847c2a30075fc9fb31dee60ebe2')
source_i686=("${pkgname}-i686-${pkgver}.gz::https://github.com/Dreamacro/clash/releases/download/premium/clash-linux-386-${pkgver}.gz")
source_x86_64=("${pkgname}-x86_64-${pkgver}.gz::https://github.com/Dreamacro/clash/releases/download/premium/clash-linux-amd64-${pkgver}.gz")
source_arm=("${pkgname}-arm-${pkgver}.gz::https://github.com/Dreamacro/clash/releases/download/premium/clash-linux-armv5-${pkgver}.gz")
source_armv6h=("${pkgname}-armv6h-${pkgver}.gz::https://github.com/Dreamacro/clash/releases/download/premium/clash-linux-armv6-${pkgver}.gz")
source_armv7h=("${pkgname}-armv7h-${pkgver}.gz::https://github.com/Dreamacro/clash/releases/download/premium/clash-linux-armv7-${pkgver}.gz")
source_aarch64=("${pkgname}-aarch64-${pkgver}.gz::https://github.com/Dreamacro/clash/releases/download/premium/clash-linux-armv8-${pkgver}.gz")

sha512sums_i686=('4075443913970c5115e43aa9f2e4d7c5d1e0eeff620fc8b450a731447a906ec7a53f1689c1e4da750f8ee460dd027a58a84aa7d18afd73afdc8b9ea975c3053e')
sha512sums_x86_64=('6bbc085d2a5bfe51b8042f46fceef603bd2e8a6a8ac322767510918f7d2706ed36445eeda3641bcc93508e27bb7b352e7f031a0cda1e781238cc08b72b0c6d57')
sha512sums_arm=('8151b993a39ddadc40402264c7591202e5ebe7f42fafcf9335fd37ff4c2b0f6af3e5644a0d0daca7aab07481d9b561870296d9b0ef8f8996e303f990d0f7ac2c')
sha512sums_armv6h=('9f951ed0e5b3968f85c374f6374c0250ec4811ad1b8c99c51d602fcb6d3cb171c388e8eda8d3058f69ee05eb2e96e6e80bb9a0891ec766bdf56588b8b9d64aec')
sha512sums_armv7h=('e6f03611fbc7fe6e18605b4640aade97de88e21e1b4550d354169f8c5beeeed08ab3af4f7f06ed4832d2ff292170d959ae83bfd6e3b619c00583deaf81e5a436')
sha512sums_aarch64=('3b2a666af8aa55bb6f85b00610e7363feea8281a5f25591f770d847e6597ebb7f9fdd80712c377acdd906423f0cbff7932f2fe4f150441a4ef7135b1bafb69cf')

package() {
    cd ${srcdir}
    install -Dm755 "${pkgname}-${CARCH}-${pkgver}" "${pkgdir}/usr/bin/clash"
    install -Dm644 "clash@.service" "${pkgdir}/usr/lib/systemd/system/clash@.service"
    install -Dm644 "clash_user.service" "${pkgdir}/usr/lib/systemd/user/clash.service"
}
