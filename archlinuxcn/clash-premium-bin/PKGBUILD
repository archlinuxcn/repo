# Maintainer: yangon99 <yangon99_all@outlook.com>

pkgname=clash-premium-bin
pkgver=2022.01.02
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
sha512sums_i686=('83e885159b334517985c3b839b6672333ab0b2006cf18cb00876bdf94cc15ca83554db15970629aac68f8c210961914c8f5b2a3762ceeef033753835d6036d7f')
sha512sums_x86_64=('e81e961a11baa6a3a2bfe71bd52667b86d5e85833100c6f25ac3f36321bdda235e457735380dedb12ced580968a5c2a2394ebd512c208495c738674880ddcadd')
sha512sums_arm=('956248ce67f6071def37015881ce002684691ca7eae22c572b8f34a4e488f595ff4eba5c4ad048ba7ef8e31e7c02f77a153220800ec521d9c5cf6e2cf5645a29')
sha512sums_armv6h=('04def0e7e19bae0fe3e8711e0257d9c2992a879300e19a0961120acba9969ba4e21d42377031d807cd15c5490b3dbc374695e778356101c4d6dde2c70f27596f')
sha512sums_armv7h=('ff2186876f987448476ec388631fe57d240f243fbf76b01adab0d4f0adad17ceeff41060cfd2cd4d136ff41cc20c0ef8916f2b6825cf3aad17b965b09dab4e8b')
sha512sums_aarch64=('4d8f3a8e3e44ca3eaa171caaf77c2175a3f40d48a5ee28841ac5f76ea9b36a43bc06da39c1c0bc13f664fc6eac3408c57f0d89536519a9524f95082836dce99c')
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
