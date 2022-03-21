# Maintainer: yangon99 <yangon99_all@outlook.com>

pkgname=clash-premium-bin
pkgver=2022.03.21
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
sha512sums_i686=('586ade7c8ead9e0dd604a485dc6154b943aee0bf2dfab05b4af574e0a53b1855dfd799ab13d5b627bd57fb0a9d619da40e95810d19ce24637cb31b2b6de7c4c0')
sha512sums_x86_64=('925f42e9cd2035aac415c7708eaf5fdb6198ecdf77f5a0d6ca394a738690bfb4c4c7063385f79bde4ebe84af1a5430038e7e6b587a50766b4147fb6c91f14098')
sha512sums_arm=('617dcab4063fe4f6a5632d881a9d07960b492b9dbe64f7e3b5a304784447ca70df434a65c309c5d2ea4f720a45e76995e4592fc75363207d7ff785b71d77fe3f')
sha512sums_armv6h=('33072ed5f9b9981dede7a5deaf01cc368bbb6304aa9fd11413f943b1327820180a31dd8a09411785fa85a640c9431c93719abd6410597c32520d47c176d6583b')
sha512sums_armv7h=('dd810eec580d2f592385360c717a2d62ef58b285b15c1512442efa24323d3f5fe85d059005ecf562cc2d0c714cd7e997fba148f4e079c819f212e755d64d543f')
sha512sums_aarch64=('cea8c184f31fbe81b4198ec562bf2a1250552372f244ded6a04e55d30b626de03f438d5515d5f702dc28fbf0619fbbeca44f68810e0daef38d574d304804ebee')
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
