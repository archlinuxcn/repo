# Maintainer: yangon99 <yangon99_all@outlook.com>

pkgname=clash-premium-bin
pkgver=2022.04.10
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
sha512sums_i686=('29793d93626ff7eb05bcf3e0c2228984fe689ef51e01db22867103601eb0794106e81d9bab8392f93d27e8901da48752dbdf9e8b12dd03cfbcb8040d6d67936a')
sha512sums_x86_64=('c84e08ddadc5839d41379f59fb6d3bcfe26ff23162ca0172c5840ad86ece61187a951dd07dee7a6b020dec0c82a98414dd2b6848f3f50f271c09781f2fee1c35')
sha512sums_arm=('161adf41c0d036849f9fe8d3bec00cbadb74880ae92745ed8e29a7604392101df4061d4c4f2e13787b09206b320debab7da59bfb1691d58a02b1a0a924e54b0d')
sha512sums_armv6h=('4f645476ce8e051357b73df4acf1bb50fc816c5621066e0d3adbc6f6dd89d3645728e98b8d39cc5f5845694a2480d900e08e8c391081c62203ebc5690f2d5264')
sha512sums_armv7h=('7a0ba820bf80207eef3415d6f04fbe3a458695aff0b871bd7ec029429210a3e8c47959d34f691bf2a1c1c4762233adcaf3ff5422099a7a0d7596c9c14afd8ca9')
sha512sums_aarch64=('5e51d2da56aeb21e14c44deba160bcec713370040755c2862bbd5aaa8a35c28f4cbffb4f357d306b7001ff4b1e973a2d7f685414e5a3180590d91c596d78cbb7')
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
