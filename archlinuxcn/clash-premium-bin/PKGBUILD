# Maintainer: yangon99 <yangon99_all@outlook.com>

pkgname=clash-premium-bin
pkgver=2023.05.29
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
sha512sums_i686=('cc78802448f03e858c74a24d09224e01f4c607aa2a4189bff7b6cd72abe025f47f0a56b70d8349a9e9b664c10e35096aded05a8c1450444ffd65f89d7cc30914')
sha512sums_x86_64=('3a79401a626c1412b735c7f7bfeb88f1d94825cc753cfd99a85bab54e2389c3f0744ed64e519ccef9ba6f2c0028df3ba92801c4dbc73ae762265aacbf7219f22')
sha512sums_arm=('c4c2f432069ae884912bfafecfe6e2a4f4d7763f0d9c7c065f3489a6d029b57ae3957d679c1daaa962265f566b5bea31f582abd5f0582c5d96bf39ee81acc291')
sha512sums_armv6h=('96e28d8deec9836b94483690d7f9b05c88bc8d005fb6615ce2ef64a1dc1215496007b95596fbe901259aeba2ab1444dbdcdfe28b6f0066b39de0c7ffb83a9327')
sha512sums_armv7h=('18a95c0ff171f3369e0c1df89a7bc153c5b8d7169db4ea6777d8079439bc33e653bb37b4f63824c9dba9a36364507de56c631fa93ca7d09215e0efa2dffe2f07')
sha512sums_aarch64=('cc6a0aa2182d997bb10ff600709ffcc41ba22a418abde23301c93409cdb852fdf61c20dd7dc1411fd265db4740e24ef63e02afc5d83c8eaf9d592f4c208dc983')
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
