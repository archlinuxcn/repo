# Maintainer: yangon99 <yangon99_all@outlook.com>

pkgname=clash-premium-bin
pkgver=2020.11.20
pkgrel=1
pkgdesc="Close-sourced pre-built Clash binary with TUN support"
provides=('clash')
conflicts=('clash' 'clash-tun' 'clash-dev-git')
arch=('i686' 'x86_64' 'arm' 'armv6h' 'armv7h' 'aarch64')
url="https://github.com/Dreamacro/clash/releases/tag/premium"
license=('unknown')
depends=('glibc')
install=${pkgname}.install
source=("clash@.service"
        "clash_user.service")
sha512sums=('3d4b599a972caab7238f405d57e8ec74f9d0f51bc2b51f6656305f3a46aecd4d1d5c10a16415c3c158df1e0248f0aad327ddefc168d480c2674cec29602a31a0'
            'c08d9f25b8c7656b72da975c2ab580adfc8834a61c2dfec8296f19b6964460d12cad2100becadb7478cbccffa7c4805dbed80847c2a30075fc9fb31dee60ebe2')
source_i686=("${pkgname}-i686-${pkgver}.gz::https://github.com/Dreamacro/clash/releases/download/premium/clash-linux-386-${pkgver}.gz")
source_x86_64=("${pkgname}-x86_64-${pkgver}.gz::https://github.com/Dreamacro/clash/releases/download/premium/clash-linux-amd64-${pkgver}.gz")
source_arm=("${pkgname}-arm-${pkgver}.gz::https://github.com/Dreamacro/clash/releases/download/premium/clash-linux-armv5-${pkgver}.gz")
source_armv6h=("${pkgname}-armv6h-${pkgver}.gz::https://github.com/Dreamacro/clash/releases/download/premium/clash-linux-armv6-${pkgver}.gz")
source_armv7h=("${pkgname}-armv7h-${pkgver}.gz::https://github.com/Dreamacro/clash/releases/download/premium/clash-linux-armv7-${pkgver}.gz")
source_aarch64=("${pkgname}-aarch64-${pkgver}.gz::https://github.com/Dreamacro/clash/releases/download/premium/clash-linux-armv8-${pkgver}.gz")

sha512sums_i686=('a49c30dcedc0bfbc41a9977fdd82574abf3750cce63feb2b14cc26e2718e075b8bd9c3bfd3bdc3707114ffdebec79cdf7ff515d49ac192fc95cb1b53b06f9e6d')
sha512sums_x86_64=('d420f0e2320867e07f735b329eb01ffbe6fe5bc779a88f8d396b8a9d1e0fedf7b14d4d69f893ae9a281bd6c376d97f187dd9eea0413ab47b4e207a65d639956f')
sha512sums_arm=('ff8ec4bd0fdfcb281fb4b4a3b6f3ddc95614b9e62eb29ebbfbcd5bec3ed92a519c208b9c074db8ff22a5f0855368a62ed241a75c571534e832212c2d2883f9e8')
sha512sums_armv6h=('b02bd5728e431f8201f8cc43cba8eed7d600b252dc4575ecf68bb0d9327d9e7e8ed15071b4e24aa63ca50e6541967a6fc10c3f9d8c1eb6adec814fc135e2af5a')
sha512sums_armv7h=('7bc55d1bb8b928ac08cf45345aaead523968e9a1f7e6fad6e0e78cb747170cd6075548a6423ee09eedbc8aacc7cfad97154344c0203154a2793aeafbf74c25d8')
sha512sums_aarch64=('da622bebe9150cb63d3030fe6fbb16c5c6744d2e0ba213efad6c241d3563d59c113d26e88e223d185c243c48d462b65ea3481989057c847ab32300cc36ccdfc5')


package() {
    cd ${srcdir}
    install -Dm755 "${pkgname}-${CARCH}-${pkgver}" "${pkgdir}/usr/bin/clash"
    install -Dm644 "clash@.service" "${pkgdir}/usr/lib/systemd/system/clash@.service"
    install -Dm644 "clash_user.service" "${pkgdir}/usr/lib/systemd/user/clash.service"
}