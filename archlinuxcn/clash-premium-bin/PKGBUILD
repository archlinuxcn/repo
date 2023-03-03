# Maintainer: yangon99 <yangon99_all@outlook.com>

pkgname=clash-premium-bin
pkgver=2023.03.03
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
sha512sums_i686=('d45b6dff30182079bfc5a0531d49440d9e80200ac34068f332abc5692bbd8dd6a3633966587e1427005b36349d52cd5cbdc1b8a4d9a2391cc248e3eef1098dfd')
sha512sums_x86_64=('bd928b49ec0f20cbcd8dac7769386847ec6683999e22571c3138ef67ab6e099b4b513d56bbf61212d185b6361c8b59c6c09765c62d12af7250eb23b12929897e')
sha512sums_arm=('7112a3140f63381df90e341b9c92d6e97ace5345883b3040b2aef764af91f6961ce626111ac0d3d90294e844716edbc6de9abd6dbd439745c3ddfb396b543d0c')
sha512sums_armv6h=('a571f3e51fa22c6cd74db4aeb40b372fc50f315328af02a4713e4279493a120836d7f9b5d72edeefb5f8a3a1b28e19c50873230fe0efa05c778c70ff2558f782')
sha512sums_armv7h=('7f29e5076b472581ff8b3257fe3b7df14544c3792040f3d7dd4f1e9ff58e67ee66ea1a9fc807d34720b3ac8f24f5453444e1b814a6321a8e4dd43badf9d59387')
sha512sums_aarch64=('0a375878eb458663e20c8556a90d5b189fead494d5522fd4da6153510ff71a79559a1acf8f1cc7f4068ee2fcd5218951bfe0b94904a8bfcb45722f93908b7c0f')
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
