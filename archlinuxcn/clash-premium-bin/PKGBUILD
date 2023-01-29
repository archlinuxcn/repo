# Maintainer: yangon99 <yangon99_all@outlook.com>

pkgname=clash-premium-bin
pkgver=2023.01.29
pkgrel=1
pkgdesc="Close-sourced pre-built Clash binary with TUN support"
provides=("clash")
conflicts=("clash" "clash-tun" "clash-dev-git")
arch=("i686" "x86_64" "arm" "armv6h" "armv7h" "aarch64")
url="https://github.com/Dreamacro/clash/releases/tag/premium"
license=("unknown")
depends=("glibc")
install=${pkgname}.install
source=("clash@.service"
        "clash_user.service")
sha512sums=('3d4b599a972caab7238f405d57e8ec74f9d0f51bc2b51f6656305f3a46aecd4d1d5c10a16415c3c158df1e0248f0aad327ddefc168d480c2674cec29602a31a0'
            'c08d9f25b8c7656b72da975c2ab580adfc8834a61c2dfec8296f19b6964460d12cad2100becadb7478cbccffa7c4805dbed80847c2a30075fc9fb31dee60ebe2')
sha512sums_i686=('2274d82f1c7cfbf3c3ec518f0eaea01d987b242f451cc0e3f79805fc043f8999008c46f887eaae465398abf92e473b0b23b35493f73f62be1873ecf37eea328f')
sha512sums_x86_64=('f0ccf29d3ef3c2259e745f45bf5f064d1ce188544b295282cfb15c6bac95e974f77fdac6a591f0edf2fb5d7c672777ff9d7634ea273d1812f76a0e9ba4f80a3a')
sha512sums_arm=('9f4fec3bba4cc8e4eccae7a30bb681ada4eb9911f52e6ca393f6c423f60b6c5cdb2c9e592211f0912cdff377c2b3d58f1a2238d9a02eaccec26adc54943db271')
sha512sums_armv6h=('bc54734c37e93f0ecb0aba77f037ed4963a87aa8c5d95c9ce98a31ab4fb0e6c146eefe0d07b7b14c0ca14f7fd8516659e288bbace5889f88b461ad7bee0daa1d')
sha512sums_armv7h=('d2f0167ed6e8a94177819179c03eb800288fcb0493498639e042b5f13578eba1be45f79345cdfa6f32f05a2737e7a70b416b6aa58ef077faa5fa2635b419f4a4')
sha512sums_aarch64=('e731bf52b1a3a5abadfc64f5c5caa22556da1ccf4361678b76e14f3f75bafce58b1fb101d8f0b6f71148f78715b4ebdc91305cc7c75462bafe3bbafa91e7601c')
source_i686=("${pkgname}-i686-${pkgver}.gz::https://github.com/Dreamacro/clash/releases/download/premium/clash-linux-386-${pkgver}.gz")
source_x86_64=("${pkgname}-x86_64-${pkgver}.gz::https://github.com/Dreamacro/clash/releases/download/premium/clash-linux-amd64-${pkgver}.gz")
source_arm=("${pkgname}-arm-${pkgver}.gz::https://github.com/Dreamacro/clash/releases/download/premium/clash-linux-armv5-${pkgver}.gz")
source_armv6h=("${pkgname}-armv6h-${pkgver}.gz::https://github.com/Dreamacro/clash/releases/download/premium/clash-linux-armv6-${pkgver}.gz")
source_armv7h=("${pkgname}-armv7h-${pkgver}.gz::https://github.com/Dreamacro/clash/releases/download/premium/clash-linux-armv7-${pkgver}.gz")
source_aarch64=("${pkgname}-aarch64-${pkgver}.gz::https://github.com/Dreamacro/clash/releases/download/premium/clash-linux-arm64-${pkgver}.gz")


package() {
    cd ${srcdir}
    install -Dm755 "${pkgname}-${CARCH}-${pkgver}" "${pkgdir}/usr/bin/clash"
    install -Dm644 "clash@.service" "${pkgdir}/usr/lib/systemd/system/clash@.service"
    install -Dm644 "clash_user.service" "${pkgdir}/usr/lib/systemd/user/clash.service"
}
