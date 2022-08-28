# Maintainer: yangon99 <yangon99_all@outlook.com>

pkgname=clash-premium-bin
pkgver=2022.08.26
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
sha512sums_i686=('fe77d242eb1937f6ea218981393a74d79e8060f6a29a89e9bb130e9b48750b6460ad47791c44ab648fe604c7dd4763e21f9da2e6e3724e7f0dded36ddcea1a30')
sha512sums_x86_64=('006fedfc30afee84f71f8216be917cb5feef18b89d04b4275a58e33bb6f52e4516d8209ad4de373ac6abef418cb6000515b2bf56512ac5bf7ba411be2c87863d')
sha512sums_arm=('4259641a10496c8696f8a6033aeafbb0835e7a0b6a56fbf96d06dfb2e7e54fa3d74b0ff71fe2187fe746156c216b222baadc41ec457116cb8d734d4fbaa1fbde')
sha512sums_armv6h=('8f7e6cbf8096f4a879df77d9f60a6b2b31559b324cfe7121d0062e90fb1ef584dcd0588e112245874e75b85d13db42040635e4bb5e3f3d13852203554ca0180d')
sha512sums_armv7h=('e16f733afe9304537df396343ea999f9eabbda2a199b68c48c78e5e57c35db8bc99bd341b883552dd60a7ab606dc92457a11745a9b17df4f949fe03e911ab1ee')
sha512sums_aarch64=('5357c54e43fe2ac834ffa2a846fed85cd159e543da616a521243fa33a249fe030bf148bdd2d62a869422aff4e9814b239a2eb590d9c67daa9ee124b97470f7c6')
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
