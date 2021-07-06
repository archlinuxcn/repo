# Maintainer: yangon99 <yangon99_all@outlook.com>

pkgname=clash-premium-bin
pkgver=2021.07.03
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
sha512sums_i686=('b1d898092b43339117dc1135dc7ded40e3a25521731eda319881e170fce00c0e2fc14910155f6f5bea7f99a79542f37c9e03c60127df17e963fe1e8e0ec98b04')
sha512sums_x86_64=('44ac83f07c3fce490862d8efa7827fa4fdd3bdcb6921149b318ab5fa40fd401835d5c6ad53a9ad42f3652f4ee467821ccf56611a09fd31bebb1ea8bf29790f22')
sha512sums_arm=('1d730b3d14edb7f9ebbefdff9b3c93f29ff44c659ce0079340c9f16c490558239632c51119dd63e3341eac63ca3cc4d2d6cde7555c429956b87524f13b01ad96')
sha512sums_armv6h=('fb565b127a61f73b70e4077d554c56bee5c4a1db3283ea94c6288948e04fabc8cfaa6a655902605b67a3835149b8eab6fa72e33360cd552e01357945b67200b5')
sha512sums_armv7h=('91fbf6f450ba7b1c9a51d012a8a18f0a73469c8e6d9dbde30ce79c31ae3c8343eb5855232d48da45f56c459f5b4d8f4c2c9936c28af37662b351778f3bf22926')
sha512sums_aarch64=('518106b990dc35295a35e56895bc5a87470a7bdb8f9325d2afe13fbf76c52d8978689512813c51f08ed4e2fed54539d8697030fd78ba0221f0e0a414d849e69d')
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
