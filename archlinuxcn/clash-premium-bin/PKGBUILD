# Maintainer: yangon99 <yangon99_all@outlook.com>

pkgname=clash-premium-bin
pkgver=2021.03.10
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
sha512sums_i686=('ccad30d1e3c17493fb7bc7db64171dbe3533ccca5532369253211dcc7f00dc2ca371dc848bbd27c8bdaafb7514f70387528a1b3bba3da1e4b8a822f4e44215d0')
sha512sums_x86_64=('d64d96f18eb0751275af9c4819070513cb15fd9b79b34574c861f307ef4f9fdd6f889f3d4213aa33300600ed1a853b33f4d1f7abbcb84cac995f7a737e14130b')
sha512sums_arm=('b9fb69ab205fad497aa6e9345e75b6f5e3a511b7c03f43c4b8c73c352e376e6c9699a89bc91f73a0fb205ff10985e1370fb99b5ec9336af77b79423a0da0fb9a')
sha512sums_armv6h=('ba6903b71481803fd5e91500ecb57fbf7b7d83846847b318b0ca68aa943b3673a6ef9e4351bb04005a211c8dfd2c8cd40833ec6e93f4267a00e5efc5f97a44df')
sha512sums_armv7h=('6c066de8ebb11546d5155dff8444efda882d46ac43ee3a916d68b5355ff5160e20d3e1f8400852e7851b9d8de6e1fbf9cb6b798fbf7d12ddd9b6e7bf6d8b124a')
sha512sums_aarch64=('0c5876df0ff7fce750ee789a9d37e648fbede98329737ff21e5e800a26ac4e3305318c1396e0df4851a5893a456bd171a9066de5c801332f527dd2a9d243a573')
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
