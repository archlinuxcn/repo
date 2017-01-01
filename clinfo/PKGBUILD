# Maintainer: Zanny <lordzanny@gmail.com>
# Contributor: Ivan Shapovalov <intelfx@intelfx.name>

pkgname=clinfo
pkgver=2.1.16.01.12
pkgrel=2
pkgdesc="Print all known information about all available OpenCL platforms and devices in the system"
arch=(i686 x86_64)
url="https://github.com/Oblomov/clinfo"
license=('custom:Public Domain')
depends=(opencl-icd-loader)
makedepends=(opencl-headers)
provides=(clinfo)
conflicts=(clinfo)
replaces=(clinfo)
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/Oblomov/clinfo/archive/${pkgver}.tar.gz")
md5sums=('SKIP')

build() {
    cd ${pkgname}-${pkgver}
    make
}

package() {
    cd ${pkgname}-${pkgver}
    install -D -m755 clinfo "${pkgdir}/usr/bin/clinfo"
    install -D -m644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
    install -D -m644 man/clinfo.1 "${pkgdir}/usr/share/man/man1/clinfo.1"
}
