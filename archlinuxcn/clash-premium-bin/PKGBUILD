# Maintainer: yangon99 <yangon99_all@outlook.com>

pkgname=clash-premium-bin
pkgver=2022.01.03
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
sha512sums_i686=('5e511518b5e58933e80374200f50f2b6d46f5a189231c9d074050d4441e4700f900a994d4e77d26df7b5beb335824c7ecf619553dfabfcc820fa2774b9804038')
sha512sums_x86_64=('7a7e471e707bd9e61edc07ec335dd2236c6b156e434ab6aa1d90607c643d36345f8860ce1bb6172bbc703769799e75bf60418dc276fded5d69feeb911f69c4f6')
sha512sums_arm=('9e65b363b956cd601c29ea2dc734c6bd6cedf8c9e7d12d4ec91ba2e8ef54a01120e15d7fe2d8fb5782f2c805c86c09b9210ce6edb24e6cbd99c1c6a29442f4a2')
sha512sums_armv6h=('365167341c0a665cfa10c4b4a447a603dfa1cee00c3950bd1072b667659fd3f16d3229ffdee24d6f7e7baac782914267e6b47360cbf11606f63661f75df7c3b3')
sha512sums_armv7h=('460f65f8c32297a83f4218268e2dd1bbcca56304369dcdb8730ef9edfab30c9af77b1eeaaba4528361d831e543e51fd89f864283d364aebe8609114a660c0854')
sha512sums_aarch64=('7cebddc92db7613a24b36dc12172226e7e3687b9725cfad2bb2f62f8690378b40559daa46269d53e666adc5eacb8f5d66e78351aec229cd43462b7c5fda76cb1')
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
