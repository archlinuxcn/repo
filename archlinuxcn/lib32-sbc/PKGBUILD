# Maintainer: Rodrigo Bezerra <rodrigobezerra21 at gmail dot com>
# Contributor: orumin <dev@orum.in>

_basename=sbc
pkgname="lib32-$_basename"
pkgver=1.4
pkgrel=1
pkgdesc="Bluetooth Subband Codec (SBC) library (32-bit)"
arch=('x86_64')
url="http://www.bluez.org/"
license=('GPL' 'LGPL')
depends=('lib32-glibc' 'sbc')
source=(https://mirrors.edge.kernel.org/pub/linux/bluetooth/$_basename-$pkgver.tar.xz)
sha512sums=('f35250c202034e93ce4046d29883d76b162164d42fb59e6af8ff5e57f197244238f5f8087309cef2d44755c179e7f0869cf096735c8de510b1ac7e0f6c29d84f')


build() {
    cd $_basename-$pkgver

    export CC='gcc -m32'
    export CXX='g++ -m32'
    export PKG_CONFIG_PATH='/usr/lib32/pkgconfig'

    ./configure --prefix=/usr \
        --build=i686-pc-linux-gnu \
        --libdir=/usr/lib32 \
        --disable-static \
        --disable-tester

    make
}

package() {
    cd $_basename-$pkgver

    make DESTDIR="$pkgdir" install

    cd "$pkgdir"/usr

    rm -r bin include
}
