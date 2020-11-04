# Maintainer: Rodrigo Bezerra <rodrigobezerra21 at gmail dot com>
# Contributor: GordonGR <ntheo1979@gmail.com>
# Contributor: josephgbr <rafael.f.f1@gmail.com>

_basename=libmms
pkgname=lib32-libmms
pkgver=0.6.4
pkgrel=2
pkgdesc="MMS stream protocol library (32 bit)"
arch=(x86_64)
url="http://sourceforge.net/projects/libmms/"
license=(LGPL)
depends=(lib32-glibc libmms)
source=(https://download.sourceforge.net/libmms/${_basename}-${pkgver}.tar.gz)
sha256sums=('3c05e05aebcbfcc044d9e8c2d4646cd8359be39a3f0ba8ce4e72a9094bee704f')

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

    rm -rf "${pkgdir}/usr/include"
}
