# Maintainer: Dct Mei <dctxmei@gmail.com>
# Co-Maintainer: xosdy <xosdy.t@gmail.com>
# Co-Maintainer: ohmyarch <ohmyarchlinux@protonmail.com>

pkgname=geph-bridge
pkgver=0.22.2
pkgrel=1
pkgdesc='Runs on bridge nodes, which relay client-to-exit encrypted traffic across harsh firewalls'
arch=('x86_64')
url="https://github.com/geph-official/geph2"
license=('GPL3')
groups=('geph2')
depends=('glibc')
makedepends=('go')
source=("${pkgname}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz")
sha256sums=('dd1ccd9c5aac06b46d57b9ba7aab00b6f42b3ec8fde85d00f09e2e474e7c1dc1')

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
}
