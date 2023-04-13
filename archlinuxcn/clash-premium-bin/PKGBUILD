# Maintainer: yangon99 <yangon99_all@outlook.com>

pkgname=clash-premium-bin
pkgver=2023.04.13
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
sha512sums_i686=('a9315f112cf34ae44ad14dc46a92a65cafdb81c34da5bf3c56161f994b5d42817b93692ddc1742bb1bcdf23b4330815edfc77945c261d0d96ca2646103717d23')
sha512sums_x86_64=('b178b5dde9f14ae987ce263a054e8b2e85a005422d0a881b6b7fd529dfa3adbb7335e9c9b1bc532dd01e0f88f7c5970b76aefab50d58566ecfa2ad9d1f3da26b')
sha512sums_arm=('d79edd592946bb960f84b3d581817cc435bd47c5dc384135d6dd789a1ba1941735703f16797693be98696a8b51c79130342709886e73d561db23d0d25e33e85f')
sha512sums_armv6h=('40dbfdb864e30fc63d06b63edae0a95bc5fbec3a48b80d834c2bfe3706a31f056a8f90dca242c15cc834a0719781f0e396bd90b126b358e2768a45aa9e17bceb')
sha512sums_armv7h=('e5c5488c0248f9f753833564e42c8847280a9b240cc269151abaf2876190f8eab814a0bfcea199051715cf1fb06d299d478640aa0e18bc40d1282e271eb67459')
sha512sums_aarch64=('8227b858abf3cfdd951dae8b1014bd88318d13425fe90b1ee516117f805232258357162f357276aec038dd73a9d1e6a6aa3bb30cbe50de06fea46afa61696215')
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
