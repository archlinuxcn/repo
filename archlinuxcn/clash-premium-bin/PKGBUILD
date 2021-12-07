# Maintainer: yangon99 <yangon99_all@outlook.com>

pkgname=clash-premium-bin
pkgver=2021.12.07
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
sha512sums_i686=('34cf1056f71fa7e830fe50b84deca889dd71d1bffe1c0ba15cce83e4b839dca9ed640ae5c14a5227ccd8bd0388c8ae06f750c0b7c997a192a628e51bb91bffdb')
sha512sums_x86_64=('460a8cc50042ccffa0ce56aac4f33568496a163f234ead2cbec2e923f917e946e425ff3d4d170455bb6d583f484f1f010ba1b444757a9540d18560b3f317c4f0')
sha512sums_arm=('40a0af3df3591b2c0b1a5e339ca68f662adbef2defdeeb55bd0bb0502268e5c5d5a9896083072c65e32a50aead51c5679214a4e206b1e620c8495cc972d31a6b')
sha512sums_armv6h=('03f417d86dea709d084e8638bf2058cc8e54c3efcce876db64b453562b55edb31c5d6f0237575e2abdc73cf765868868c520b85940b8a2acf07d68fc39fcd809')
sha512sums_armv7h=('3e2386b6ca14a8f887db00851cf963cd393de2d1bd15836a808a845077e2893d26206187985fc3988341493e507e42dd1b363f5a0c2f5a219d99eb1f68908277')
sha512sums_aarch64=('637139496b9e166e3dcc1d64e6b3a5ce24aaa6991be5d88e9b61ad36a4650f2f24df7ee623db43091cf4e21d71c3ed8c90919d39c8944eeb1b5f2be763f60325')
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
