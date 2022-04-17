# Maintainer: yangon99 <yangon99_all@outlook.com>

pkgname=clash-premium-bin
pkgver=2022.04.17
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
sha512sums_i686=('03e1c440401e4a1ce1b541650fabdbd5fd2e86b014f05baa0e2a999316fbe90e576a105bf17d1437f4ca5b9a924e73c40309405a3707500bf8ca015602b7b23d')
sha512sums_x86_64=('072cb6d6b35ae87e556e47b8041fa9126f63bc2de8cd8bfbcbb1cf5f1429adf3fd781c16dfa25f121ced43ef450b917bac1e50c9ea185d832228a7507b013415')
sha512sums_arm=('71ef25df045d9be7e2f9c4481790ba1e467dea2253a30d33493d2631486f6a81f4c3488463e107179d16d4c9faa6abd1df50a674cd58348074fa6a57f8d2d46b')
sha512sums_armv6h=('b9722c61d28daea504b38af9dc0f805bbb7ca8bb65a0fedf2afd822a9a8875bc2a104c69b7096007cc39d88413bab642a689810b820f1d192f26b9212bfb0ba9')
sha512sums_armv7h=('0cc8546156124cb529ce6e9011e5ea105d73e97d65a1806e0ff05c19e88cb0a8c5279d188a4fdfc20eba44757149aa9420cfac83272b738c2493e28eca484e78')
sha512sums_aarch64=('639d16c11479c8d3ae357b4b98b10a68319c11fd1393b06f24e5df2cecfbf14b39d5727cb5ed85d9396ac3f6735c304bd35d6667f62a8d72075d39941d0bc454')
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
