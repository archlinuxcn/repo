# Maintainer: Rodrigo Bezerra <rodrigobezerra21 at gmail dot com>
# Contributor: GordonGR <ntheo1979@gmail.com>
# Contributor: josephgbr <rafael.f.f1@gmail.com>

_pkgname=liblrdf
pkgname=lib32-liblrdf
pkgver=0.6.1
pkgrel=3
pkgdesc="A library for the manipulation of RDF file in LADSPA plugins (32 bit)"
arch=('x86_64')
url="https://github.com/swh/LRDF"
depends=('lib32-ladspa' 'lib32-raptor' 'liblrdf')
makedepends=('gcc-multilib')
license=('GPL2')
source=("${_pkgname}-${pkgver}.tar.gz::https://github.com/swh/LRDF/archive/v${pkgver}.tar.gz")
sha512sums=('7732813eec704aef984d056de254e4fa049fdd0a7444b6a88f75f012afe9c587cbd1295f027c77361fa42bc097cdce9d9cabdba6b86e99a3c14805d84258df1c')

prepare() {
    mv -v "LRDF-${pkgver}" "${_pkgname}-${pkgver}"
    cd "${_pkgname}-${pkgver}"
    autoreconf -vfi
    sed -e 's,raptor.h,raptor2/raptor.h,' -i lrdf.h
}

build() {
    cd "${_pkgname}-${pkgver}"

    export CC='gcc -m32'
    export CXX='g++ -m32'
    export PKG_CONFIG_PATH='/usr/lib32/pkgconfig'

    # raptor.h changed location
    export CXXFLAGS="$(pkg-config --cflags raptor2) ${CXXFLAGS}"

    ./configure \
        --build=i686-pc-linux-gnu \
        --prefix=/usr \
        --libdir=/usr/lib32
    make
}

package() {
    cd "${_pkgname}-${pkgver}"

    make DESTDIR="${pkgdir}" install

    rm -rf "${pkgdir}"/usr/{include,share}
}
