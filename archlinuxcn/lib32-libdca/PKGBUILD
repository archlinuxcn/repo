# Maintainer: Rodrigo Bezerra <rodrigobezerra21 at gmail dot com>
# Contributor: GordonGR <ntheo1979@gmail.com>
# Contributor: josephgbr <rafael.f.f1@gmail.com>

_basename=libdca
pkgname=lib32-libdca
pkgver=0.0.7
pkgrel=1
pkgdesc="Free library for decoding DTS Coherent Acoustics streams (32 bit)"
arch=(x86_64)
license=(GPL)
url="http://www.videolan.org/developers/libdca.html"
depends=(lib32-glibc libdca)
options=('!emptydirs')
source=("https://download.videolan.org/pub/videolan/${_basename}/${pkgver}/${_basename}-${pkgver}.tar.bz2")
sha512sums=('dae15d77d066687c882833d5bed8d65a585c1fc0277b7276563c89ddd5a83b35389ec94cca445f38af28a9b01430b72647e9afd1b08f030959e711de1a08924a')

prepare() {
    cd ${_basename}-${pkgver}

    ./bootstrap
}

build() {
    cd ${_basename}-${pkgver}

    export CC='gcc -m32'
    export CXX='g++ -m32'
    export PKG_CONFIG_PATH='/usr/lib32/pkgconfig'

    ./configure \
        --build=i686-pc-linux-gnu \
        --prefix=/usr \
        --libdir=/usr/lib32 \
        --disable-static

    make
}

package() {
    cd ${_basename}-${pkgver}

    make DESTDIR="${pkgdir}" install

    rm -rf "${pkgdir}/usr"/{bin,include,share}
    rm "${pkgdir}/usr/lib32/libdts.a"
}
