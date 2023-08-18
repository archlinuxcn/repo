# Maintainer: yangon99 <yangon99_all@outlook.com>

pkgname=clash-premium-bin
pkgver=2023.08.17
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
sha512sums_i686=('b5de9cb5b95fc03d2c972917e18fe0adf0e2477b08bf20fb136113ab6e90c827067f525c562dcb71b4f518d8f378647e9b6758a758937d13a7c417c60df47808')
sha512sums_x86_64=('8a02ace826ce383e7301fdc618655a1b253d101ecf2ff729d49c7f5efe43f4c25183f9ccd3fd1a5b73fda94e574b1fa4eb6615a95974c29cdfdaa8176cbed65b')
sha512sums_arm=('4ffca8ed3bb1723054108b2629cf45c63849e670b58864be57723a9a85b56b6ff50464f17b84e312d4f6c0585317b30b35c598a6b9d1f286bf797a6398aa05e0')
sha512sums_armv6h=('365671d8177814e617f6de4142d18495f84d5b7b76145e7cd2a8b001c9e2e4c0cb1e508ab7f2a43a21ced3ca1002f260d655af17ad29b2022e501adf1be2aacc')
sha512sums_armv7h=('ff8fbc2a7bd77e790f7ecf508001813e64772fa24e94e72111609778fd419a9b01dcece84cb77bf9e994b2f8ac463fdebe0d2e57d861a23e401ae6dcea92ccbf')
sha512sums_aarch64=('bbf13eb2b66cd4f59be8f5304ec1cad1fa202e0a629db398cad0fe03a0393ec8a780b59dbe8d6f611470c04d78917befc0b8c06ae7a27c42371c99312fea5cc8')
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
