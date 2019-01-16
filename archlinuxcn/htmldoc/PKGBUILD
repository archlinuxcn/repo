# Maintainer : Daniel Bermond < gmail-com: danielbermond >
# Contributor: James An <james@jamesan.ca>
# Contributor: Mariusz Libera <mariusz.libera@gmail.com>
# Contributor: mortdeus <mortdeus@gocos2d.org>
# Contributor: Sergej Pupykin <pupykin.s+arch@gmail.com>
# Contributor: tobias <tobias@archlinux.org>
# Contributor: Simon Rutishauser <simon.rutishauser@gmx.ch>

pkgname=htmldoc
pkgver=1.9.4
pkgrel=3
pkgdesc='HTML Conversion Software'
arch=('i686' 'x86_64')
url='https://www.msweet.org/htmldoc/index.html'
license=('GPL2')
depends=('libxpm' 'gnutls' 'fltk' 'shared-mime-info')
changelog=ChangeLog
source=("https://github.com/michaelrsweet/htmldoc/releases/download/v${pkgver}/htmldoc-${pkgver}-source.tar.gz"{,.sig})
noextract=("htmldoc-${pkgver}-source.tar.gz")
sha256sums=('8e33d22e0d757099bcbc09d513dae599bdb735450f2af24597f325a7a854d1f7'
            'SKIP')
validpgpkeys=('845464660B686AAB36540B6F999559A027815955') # Michael R Sweet

prepare() {
    mkdir -p "${pkgname}-${pkgver}"
    cd "${pkgname}-${pkgver}"
    
    # source file misses a top-level directory
    bsdtar -xf "${srcdir}/htmldoc-${pkgver}-source.tar.gz"
}

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
