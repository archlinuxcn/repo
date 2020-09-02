# Maintainer: Dct Mei <dctxmei@gmail.com>
# Co-Maintainer: xosdy <xosdy.t@gmail.com>
# Co-Maintainer: ohmyarch <ohmyarchlinux@protonmail.com>

pkgname=geph-exit
pkgver=0.22.2
pkgrel=2
pkgdesc='Runs on highly secure exit nodes, and handles exit traffic'
arch=('x86_64')
url="https://github.com/geph-official/geph2"
license=('GPL3')
groups=('geph2')
depends=('glibc')
makedepends=('go')
source=("${pkgname}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz"
        "geph-exit.sysusers"
        "geph-exit.service")
sha256sums=('dd1ccd9c5aac06b46d57b9ba7aab00b6f42b3ec8fde85d00f09e2e474e7c1dc1'
            'c07a69c9a4adcd0658dcfcad88555d87259b24ca13d35904b0b0b87b2c979a70'
            '0b74c574a28b504a02fc501e36a89d78d5179a396c8131376dabd5a6124415ec')

build() {
    cd "geph2-${pkgver}"/cmd/"${pkgname}"/
    export CGO_CPPFLAGS="${CPPFLAGS}"
    export CGO_CFLAGS="${CFLAGS}"
    export CGO_CXXFLAGS="${CXXFLAGS}"
    export CGO_LDFLAGS="${LDFLAGS}"
    export GOFLAGS="-buildmode=pie -trimpath -mod=readonly -modcacherw"
    go build
}

package() {
    install -Dm 644 "geph2-${pkgver}"/LICENSE.md "${pkgdir}"/usr/share/licenses/"${pkgname}"/LICENSE

    install -Dm 755 "geph2-${pkgver}"/cmd/"${pkgname}"/"${pkgname}" -t "${pkgdir}"/usr/bin/
    install -Dm 644 "${srcdir}"/"${pkgname}.sysusers" "${pkgdir}"/usr/lib/sysusers.d/"${pkgname}.conf"
    install -Dm 644 "${srcdir}"/"${pkgname}.service" -t "${pkgdir}"/usr/lib/systemd/system/
}
