# Maintainer: yangon99 <yangon99_all@outlook.com>

pkgname=clash-premium-bin
pkgver=2023.04.16
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
sha512sums_i686=('87384fc4d896ff8775c61afccb539d006e09454aae8c556cef95ee3851e7bd07b6da63e37479f4f90e49cd31bf244fdf05d026a703a4a3e4b9e52ec2bf45d96a')
sha512sums_x86_64=('f9f4672fbe4c075e1d5583303ea6d7ad75f2a479f474dca502512dd81d37c5f90c9cc48d11863089920298a77b08ba129c083393fddadbba00367e88f314b11c')
sha512sums_arm=('eeb81a6741f2b026a996b7f85e2f0f1db4c221be811ae9a5ddbd8e55e131cd8c114fbd71ab6ce97d06d25c587736078d027b78803fd9d22fac19b9b7e2dd75df')
sha512sums_armv6h=('d3742b743d1950c26c3d92aa1a335dc85a22d7dd3ad35a53d590a045b363f9b18defb3396e22af8ccc9695308abe82d2a9d0845948a2a286c2a34905a24380ce')
sha512sums_armv7h=('f8e1542abd81e6931050b2d17b82f8197bf70c0d1f5e167b7a4019339ff218902aed37760be2503a19a907f616d8c7fce855d6255114a76e50784827666eca8e')
sha512sums_aarch64=('ff4f1ad72f356f25edc53be91fa5857224e77ad5eee2dd0c5698416332cd9e9946d2206ffc4753f2199138d934e478aba5a270c256d2557335c8aea76407028b')
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
