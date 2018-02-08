# Maintainer : Daniel Bermond < yahoo-com: danielbermond >
# Contributor: James An <james@jamesan.ca>
# Contributor: Mariusz Libera <mariusz.libera@gmail.com>
# Contributor: mortdeus <mortdeus@gocos2d.org>
# Contributor: Sergej Pupykin <pupykin.s+arch@gmail.com>
# Contributor: tobias <tobias@archlinux.org>
# Contributor: Simon Rutishauser <simon.rutishauser@gmx.ch>

pkgname=htmldoc
pkgver=1.9.2
pkgrel=1
pkgdesc='HTML Conversion Software'
arch=('i686' 'x86_64')
url='http://www.msweet.org/htmldoc/index.html'
license=('GPL2')
depends=('libxpm' 'gnutls' 'fltk')
conflicts=('htmldoc-git')
changelog=ChangeLog
source=("${pkgname}-${pkgver}.tar.gz"::"https://github.com/michaelrsweet/${pkgname}/archive/v${pkgver}.tar.gz")
sha256sums=('f967654f1cd607f80297f46d774b5607cda80ab8199f358d868a7efa77de35d3')

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
