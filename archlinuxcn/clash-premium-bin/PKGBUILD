# Maintainer: yangon99 <yangon99_all@outlook.com>

pkgname=clash-premium-bin
pkgver=2021.04.08
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
sha512sums_i686=('919302b7859f1f19ee8416c7e3266e214bc82569399aabb4a9944c9d5d78643c98ddee6f3f96ac0b0f23b2f5edee691ba37cd29162ff158ed7dc79e7e1b5cab2')
sha512sums_x86_64=('96c36814f80cacad76107218690826012307479ad2915d96134a63e2184a6c581b711a24c083763a2dc22a7b1f0cb79e629e050e5de1a4bcee1dab5f26bbc9ca')
sha512sums_arm=('b2edf2303a1a79470bd6e0fe6ebf051bd43eb0197a282e7d54c8109199e1406fa752c44214e6de463566adeb7a20e8d9b6f8552e22941e781c0a672ddc56e7e6')
sha512sums_armv6h=('940e89d9f3089334fa730b0e03961b931abad351238d7eac46c67ddffe6bdb4b97dba0db7d2ef6153330f00a58ebbed003fc4e92f19c4039cbf96784a5a5a902')
sha512sums_armv7h=('ea652de7b26037eb8c127a4233e6f146ae861f1331ca0eeaa4b6259bca9dd64042bbd8a518e9fef1a716a07de7841efb1f9ee3adf64cc04a2bf2d2363f3d2c2e')
sha512sums_aarch64=('c6fad1ed19f2c81f6167a1b292cf967868a969961103e8af5d652b2a2ba090b58517053b3553cfc437cc7dc2119bf14208c9c5254e8658735aad2f82558a9362')
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
