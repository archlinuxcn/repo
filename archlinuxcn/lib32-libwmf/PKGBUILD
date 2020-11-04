# Maintainer: Rodrigo Bezerra <rodrigobezerra21 at gmail dot com>
# Contributor: orumin <dev at orum.in>

_basename=libwmf
pkgname=lib32-libwmf
pkgver=0.2.12
pkgrel=2
pkgdesc="A library for reading vector images in Microsoft's native Windows Metafile Format (WMF) (32-bit)"
arch=('x86_64')
url="http://wvware.sourceforge.net/libwmf.html"
license=('LGPL')
depends=('lib32-expat' 'lib32-freetype2' 'lib32-gdk-pixbuf2' 'libwmf')
makedepends=('lib32-gtk2' 'lib32-libxt')
options=('!docs' '!emptydirs')
source=($_basename-$pkgver.tar.gz::https://github.com/caolanm/libwmf/archive/v$pkgver.tar.gz
        libwmf-freetype.patch)
sha1sums=('490a26175ad667fbc0c009d390bf56644919bed6'
          'ef4d452cd5e7fcb36751771c6f44b4b7a3f8693a')

prepare() {
    cd ${_basename}-${pkgver}

    patch -p1 -i ../libwmf-freetype.patch # Port away from freetype-config, patch from openembedded.org

    autoreconf -vif -Ipatches
}

build() {
    cd ${_basename}-${pkgver}

    export CC='gcc -m32'
    export CXX='g++ -m32'
    export PKG_CONFIG_PATH='/usr/lib32/pkgconfig'
    export FREETYPE_CONFIG='/usr/bin/i686-pc-linux-gnu-pkg-config freetype2'

    ./configure \
        --build=i686-pc-linux-gnu \
        --prefix=/usr \
        --libdir=/usr/lib32 \
        --with-gsfontdir=/usr/share/fonts/Type1 \
        --with-fontdir=/usr/share/fonts/Type1 \
        --with-gsfontmap=/usr/share/ghostscript/9.10/Resource/Init/Fontmap.GS

    make
}

package() {
    cd ${_basename}-${pkgver}

    make DESTDIR="${pkgdir}" install -j1

    rm -r "${pkgdir}/usr/bin"
    rm -r "${pkgdir}/usr/include"

    #Remove fonts, these are in gsfonts
    rm -rf "${pkgdir}/usr/share"
}
