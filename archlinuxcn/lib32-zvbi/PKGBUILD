# Maintainer: Rodrigo Bezerra <rodrigobezerra21 at gmail dot com>
# Contributor: orumin <dev at orum.in>

pkgname=lib32-zvbi
_basename=zvbi
pkgver=0.2.35
pkgrel=3
pkgdesc="VBI capture and decoding library  (32-bit)"
url="http://zapping.sourceforge.net/cgi-bin/view/ZVBI/WebHome"
arch=('x86_64')
depends=('lib32-libpng' 'zvbi')
makedepends=('lib32-libx11')
license=('GPL')
source=(http://downloads.sourceforge.net/sourceforge/zapping/${_basename}-${pkgver}.tar.bz2)
sha256sums=('fc883c34111a487c4a783f91b1b2bb5610d8d8e58dcba80c7ab31e67e4765318')

build() {
    cd "${_basename}-${pkgver}"

    export CC='gcc -m32'
    export CXX='g++ -m32'
    export PKG_CONFIG_PATH='/usr/lib32/pkgconfig'


    ./configure --prefix=/usr \
        --build=i686-pc-linux-gnu \
        --sbindir=/usr/bin \
        --libdir=/usr/lib32

    make
}

package() {
    cd "${_basename}-${pkgver}"

    make DESTDIR="${pkgdir}" install

    rm -r "${pkgdir}/usr/bin"
    rm -r "${pkgdir}/usr/include"
    rm -r "${pkgdir}/usr/share"
}
