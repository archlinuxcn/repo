# Maintainer: Rodrigo Bezerra <rodrigobezerra21 at gmail dot com>
# Contributor: josephgbr <rafael.f.f1@gmail.com>
# Contributor: GordonGR <ntheo1979@gmail.com>

pkgname=lib32-raptor
pkgver=2.0.15
pkgrel=8
pkgdesc="A C library that parses RDF/XML/N-Triples into RDF triples (32 bit)"
arch=('x86_64')
url="http://librdf.org/raptor"
depends=('lib32-curl' 'lib32-icu' 'lib32-libxslt' 'raptor')
makedepends=('gcc-multilib')
license=('LGPL')
source=("http://librdf.org/dist/source/raptor2-${pkgver}.tar.gz")
sha256sums=('ada7f0ba54787b33485d090d3d2680533520cd4426d2f7fb4782dd4a6a1480ed')

build() {
    cd "raptor2-${pkgver}"

    export CC='gcc -m32'
    export CXX='g++ -m32'
    export PKG_CONFIG_PATH='/usr/lib32/pkgconfig'

    ./configure \
        --build=i686-pc-linux-gnu \
        --prefix=/usr \
        --libdir=/usr/lib32 \
        --disable-static \
        --with-yajl=no \
        --with-icu-config=/usr/bin/icu-config-32

    make
}

package() {
    cd "raptor2-${pkgver}"

    make prefix="${pkgdir}"/usr libdir="${pkgdir}"/usr/lib32 install

    rm -rf "${pkgdir}"/usr/{bin,include,share}
}
