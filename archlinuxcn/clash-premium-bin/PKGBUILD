# Maintainer: yangon99 <yangon99_all@outlook.com>

pkgname=clash-premium-bin
pkgver=2023.02.16
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
sha512sums_i686=('215623ca3c6aaedd95bf76dfe7180fe25efd9ef066f2936260ec01ec32dc070f4063264eb8bd4c3ccd59279281d67d818e33c8ec393b394b35842e839f8342b0')
sha512sums_x86_64=('d13b09736507658d83a33aa4445d0d20cc5fcdf3ee0e31353c7ecb732948af47eb9b5eccb881942fb3912d0a4d984417fe94ce8905b91cc6c2d14f0b65af9295')
sha512sums_arm=('30721f1c9e8934efa41162fb89cd43c4457746355793a2375607ec1f092a2e15111b8f8e22880b2c71e0928c128cef519a4d3b4da8ccc78a894417c3f337c185')
sha512sums_armv6h=('b2d4be74c137424b5d3204beb03ed334570e470a0fe64f80f178b2152aa212dbdefd29644b974def92089fa3bf12669d983fdeb752c75c3e71f761a411bf9600')
sha512sums_armv7h=('a18fe08c0f63e185ed153a7cf1d5a38ca77363c6188e4e6dc619305060062fc811a5c5826fa2618284a95849691401485dd7f23683efe4e43bd783fc9c0c55ef')
sha512sums_aarch64=('c7990b56805b85514288e526e9aea555bfab19fcc6d3aa01d784a02048ffa2bc975ed0eb3c2d13c458af38b6a9051a108cd1b7671b72565d07b5c0c95debb4e5')
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
