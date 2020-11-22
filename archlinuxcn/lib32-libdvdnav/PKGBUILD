# Maintainer: Rodrigo Bezerra <rodrigobezerra21 at gmail dot com>
# Contributor: GordonGR <ntheo1979@gmail.com>
# Contributor: josephgbr <rafael.f.f1@gmail.com>

_basename=libdvdnav
pkgname=lib32-libdvdnav
pkgver=6.1.0
pkgrel=1
pkgdesc="The library for xine-dvdnav plugin (32 bit)"
arch=(x86_64)
license=(GPL)
url="https://www.videolan.org/developers/libdvdnav.html"
depends=(lib32-libdvdread libdvdnav)
source=("https://download.videolan.org/pub/videolan/libdvdnav/${pkgver}/libdvdnav-${pkgver}.tar.bz2"{,.asc})
sha256sums=('f697b15ea9f75e9f36bdf6ec3726308169f154e2b1e99865d0bbe823720cee5b'
            'SKIP')
validpgpkeys=('65F7C6B4206BD057A7EB73787180713BE58D1ADC') # VideoLAN Release Signing Key

build() {
    cd "${_basename}-${pkgver}"

    export CC='gcc -m32'
    export CXX='g++ -m32'
    export PKG_CONFIG_PATH='/usr/lib32/pkgconfig'

    ./configure \
        --build=i686-pc-linux-gnu \
        --prefix=/usr \
        --libdir=/usr/lib32

    make
}

package() {
    cd "${_basename}-${pkgver}"

    make DESTDIR="${pkgdir}" install

    rm -rf "${pkgdir}/usr"/{include,share}
}

