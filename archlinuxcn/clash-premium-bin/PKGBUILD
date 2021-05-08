# Maintainer: yangon99 <yangon99_all@outlook.com>

pkgname=clash-premium-bin
pkgver=2021.05.08
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
sha512sums_i686=('844ca92c89e3ecf57163fb5c791a3c627dd25cf4b9dfc864931f0e8da82f220557ad425b5c8a4a0f8e838aedcd72f1666838ab12bfd2cebc9d9d70af86447ea0')
sha512sums_x86_64=('508dfbdd3fcefa929078377945f88ff180a1e06b64391cc4ddf745b78448c1d87092c3de99adf4271736a9c687e9a29b8045d314dab57409ac4c2a8eab669661')
sha512sums_arm=('69a8cc29dd8ac993082d2c2a1c4dfb5a7342303caf0781bca81f0e5be05c0df6000372ece64c496fb2f2285b8f2527b925419e672c33d733b52078b7ef2fffbe')
sha512sums_armv6h=('bbcfb7918d742151de067fc1f98c97022f16dcd4fddf6cc45bb2218fca2856a89914c7bea6d792c010357404f47d4eb462a1272ac8d02dfbc62eedb072806acb')
sha512sums_armv7h=('5e719b35960e42da9d38ea72730f9c71d26807d1e5d7ec8b5841c01c41bd71f6811e386aad0c0f66dcadf4357a797fa83f0e31cf0106cd96bc2a1943459674b0')
sha512sums_aarch64=('ef2faed0b52d8caca283992641bab30c1581bfb0414d2f8a9bbe1eaeb92f0030e8df423fb19a3bd8f087ad1d5536c334f00a58ee8d533b76681c3551b0b12eb0')
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
