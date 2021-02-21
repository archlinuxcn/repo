# Maintainer: yangon99 <yangon99_all@outlook.com>

pkgname=clash-premium-bin
pkgver=2021.02.21
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
sha512sums_i686=('829cb6a995c8808b7dbd1dc12b0473b6c467f34fe86a6169073d3eee98f50b771f53fb655caaf20e374d708abf62c510f7f868eda8566333b239748f87755667')
sha512sums_x86_64=('1de542f276a8c003e45420190231ec45b0cfa1db29337b0074fa1983f967b4d72c2ef8a66d49a4eab0860eb187e9cda7d40e9029cee0437a03f3ec08adccebeb')
sha512sums_arm=('3164fcdcffb7cbff73b77ff97ae9740594735e9b5c68aef0e0ef681f70ca082a9199f4bf37500ccc9c6c4fd09d40e35022745270a72d5f93f5e113414c02e4e7')
sha512sums_armv6h=('6cdacbaacd2ced37b4c6d2e258d63245e10e2bf8e7c25cac9b65577ec6cdfc0b1719a3d3bcce24eaa6973b8e87067bc60a70240d38c5ffcafe885b697976f6c2')
sha512sums_armv7h=('ab4803a1f98165834a970466d681e6da0e597d6d4e141ff86f197771e8b2ccf9b012ef85a5c8eabb39ab91bf088fdf8ebf1a50f77c3f16275005adf6eb365648')
sha512sums_aarch64=('f53deb1b9e8a963c18d8afcdf3932c717b945f80f20b83375295255e8643103dafc936ab80f177f8630949de4ac4f53aad74ee23bae7e9faa413c45be3d2e028')
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
