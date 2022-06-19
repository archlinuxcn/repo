# Maintainer: yangon99 <yangon99_all@outlook.com>

pkgname=clash-premium-bin
pkgver=2022.06.19
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
sha512sums_i686=('ed7228f6d536f70312036fe0c9f29ec0a12cf7fa6bc47bd03cf7a2499c3f65a3af8185a31c1942ac62cab3db2e2ca4d60e4075711471d222ec07d0f1097d49a2')
sha512sums_x86_64=('e44dcf008c0d0552b2d0adba772b627fbaa9f7a377f0ce342a2cf4fdeb13720f517f4a99be0caf0d4564773ac19f3a2cb8808e0f18e0e7ff0feccd4408d44c2c')
sha512sums_arm=('3489035475f7154659d6a27c6e7ef8f9f5a2adada64ec04e39d5a6107c19639581b3ab9ba542727aa773522c5cc5ce6b5d476a3d2d9a8a1c8d9ff7d637f17c06')
sha512sums_armv6h=('36a8ac9d52182f89dcc5a3a9a0cf7cbe37499638a08725b00c3d37ce1e7492896dcb5b61fb69d5e8687fc3d0daf31b2edd5826bfa3ddd285945600da956da44f')
sha512sums_armv7h=('cb68dded9ae487a9a147f01381930542e487da29a8a66d3ae3c4d87d1aca0346b9b7da09c9d7ea153913de52729515654f675592ca4bf80720478b89d39f06ba')
sha512sums_aarch64=('1d3917208f3b02a9e57daa8f83b147547f0a5a8b1951388742221886b3ac0983e41fc9a08435c5a66e6ab04461ca3266e751a0b69d0646e91092923bac5d6f00')
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
