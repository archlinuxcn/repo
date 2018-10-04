# Maintainer : Daniel Bermond < yahoo-com: danielbermond >
# Contributor: James An <james@jamesan.ca>
# Contributor: Mariusz Libera <mariusz.libera@gmail.com>
# Contributor: mortdeus <mortdeus@gocos2d.org>
# Contributor: Sergej Pupykin <pupykin.s+arch@gmail.com>
# Contributor: tobias <tobias@archlinux.org>
# Contributor: Simon Rutishauser <simon.rutishauser@gmx.ch>

pkgname=htmldoc
pkgver=1.9.4
pkgrel=1
pkgdesc='HTML Conversion Software'
arch=('i686' 'x86_64')
url='http://www.msweet.org/htmldoc/index.html'
license=('GPL2')
depends=('libxpm' 'gnutls' 'fltk')
conflicts=('htmldoc-git')
changelog=ChangeLog
source=("${pkgname}-${pkgver}.tar.gz"::"https://github.com/michaelrsweet/${pkgname}/archive/v${pkgver}.tar.gz")
sha256sums=('663598a33f21b4d180f4ffd7219c68f7c84fedb7f1a253a804830a40befb113c')

build() {
    cd "${pkgname}-${pkgver}"
    
    ./configure \
        --prefix='/usr' \
        --enable-largefile \
        --enable-ssl \
        --enable-gnutls \
        --enable-cdsassl \
        --enable-localjpeg \
        --enable-localzlib \
        --enable-localpng \
        --with-gui
    
    make
}

package() {
    cd "${pkgname}-${pkgver}"
    
    make DESTDIR="$pkgdir" install
}
