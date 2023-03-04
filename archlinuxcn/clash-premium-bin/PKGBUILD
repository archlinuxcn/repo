# Maintainer: yangon99 <yangon99_all@outlook.com>

pkgname=clash-premium-bin
pkgver=2023.03.04
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
sha512sums_i686=('47a93c0c52ab769ec60799c15a2f1dc40c1d614c592acc7bc8c1b71a26bb968d43a3c442374f2f0232f5686560742358476e7b69de203c0ed1c717370d44ea85')
sha512sums_x86_64=('f01f6c62a5513ae37b9aed218d1beca82499bb2a29f83ccdf52f73e6e9376e1f44f2c04c6c9ae30e83a3d7b62a18dcd302510385e8ccf5a5a12a9f62113ac5cb')
sha512sums_arm=('44222dce4ba873a6fb8479794497c46ee8ae9d8af4ff7b41f84653b16fdfca8320f44451ed79acb476364d4d882e037998169bcbbe09bdd252cb3654de52a59e')
sha512sums_armv6h=('d8d7263203bda36077e27cd61ad06f25c3c0534faccecde191e0c777078e2de29e6f24eafdf73b8a64d9314f3850cb877802b98f27d093dbc28d0876b7be7fbc')
sha512sums_armv7h=('dde951aa08ff0077585945e6b8e5c2abd104027a7960d49707c0ffb1c6205a7bffe8352c6be7fc2aafe180121afa825b41a24671e5d812a7039c69af8947c5e4')
sha512sums_aarch64=('3f67843ef43d293bd4de92f7a57b6c4b44f7aba85c17b3f9b1095d7914e2b26b41d1d5b6c75cc195f3b137ecfdc6a1f03585fabf64e306a9ba23a038eac10dc1')
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
