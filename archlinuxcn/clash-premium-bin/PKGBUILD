# Maintainer: yangon99 <yangon99_all@outlook.com>

pkgname=clash-premium-bin
pkgver=2022.03.19
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
sha512sums_i686=('fdd65b664d351a1bd4238d3606efca3ea01a2cc57edaa6048ffe569826bd97d616e2209ea4d60c3ffa5df9cb92560e8ce77829ef5bf20fb8e05e2ac96624d619')
sha512sums_x86_64=('bce193e963d6884b59036b1fd6672bccb539d95ff8094b6a6a4a4c39ad44bfe95270fa154da9aac3c9b0d8d4b731c22f6173c7476386d005676c2295c688b161')
sha512sums_arm=('18a6b5b71f0af1d552c001cb8bd4a5709bea19f0aa0a944dd5ad8760d031a5a44d421223a4822c216c7bdebeaf0e9c363c4ac2a4c5b41db9ac9527cb5a466c7b')
sha512sums_armv6h=('635b7b676d85f43343bf36757719c9d7187e451f0b2dec0ca72586fae99a1efc2214a7117d86e2c156ae5b440539c3d4dfe13a6113e5b12bc5618d5e8bec30a1')
sha512sums_armv7h=('ba9d4dac56edaa58c8e2246895ec712d86ae24f36644e9f500f40a129615c288f93f47ed4311d4590c51b0c67beeaa657a64e137c9e612921d24b565043633af')
sha512sums_aarch64=('720564d6ac5461246e3111cbc0f2332705ac10bf4a83fd37907ef99eae6d81e427e7dceacc58d17bb6635cd937ffc286f1c9562846921cbbe042c10a28f48e2e')
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
