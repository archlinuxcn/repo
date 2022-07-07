# Maintainer: yangon99 <yangon99_all@outlook.com>

pkgname=clash-premium-bin
pkgver=2022.07.07
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
sha512sums_i686=('a599a85ebe5216809ee2b8457cf674ede57b59683a1c67f077d181c209ab82e1b0cf417bb7890fbee592864bbe7b02437c9f2af70805cfc8966a04e9971d4ea9')
sha512sums_x86_64=('a107cff9628e9ee25aa4bb5cf3fa2832ddb9f14f29c481321ab613c1727d73ef5c1006777d3c29c1e1448d4738417c8779e9a4735fb828e3d739b9c5c257eef0')
sha512sums_arm=('586e3090d2055eb905faefcf93e1170666cd7446e7db057f1037407d0c8706745bdb8197d452c5301e3f11b67bcf34049c50f88c752f52087eb3d3349f595b4c')
sha512sums_armv6h=('29308d99e4afb2b0362106f298d7cf64aeec68fdb2e251035f3b2d48e48d41ace5047b62dd49b2cf18d457f3ce82a7a473f45e76b0ebc76ff7e96c8a8151ba54')
sha512sums_armv7h=('324e8491779351abe926c37e402eba60d2791135149ec4902a5f4944487ed8271944d50bb750405aa93478506740188b770c733dd7016616a66fdf8eef597a65')
sha512sums_aarch64=('e9e0ee9416baac87c45ff20524f89a34e3d2dc1de50a347faec6989eba480ac6a4361da301898b8cfc4fbf8464106c4fbea8693f2d0d4f8acd675aae71ac3138')
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
