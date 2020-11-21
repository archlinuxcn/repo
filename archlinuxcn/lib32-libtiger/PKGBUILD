# Maintainer: Rodrigo Bezerra <rodrigobezerra21 at gmail dot com>
# Contributor: orumin <dev@orum.in>

_basename=libtiger
pkgname=lib32-libtiger
pkgver=0.3.4
pkgrel=4
pkgdesc="A rendering library for Kate streams using Pango and Cairo (32-bit)"
url="https://code.google.com/archive/p/libtiger/"
license=('LGPL')
arch=('x86_64')
depends=('lib32-pango' 'lib32-libkate' 'libtiger')
makedepends=('pkg-config')
source=(https://download.videolan.org/contrib/tiger/$_basename-$pkgver.tar.gz)
md5sums=('dc1dbeb658c95485ba10b9b2897b4ae2')

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
        --disable-doc

    make
}

package() {
    cd $_basename-$pkgver

    make DESTDIR="${pkgdir}" install

    cd "$pkgdir"/usr

    rm -r include
}
