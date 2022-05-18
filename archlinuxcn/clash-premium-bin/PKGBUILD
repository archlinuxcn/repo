# Maintainer: yangon99 <yangon99_all@outlook.com>

pkgname=clash-premium-bin
pkgver=2022.05.18
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
sha512sums_i686=('80e4529dfb6ddb927ed029233e4520bf647b9bea4cd8fcf256f7344b8778cbfb0a88122229c3d8572fd539178dc46b70c359bae6c90c1d3b98538c74dfed8ddf')
sha512sums_x86_64=('179db58603917d849fb10f66dc820a30d0e9db678289f057a640566dfc254e99228fdc36172ad38b1080a9c5176b76a2b2245fc211ef9f2c31529a7410ca2b9d')
sha512sums_arm=('afa8ccc03685ae1a29a4c06456b7f4a3f5459cecf739a2dd95df61e3c8937b86b66c3fbc56472cef46aa454721654389a60aabe820437b3d68a5c85ec6e3adb9')
sha512sums_armv6h=('be0acea75d440fcce485e99b1faede541bb77165ce04c0f9d1726647d415d0df6ce218f7f312ef92a6438016524bfe5d694c20feeeb490c1819ea40a8ce27eb4')
sha512sums_armv7h=('358134c6622d548c42b2632eed9075c35783ea9ef449b0ab16e3e5fe05a4b1e16e84d5e69af2f3a0d00d8ee5c79b4cbc667364c1ace0479eec2da2239c038460')
sha512sums_aarch64=('1677ba93479bf464358d44ae0e48b42f4631d8f53ff89b5e8dde75f3e123ae66d0ab9e6b82171d58f1a456d3d2f52fb7a509110b9afeb14da33e9f262394a8dd')
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
