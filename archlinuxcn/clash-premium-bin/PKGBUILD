# Maintainer: yangon99 <yangon99_all@outlook.com>

pkgname=clash-premium-bin
pkgver=2023.03.18
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
sha512sums_i686=('f9250e3c8d14e38e407b40ae4320508abd8d1e3181e606596c7e611e85d311cc8226065b57ac37e426a19a8f1be832129b4983ff63b39892d7e02d3d6d1d8bd3')
sha512sums_x86_64=('fc19828984c703ec2f4c1cba2b5a99d53c1c21f44dab5f933c64b8fba2c51b2add8d499d3a4794b3653fc8ef65f0d946e06be8a8daa54813748a5e587b6d5586')
sha512sums_arm=('21ae7df93972b80ef02832252dd8d8b0f40709ee4a958f9d795a0a2081a380804aa1964e94515b80ded6c815820913191615fc12e532c4138fba1ab0fb13c914')
sha512sums_armv6h=('c3550ea0bf9794e0027f914b0125e911277614501c95295fae87781df10d0ad12f3031281be127757b98642cdcbfdb6039bcb478999dc3c5e70c8846f500b6fe')
sha512sums_armv7h=('80cea75e7725c9024036916ddb900dd1e1bac4923522d68034641321c0d363673b8984e300b9b692eee20e12baba7b934de79fe35822eab0cbd2855652ef9f3a')
sha512sums_aarch64=('4a453e0244dac6fc18e698e1d2c9bac2f7fe88afe51ac3b69669669190c5cc298373365c28f909758b03840d9367f3db38f157b4134761d13afe9d7f9e906636')
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
