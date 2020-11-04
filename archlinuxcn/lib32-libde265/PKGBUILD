# Maintainer: Rodrigo Bezerra <rodrigobezerra21 at gmail dot com>

_basename=libde265
pkgname=lib32-libde265
pkgver=1.0.3
pkgrel=1
pkgdesc="Open h.265 video codec implementation  (32-bit)"
arch=(x86_64)
url="https://github.com/strukturag/libde265"
license=(LGPL3)
depends=(lib32-gcc-libs libde265)
source=(https://github.com/strukturag/libde265/releases/download/v$pkgver/$_basename-$pkgver.tar.gz)
sha256sums=('e4206185a7c67d3b797d6537df8dcaa6e5fd5a5f93bd14e65a755c33cd645f7a')

build() {
    cd $_basename-$pkgver

    export CC='gcc -m32'
    export CXX='g++ -m32'
    export PKG_CONFIG_PATH='/usr/lib32/pkgconfig'

    ./configure \
        --build=i686-pc-linux-gnu \
        --prefix=/usr \
        --libdir=/usr/lib32 \
        --enable-static=no \
        --disable-dec265 \
        --disable-sherlock265

    make
}

package() {
    cd $_basename-$pkgver

    make DESTDIR="$pkgdir" install

    cd "$pkgdir/usr"

    rm -r bin include
}
