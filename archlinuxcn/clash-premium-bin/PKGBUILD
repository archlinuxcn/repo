# Maintainer: yangon99 <yangon99_all@outlook.com>

pkgname=clash-premium-bin
pkgver=2023.06.30
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
sha512sums_i686=('82c8947d39cef5b4113f23c8b8e5728af7d83f6b8b4ffb973a49b756a18dce52e6c090d755a747e8014c5365a27fd11e6b3ff419dcd7a578b1cb8b845c08a64a')
sha512sums_x86_64=('9c7ceff28dbb808bb9ea70dc288084c520af0009be40a2dbee6bd4b25372ea355a1c10990616a0076055e3958e4e8b27d1c1df4e320dad8d3d90f8645f9203e6')
sha512sums_arm=('4cedb7c5102e54d3ae186b16f17246d638d7887e45b11825f70672aa43844fb1d3742db00ef2d8b2e897000becc965c1ff5ab7e2c44476a25dc7efa172a4b38d')
sha512sums_armv6h=('7dcaf26949ad09113d7a739214bec02afbe191a8427402b30042c69f996aeb8685a59be49b77635be0fc28a871b6d6f36042a8e1539845484b2e6672f88379a5')
sha512sums_armv7h=('7c39f8ec0cc58194cb28396e4bdcae6095c54cc5f27a3dfeffa8f5c6eae1b45f2bb3539fc46857bf9c5cc844318885574a4b4809e56cf7306924ce869b736ac8')
sha512sums_aarch64=('66a78df731fde400fd1f6500c5767bea289a341a57f0db7be3871dd0c2914a57b8bc6557b7eacaa2034dcefd6b45a43741fb6cd2ebbbec9dc333a6687a3feab3')
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
