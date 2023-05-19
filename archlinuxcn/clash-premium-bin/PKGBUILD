# Maintainer: yangon99 <yangon99_all@outlook.com>

pkgname=clash-premium-bin
pkgver=2023.05.19
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
sha512sums_i686=('f20d2a3b6e476d4fb8edd84e646ea0acff3abbab6eaacf6c538c44970b9798ece9a54675160463a654f91f7280361570a8cfae1ca209a1d1e8b5fe7b9f7073d7')
sha512sums_x86_64=('2575085ff36bf5de7fc35a7af1c6ed48152c57aa5c06b44f1419a8f043a9a93d321d176eeb328a7e8f312c7b6b8e6f07cc8e5c29d4ddd2a1c1d3157aa07a0d45')
sha512sums_arm=('5a9fad3743faa6c3fa2cffe4f02a6115fb3ebc55fd838c2137afd0d30521eecbe6f6174e067f318b8d2990c99d20f9c0d83654f66dc1ad3884b4f14f398c6124')
sha512sums_armv6h=('5e5fa6582dd336f95487d75083d623051c2c054aa5709c746932d4217061cdc7467f75cd914cea8ffc6f5d7c8cf2342ee8449a874305002bd5bf4024f41e2dc6')
sha512sums_armv7h=('7ba1e95d62494347e9f1739ec7e443c3d05a0211d98b845b777880d05647bfb21d5a2739ee9a175e915a405312893624e4716533f6da579952ee3d2228141f64')
sha512sums_aarch64=('4e58d23a39f205609dad27dd17b8b869a1941d7b0f91be215adf1a06d83ad679ed222d807857da3c091ac0df9e3992871faedc72604ff64d716846c85e134c0f')
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
