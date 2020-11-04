# Maintainer: Rodrigo Bezerra <rodrigobezerra21 at gmail dot com>
# Contributor: MArkus Kitsinger <root@swooshalicio.us>
# Contributor: Maxime Gauduin <alucryd@archlinux.org>
# Contributor: PelPix <kylebloss@pelpix.info>
# Contributor: DrZaius <lou[at]fakeoutdoorsman[dot]com>

pkgname=lib32-libfdk-aac
pkgver=2.0.1
pkgrel=1
pkgdesc='Fraunhofer FDK AAC codec library (32-bit)'
arch=(x86_64)
url=https://sourceforge.net/projects/opencore-amr/
license=(custom)
depends=(lib32-glibc libfdk-aac)
makedepends=(git)
source=(git+https://github.com/mstorsjo/fdk-aac.git#tag=d387d3b6ed79ff9a82c60440bdd86e6e5e324bec)
sha256sums=(SKIP)

pkgver() {
    cd fdk-aac

    git describe --tags | sed 's/^v//'
}

prepare() {
    cd fdk-aac

    ./autogen.sh
}

build() {
    cd fdk-aac

    export CC='gcc -m32'
    export CXX='g++ -m32'
    export PKG_CONFIG_PATH='/usr/lib32/pkgconfig'

    ./configure --prefix=/usr \
        --build=i686-pc-linux-gnu \
        --libdir=/usr/lib32 \
        --disable-static

    make
}

package () {
    cd fdk-aac

    make DESTDIR="${pkgdir}" install
    install -Dm 644 NOTICE -t "${pkgdir}/usr/share/licenses/${pkgname}/"

    rm -rf "${pkgdir}/usr/include"
}
