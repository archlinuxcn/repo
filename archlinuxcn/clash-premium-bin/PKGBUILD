# Maintainer: yangon99 <yangon99_all@outlook.com>

pkgname=clash-premium-bin
pkgver=2020.12.27
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
sha512sums=("3d4b599a972caab7238f405d57e8ec74f9d0f51bc2b51f6656305f3a46aecd4d1d5c10a16415c3c158df1e0248f0aad327ddefc168d480c2674cec29602a31a0"
            "c08d9f25b8c7656b72da975c2ab580adfc8834a61c2dfec8296f19b6964460d12cad2100becadb7478cbccffa7c4805dbed80847c2a30075fc9fb31dee60ebe2")
source_i686=("${pkgname}-i686-${pkgver}.gz::https://github.com/Dreamacro/clash/releases/download/premium/clash-linux-386-${pkgver}.gz")
source_x86_64=("${pkgname}-x86_64-${pkgver}.gz::https://github.com/Dreamacro/clash/releases/download/premium/clash-linux-amd64-${pkgver}.gz")
source_arm=("${pkgname}-arm-${pkgver}.gz::https://github.com/Dreamacro/clash/releases/download/premium/clash-linux-armv5-${pkgver}.gz")
source_armv6h=("${pkgname}-armv6h-${pkgver}.gz::https://github.com/Dreamacro/clash/releases/download/premium/clash-linux-armv6-${pkgver}.gz")
source_armv7h=("${pkgname}-armv7h-${pkgver}.gz::https://github.com/Dreamacro/clash/releases/download/premium/clash-linux-armv7-${pkgver}.gz")
source_aarch64=("${pkgname}-aarch64-${pkgver}.gz::https://github.com/Dreamacro/clash/releases/download/premium/clash-linux-armv8-${pkgver}.gz")

sha512sums_i686=("bdcc68a5368c972259e3046aac530183172783c84249579412c4d8f41d63110040d0c905dc7d7706f5f4dd63b42002df8df3b7c8004526f3238c25170cfaadfd")
sha512sums_x86_64=("c78dcad1e58ab2129aa76f71a7006f006b30c2e8f1ba3d3ff2e1843125f82017c56f21a3ad32331993747368cd827dd4150995967183d901560de41871fe587a")
sha512sums_arm=("cc7c02a55b0d217ca02dd507d1ec1853325872160ae9a04e649806c9423f0e757703b384a96d85e1c558896ee4fbeb3223ca3b57901aad98a2980b76893e84c4")
sha512sums_armv6h=("bbe67d3c16068653ccb3b1f3674772268dbf26975ce7eebba20b49a00689b18863e753ee1dee0f78223fe0dc32e05dc839e36e2cbf7caad2975692f303bd19e2")
sha512sums_armv7h=("29076aa1d226a7324bc6aee4fd7380f7d5e6b2e606c1deeb060b2b8fa4b6e64ccd9e77713b179c6a91ead072dcd67a1bf56b8a1f17ff8645ff85ccff1bc6c370")
sha512sums_aarch64=("3010e22acc9c9663d638b37efd10cafef0e8f511990214c84c50920edfd7e6e1226543e405447966084b81d0f7311aaacad43ec5de95d832fbfb629873881985")

package() {
    cd ${srcdir}
    install -Dm755 "${pkgname}-${CARCH}-${pkgver}" "${pkgdir}/usr/bin/clash"
    install -Dm644 "clash@.service" "${pkgdir}/usr/lib/systemd/system/clash@.service"
    install -Dm644 "clash_user.service" "${pkgdir}/usr/lib/systemd/user/clash.service"
}
