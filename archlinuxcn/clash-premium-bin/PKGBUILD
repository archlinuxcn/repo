# Maintainer: yangon99 <yangon99_all@outlook.com>

pkgname=clash-premium-bin
pkgver=2021.11.08
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
sha512sums_i686=('befd638c52fdabc23752a7e29ea517d3e3eea7be07a13a5ab1cc152670a2ef97ac6aed676530a13d4b9c5bebfa1cfb9749ab87a92ba80217b82ab495191149e7')
sha512sums_x86_64=('4aef15d1646026473ecb0e95d82ed4f1073fa189a1d8f29a3e2c1f5621426415b4c7f5769774d0199c23ca5ee7b3d53fbebf3598a87cf1b222f6c66c7f45b2fb')
sha512sums_arm=('22a4b1b772a900bbf07ba0e93e5b7cf774f78e2eb0976ef95976274305683b45dcde199031ed141afc1b6e679e00e5e13fa44fa1adf4fa52a0bef70383d123d6')
sha512sums_armv6h=('b9c6d345690a1561c8bb66ec38c119272246e8e0019cadc52ed22f086a037fca97f96a5f42f13f061572832d3913d9779f3f6f19ce46e1aabc3f1b84b2b6af06')
sha512sums_armv7h=('440f76a21c80794a10e06615532fb409cd115afa5447d1910de451937f7d13acd59bdf1be5c06c10410f987c5a462144816fd441087ba960ec48aabec05545c7')
sha512sums_aarch64=('c5a73681083b0d345ed51a035d555ee818e928ac952e988106c906794f39469fbd8f5c8d51684328d35b00a3d532d5e8f40f79e63abd19e5d15eae75eaa1b696')
source_i686=("${pkgname}-i686-${pkgver}.gz::https://github.com/Dreamacro/clash/releases/download/premium/clash-linux-386-${pkgver}.gz")
source_x86_64=("${pkgname}-x86_64-${pkgver}.gz::https://github.com/Dreamacro/clash/releases/download/premium/clash-linux-amd64-${pkgver}.gz")
source_arm=("${pkgname}-arm-${pkgver}.gz::https://github.com/Dreamacro/clash/releases/download/premium/clash-linux-armv5-${pkgver}.gz")
source_armv6h=("${pkgname}-armv6h-${pkgver}.gz::https://github.com/Dreamacro/clash/releases/download/premium/clash-linux-armv6-${pkgver}.gz")
source_armv7h=("${pkgname}-armv7h-${pkgver}.gz::https://github.com/Dreamacro/clash/releases/download/premium/clash-linux-armv7-${pkgver}.gz")
source_aarch64=("${pkgname}-aarch64-${pkgver}.gz::https://github.com/Dreamacro/clash/releases/download/premium/clash-linux-armv8-${pkgver}.gz")


package() {
    cd ${srcdir}
    install -Dm755 "${pkgname}-${CARCH}-${pkgver}" "${pkgdir}/usr/bin/clash"
    install -Dm644 "clash@.service" "${pkgdir}/usr/lib/systemd/system/clash@.service"
    install -Dm644 "clash_user.service" "${pkgdir}/usr/lib/systemd/user/clash.service"
}
