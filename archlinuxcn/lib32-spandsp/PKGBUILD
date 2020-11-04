# Maintainer: Rodrigo Bezerra <rodrigobezerra21 at gmail dot com>
# Contributor: GordonGR <ntheo1979@gmail.com>
# Contributor: josephgbr <rafael.f.f1@gmail.com>
# Contributor: quequotion <quequotion@gmail.com>

_basename=spandsp
pkgname=lib32-spandsp
pkgver=0.0.6
pkgrel=4
pkgdesc="A DSP library for telephony (32 bit)"
arch=(x86_64)
license=(GPL)
url="http://www.soft-switch.org/"
depends=(lib32-libtiff spandsp)
source=("https://src.fedoraproject.org/lookaside/pkgs/${_basename}/${_basename}-${pkgver}.tar.gz/897d839516a6d4edb20397d4757a7ca3/${_basename}-${pkgver}.tar.gz")
sha512sums=('16bb215ca89a39282e832403f69bc4c98ad3fe35ab3a6eb4731ee5029a6acd9b2df243c3701de845441cbdc16c88b3cd398ef15dc3502e45d5aeca8a161917d4')

build() {
    cd "${_basename}-${pkgver}"

    export CC='gcc -m32'
    export CXX='g++ -m32'
    export PKG_CONFIG_PATH='/usr/lib32/pkgconfig'
#     export LDFLAGS='-m32'

    ./configure \
        --build=i686-pc-linux-gnu \
        --prefix=/usr \
        --libdir=/usr/lib32

    make
}

package() {
    cd "${_basename}-${pkgver}"

    make DESTDIR="${pkgdir}" install

    rm -rf "${pkgdir}/usr/include"
}

