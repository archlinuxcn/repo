# Maintainer : Daniel Bermond < gmail-com: danielbermond >
# Contributor: James An <james@jamesan.ca>
# Contributor: Mariusz Libera <mariusz.libera@gmail.com>
# Contributor: mortdeus <mortdeus@gocos2d.org>
# Contributor: Sergej Pupykin <pupykin.s+arch@gmail.com>
# Contributor: tobias <tobias@archlinux.org>
# Contributor: Simon Rutishauser <simon.rutishauser@gmx.ch>

pkgname=htmldoc
pkgver=1.9.5
pkgrel=1
pkgdesc='HTML Conversion Software'
arch=('i686' 'x86_64')
url='https://www.msweet.org/htmldoc/index.html'
license=('GPL2')
depends=('libxpm' 'gnutls' 'fltk' 'shared-mime-info')
changelog=ChangeLog
source=("https://github.com/michaelrsweet/htmldoc/releases/download/v${pkgver}/htmldoc-${pkgver}-source.tar.gz"{,.sig})
sha256sums=('0be1ae7986e01e94d482b3af7dcee19800117c8a61ef67426c30ae7744a79ea6'
            'SKIP')
validpgpkeys=('845464660B686AAB36540B6F999559A027815955') # Michael R Sweet

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
