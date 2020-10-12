# Maintainer: Dct Mei <dctxmei@gmail.com>
# Co-Maintainer: xosdy <xosdy.t@gmail.com>
# Co-Maintainer: ohmyarch <ohmyarchlinux@protonmail.com>

pkgname=geph-client
pkgver=0.22.5
pkgrel=1
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
sha256sums=('4afca74d97c890061d34c8885258d6f4a48c63e69c7e8b56719fdae68c4f306b'
            'cc30df4975a26a602eb3a1623c4a2eb3d70cb18364b6e08e86616a93df0235f4'
            'f994c3ec484adbb340089f85582c6239c58a475f3d853fd849c95d5359ecc67e'
            '1b78dc6e079aa3a9edcd94ce16609d259221b2199ce8981549b8dea7cedd3926')

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
    install -Dm 644 "${srcdir}"/"${pkgname}@.service" -t "${pkgdir}"/usr/lib/systemd/system/
}
