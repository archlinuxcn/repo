# Maintainer: yangon99 <yangon99_all@outlook.com>

pkgname=clash-premium-bin
pkgver=2022.05.17
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
sha512sums_i686=('165344ac940fcdf0580114aec5adacc308e72598909cc06c16c3e670014595d405cfc1acae07c6bd32767bf060ff4c714dd9e5d26a4a24b1bc84a28f3a82cab4')
sha512sums_x86_64=('7f7711658205ee0da8d4dc1e77d93a0fcbb16c4059d29b9e4345131e535d35190c1486398be40f930ca39e48fa93497788e3e041acef77f2cde6990e3d25f071')
sha512sums_arm=('52b31a80ef9c22435dbcbec77674fd0c51c16153be036f2c82e82caecbeda3e914bcae5934b26b56e07af5e1e56405137b590c1f46c3589ff7287c41d9ea3dc3')
sha512sums_armv6h=('81de6877e222866bae1da152cee3ec7987f0c2dffe9737a9795d357f6087467771bcd955297339a859e31755d4ddfb43383fa3f98974700db63b1bbdc38dd562')
sha512sums_armv7h=('748d997137eb9a13d30d76cd01cc76df270338008a906d2309ec0f11e6eeffa818ebcec9960c1ca37b233dd70d66f516edf97275d9c4557319f978e9bb19238c')
sha512sums_aarch64=('578e7adefeb7fddba15202828a957453cceefa86bb9007d7f3fae4724e091a15c916dc5e07e8ba4fc477aeb792842acd766972042210c4f59724fe5cd6add2cf')
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
