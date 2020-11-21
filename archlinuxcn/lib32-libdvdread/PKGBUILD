# Maintainer: Rodrigo Bezerra <rodrigobezerra21 at gmail dot com>
# Contributor: GordonGR <ntheo1979@gmail.com>
# Contributor: josephgbr <rafael.f.f1@gmail.com>

_basename=libdvdread
pkgname=lib32-libdvdread
pkgver=6.1.1
pkgrel=1
pkgdesc="Provides a simple foundation for reading DVD video disks (32 bit)"
arch=(x86_64)
url="https://www.videolan.org/developers/libdvdnav.html"
license=(GPL)
depends=(lib32-glibc libdvdread)
makedepends=(lib32-libdvdcss git)
_commit=a3329a79e9d44c927b84f0ab646a93d4c237ecb3  # tags/6.1.1^0
source=("git+https://code.videolan.org/videolan/libdvdread.git#commit=$_commit")
sha256sums=('SKIP')

pkgver() {
    cd "${_basename}"

    git describe --tags | sed -e 's/-/+/g'
}

prepare() {
    cd "${_basename}"

    autoreconf -fi
}

build() {
    cd "${_basename}"

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
    cd "${_basename}"

    make DESTDIR="${pkgdir}" install

    rm -rf "${pkgdir}/usr"/{include,share}
}
