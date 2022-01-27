# Maintainer: yangon99 <yangon99_all@outlook.com>

pkgname=clash-premium-bin
pkgver=2022.01.27
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
sha512sums_i686=('237a7c2d0d1ae14b97d01b76d9a9f8e015732de2182636eb26fb72a6902ed0363fd329b5c3789552ece437ce9293dfdde10ffbe34e5de41400c2530a022e437b')
sha512sums_x86_64=('2213c4f9e6479b8fb72a88a33c49bf19a2e83715389cce985423fdb01929786a4366529e48c5d59376cf66f9f11f0b3c1858633d0e97e98903e623f098f2cb9a')
sha512sums_arm=('97de006620dd00412049a1964306e676e9f4b5a1fa5b0f07dfa72c0d0ac4aba1097744c8339f64e907d5a824b6243f184e7dfb6dfac3370a1887becda6859d4d')
sha512sums_armv6h=('d2a12ed5a80f539c9b40987a18fd0f86e2a48077f1e74f180e78a708df0c28ebe9207b6f2f7066c0fba7d72e2e29cf30ce3318ca9b2401a2c746a18e5426b7c1')
sha512sums_armv7h=('33f983d3009a2405030fe2233ea327a31f4389a62c358f65d2d97eb45c5b30514d178b04b7eda82e5981255350bc1854b47f4b1c48bd48094cf46f602b352c22')
sha512sums_aarch64=('e246ae8dd5ecd8b5216183eff6ebbaa491dd034b58120da2c1698ea2a9c7fbf12ecb4c457516ba4c029e60fcec03d711e8c7b78e15ebf4a5b600cd74d45b7c9a')
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
