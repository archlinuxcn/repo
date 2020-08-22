# Maintainer: Dct Mei <dctxmei@gmail.com>
# Co-Maintainer: xosdy <xosdy.t@gmail.com>
# Co-Maintainer: ohmyarch <ohmyarchlinux@protonmail.com>

pkgname=geph-client
pkgver=0.22.2
pkgrel=4
pkgdesc='A command-line Geph client'
arch=('x86_64')
url="https://github.com/geph-official/geph2"
license=('GPL3')
groups=('geph2')
depends=('glibc')
makedepends=('go')
backup=("etc/geph2/${pkgname}.ini")
source=("${pkgname}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz"
        "geph-client.sysusers"
        "geph-client.service"
        "geph-client@.service")
md5sums=('72e7e2ef7f830d889f4a4e41114ea8af'
         'bbed6d787ce1a3effce8526980cfc9c0'
         'a21a8d9b7f58976fc535915cc78bac0c'
         'f9320a346f40b9f9da98aca263ec328d')
sha1sums=('a3ede2f10b1a621225eed7ce479e64f661f7adc9'
          '7ae4f2a4f2d175bb74d6ede2015f9d915f648712'
          '6890658fe3b898331387192feb2a22d32e921872'
          '47a9059879940d1ffb4ec045b3771df561fb96ba')
sha256sums=('dd1ccd9c5aac06b46d57b9ba7aab00b6f42b3ec8fde85d00f09e2e474e7c1dc1'
            'cc30df4975a26a602eb3a1623c4a2eb3d70cb18364b6e08e86616a93df0235f4'
            'c1e659db23ed9cdfeaa54f7c1051f7f50a48a7cdb138cbf60159d4cdd66cf11c'
            '2e5ace2b7be8bb3da72e8061a34c54e84abb35a6ab9f9b2602f2018aab8f7e53')

build() {
    cd "geph2-${pkgver}/cmd/${pkgname}/"
    export CGO_CPPFLAGS="${CPPFLAGS}"
    export CGO_CFLAGS="${CFLAGS}"
    export CGO_CXXFLAGS="${CXXFLAGS}"
    export CGO_LDFLAGS="${LDFLAGS}"
    export GOFLAGS="-buildmode=pie -trimpath -mod=readonly -modcacherw"
    go build
}

package() {
    install -Dm 644 "geph2-${pkgver}/LICENSE.md" "${pkgdir}"/usr/share/licenses/"${pkgname}"/LICENSE

    cd "geph2-${pkgver}"/cmd/"${pkgname}"/
    install -Dm 755 "${pkgname}" -t "${pkgdir}"/usr/bin/

    install -d "${pkgdir}"/etc/geph2/
    "${pkgdir}"/usr/bin/"${pkgname}" -dumpflags > "${pkgdir}"/etc/geph2/"${pkgname}.ini"

    install -Dm 644 "${srcdir}"/"${pkgname}.sysusers" "${pkgdir}"/usr/lib/sysusers.d/"${pkgname}.conf"
    install -Dm 644 "${srcdir}"/"${pkgname}.service" -t "${pkgdir}"/usr/lib/systemd/system/
    install -Dm 644 "${srcdir}"/"${pkgname}.service" -t "${pkgdir}"/usr/lib/systemd/system/
}
