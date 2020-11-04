# Maintainer: Rodrigo Bezerra <rodrigobezerra21 at gmail dot com>
# Contributor: GordonGR <gordongr@freemail.gr>
# Contributor: Sarah Hay <sarah@archlinux.org>
# Contributor: Andreas Radke <andyrtr@archlinux.org>

_basename=libmpeg2
pkgname=lib32-libmpeg2
pkgver=0.5.1
pkgrel=4
pkgdesc="Library for decoding MPEG-1 and MPEG-2 video streams (32 bit)"
arch=(x86_64)
url="http://libmpeg2.sourceforge.net/"
license=('GPL2')
depends=(lib32-glibc libmpeg2)
makedepends=(lib32-sdl lib32-libxv)
source=(http://libmpeg2.sourceforge.net/files/${_basename}-${pkgver}.tar.gz
        libmpeg2-0.5.1-gcc4.6.patch)
sha256sums=('dee22e893cb5fc2b2b6ebd60b88478ab8556cb3b93f9a0d7ce8f3b61851871d4'
            '763e188eea36ee3cdfb31e7877bbead00676b5766c25175ec6a7eb20884926d1')

prepare() {
    cd "${_basename}-${pkgver}"

    patch -Np1 -i "${srcdir}/libmpeg2-0.5.1-gcc4.6.patch"

    sed '/AC_PATH_XTRA/d' -i configure.ac

    autoreconf --force --install
}

build(){
    cd "${_basename}-${pkgver}"

    export CC='gcc -m32'
    export CXX='g++ -m32'
    export PKG_CONFIG_PATH='/usr/lib32/pkgconfig'

    ./configure \
        --build=i686-pc-linux-gnu \
        --prefix=/usr \
        --libdir=/usr/lib32 \
        --enable-shared \
        --disable-static

    make OPT_CFLAGS="${CFLAGS}" \
         MPEG2DEC_CFLAGS="${CFLAGS}" \
         LIBMPEG2_CFLAGS=""
}

package() {
    cd "${_basename}-${pkgver}"

    make DESTDIR="${pkgdir}" install

    rm -rf "${pkgdir}/usr"/{bin,include,share}
}
