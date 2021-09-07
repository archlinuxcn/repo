# Maintainer: yangon99 <yangon99_all@outlook.com>

pkgname=clash-premium-bin
pkgver=2021.09.07
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
sha512sums_i686=('5e03bfefc506026d9ffdf5f6d9cfa53f4c0cfa8b5404d6f17cc5fde0b07b672ab7bbd0e7bddabec3932840b6abb962600876e793704ee94cf1f9ffa03d7ce857')
sha512sums_x86_64=('c361274340842b4666d7b70a25062c69ad8f64663f39f2e9d998c40ac73d0121713710c7d9bb0eb3dd99800a3b53f0d735a7e21388e30b2fa5b49554fba0273b')
sha512sums_arm=('2f79638e93f56e37278885e7876340ef26a83e100077a312f40243276d68ceb7f0c57ea775fc1d8beb7161cc601bd34e47bb6f3c1ec638ff68fa06fd21dac8b9')
sha512sums_armv6h=('e9070affb6cca869d3293cc7becebc160c4195fff1d770b50b21b4961e50e82cc38d97fffc69fb75be5a358c0d80032cf81345232926d9c284a0620a7ce73eb6')
sha512sums_armv7h=('27545b3cef94ecb7190ccdd8e0dd7a3985e12df293e731a64d3ea58704ae2b5af60e5b85cf5192e1403e37744a9028eea2d033fd2a8f1db1d9c8874a0ca214f3')
sha512sums_aarch64=('669176c8c3598f68827718f23e9430e9c988f72d5169b2290fc9fd5c27eb0a0880a9067c803b987b1de213c588a1b8962fce078078ab5542230ff73014c424e1')
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
