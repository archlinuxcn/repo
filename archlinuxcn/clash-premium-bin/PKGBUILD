# Maintainer: yangon99 <yangon99_all@outlook.com>

pkgname=clash-premium-bin
pkgver=2022.11.25
pkgrel=2
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
sha512sums_i686=('fccde034bf0b34da2bc3b511b20f808a9a029cb3387ed7ecd54b48063cf09f6c20ee4dc814877386d90ad91b4b4d2f5cab4f6fca71906237b7c3f1a7bdca3ea7')
sha512sums_x86_64=('6857db1cf94f4f9fb8c746cc28ef6212cfbd3e0b253c20a370ee77b63365de6cd77dfc2b584d5724750a087c776b25594d21a35864664eac24c61625a59b1f0c')
sha512sums_arm=('7231072a32d35af11918e6710b84e41bfc0dcebf95b5a4c715aaae31fa04d5ba64fcc5eeebffe4e4534968ac887f99d7257fdba51a7b5b5efc32d40321bc8b34')
sha512sums_armv6h=('589c06c977729e6240f3cc638ef41b099d2883e96e75ead7e514e846b76b668c9bb0485c673ce1c9c7cf97535638ccf16ec38587c86666c827ec74522ee17f49')
sha512sums_armv7h=('f1da1313edf449d9eaec0e48235945fdf105704db63099373e4601d6e008702faee2476b352da20005d59f6823dc6fe6b0c783fb3b5bd85272581100071de2ff')
sha512sums_aarch64=('f2a37721af4ebe03a26fdc5a334fdb4c226fb3a3096dce96891d137b334859ad34bca3ef3c6d67b4130cf8efa549eae7ee8de4d4f39eaf8f1e4819a3710ab564')
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
