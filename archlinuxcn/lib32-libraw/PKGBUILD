# Maintainer: Rodrigo Bezerra <rodrigobezerra21 at gmail dot com>
# Contributor: orumin <dev at orum.in>

_basename=libraw
pkgname=lib32-libraw
pkgver=0.20.0
pkgrel=1
pkgdesc="A library for reading RAW files obtained from digital photo cameras (CRW/CR2, NEF, RAF, DNG, and others) (32-bit)"
arch=('x86_64')
url="https://www.libraw.org/"
license=(CDDL LGPL)
depends=(lib32-lcms2 lib32-jasper libraw)
source=("https://www.libraw.org/data/LibRaw-$pkgver.tar.gz")
sha256sums=('1f0a383da2ce9f409087facd28261decbf6be72cc90c78cd003b0766e4d694a3')

build() {
    cd LibRaw-$pkgver

    export CC='gcc -m32'
    export CXX='g++ -m32'
    export PKG_CONFIG_PATH='/usr/lib32/pkgconfig'

    ./configure \
        --build=i686-pc-linux-gnu \
        --prefix=/usr \
        --libdir=/usr/lib32 \
        --disable-examples

    make
}

package() {
    cd LibRaw-$pkgver

    make DESTDIR="$pkgdir" install

    rm -rf "${pkgdir}/usr/include"
    rm -rf "${pkgdir}/usr/share"
}
