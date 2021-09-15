# Maintainer: yangon99 <yangon99_all@outlook.com>

pkgname=clash-premium-bin
pkgver=2021.09.15
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
sha512sums_i686=('dae4b928d6344c13e4077a5034897f7ff1b60dfde3961e8c9fa4b4c83a9cf87de9733240135830b5995dc188745bcc44510d96e9aa9a5936843d982cbb858087')
sha512sums_x86_64=('5548862f4c845e4e49672841292f40ecc856227795914f92ce32f98edce46728fcad9d46ad11aeca825159f568248e808c3816f56ae0c42c4719bfc57e2365cc')
sha512sums_arm=('a5d7047f051526cd2306df0a8ee8acaa8776c4888c24a324dd68b391c42f0158e6e2449a83e285201b0fb62d5f17898410622558449ba86de0c4cd96364b5da2')
sha512sums_armv6h=('87e6444e7a6af5e6caf25342c5bb25088bd88ce34356470364d10faa89b82b0f35aeee551124da57d4e01a3b29626eb6ce43026e23004f61320d7068b112e74d')
sha512sums_armv7h=('4b105dbd484f28c81ff98fe98761ae693bc432735aae081754497bda09947b64a953b463e8106d276c42ee9d5b10f7e8a0becef83b0061157ee531a3ae583d14')
sha512sums_aarch64=('2a57125417f7b20b69da01597280aa5b1d35e3b22e4f8ffaf0395549b04188cac9b55c3f23fd3b5951838a51ca75a4d8dd50e5f01d843d7ff46511fc82260006')
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
