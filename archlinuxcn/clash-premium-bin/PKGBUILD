# Maintainer: yangon99 <yangon99_all@outlook.com>

pkgname=clash-premium-bin
pkgver=2023.07.22
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
sha512sums_i686=('fa6c11f49dd8e26a1bc16e9b1e8907403f30efd05babe1bbb3c6c1f3542e52eeea56e2ac18951bfce70ef2d69028b1bfe9e9b978d47a7c7e0757cefab3dbba6d')
sha512sums_x86_64=('3a5043b1a8dd11c5f43e2a4212b9a3b521b2f55cd15b856c41524ab2059833175a491d19ae30fa8488086fe26b923bbbc5c8dfeac37e50ca7504e80d89cb109d')
sha512sums_arm=('53464307755fc0efd67fcff2f41422a832630052f9dd991a787713e146540b987fd8026e0ef0019e1074aa79b053b495da2638577f20965dcc6416bfe4c37d66')
sha512sums_armv6h=('6017c49fc99d6b53af42975a647da7f9607874d8b08a05699b62bd3c2f7a68a52acffdbec25f2488a948df988c2488debe757623f88fbbd8dd35cda797b22b7f')
sha512sums_armv7h=('24a9e74e972f098a1aa96fdd80d627b023a975c06a050aa00d4a5c1d2bdd17e824ba954e212e9803298f9b0ddeefcdeca3a4590ad930169b492de9040345e69c')
sha512sums_aarch64=('7090071fd46555ea4ffeed2cd01ad2101614200ed19c85d6f0d1ae07a94456cae7d7967e801b11758e70eba08880a7a45a52d17400a3452f3a6a280069cf12e6')
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
