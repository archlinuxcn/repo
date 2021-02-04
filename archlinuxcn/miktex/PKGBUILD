# Maintainer: ccat3z <c0ldcat3z@gmail.com>
# Maintainer: heavysink <winstonwu91 at gmail>

pkgname=miktex
pkgver=20.12
pkgrel=1
pkgdesc="a distribution of the TeX/LaTeX typesetting system"
arch=('x86_64')
url="https://miktex.org"
license=('custom')
depends=('apr' 'apr-util' 'bzip2' 'cairo' 'expat' 'fontconfig' 'freetype2'
         'fribidi' 'gd' 'gmp' 'graphite' 'harfbuzz-icu' 'hunspell' 'icu'
         'libjpeg' 'log4cxx' 'xz' 'mpfr' 'libmspack' 'openssl' 'pixman' 'libpng'
         'poppler' 'popt' 'potrace' 'uriparser' 'zziplib' 'poppler-qt5' 'qt5-script')
makedepends=('cmake' 'coreutils' 'fop' 'sed' 'libxslt' 'qt5-tools')
source=("https://github.com/MiKTeX/miktex/archive/${pkgver}.tar.gz")
md5sums=('7ecd805e8afa8cd93cbc8254533da34d')

prepare() {
    cd "$srcdir/$pkgname-$pkgver"
    sed -i '/#include <QPainter>/a #include <QPainterPath>' Programs/Editors/TeXworks/source/modules/QtPDF/src/PDFBackend.cpp
}

build() {
    cd "$srcdir/$pkgname-$pkgver"	
    [ -d build ] || mkdir build
    cd build
    cmake -DCMAKE_INSTALL_PREFIX=/opt/miktex -DWITH_UI_QT=ON ..
    make
}

package() {
    cd "$srcdir/$pkgname-$pkgver/build"
    make DESTDIR="$pkgdir/" install
    
    cd $pkgdir

    install -Dm644 opt/miktex/share/applications/miktex-console.desktop usr/share/applications/miktex-console.desktop
    sed -i 's/^Exec=miktex-console$/Exec=\/opt\/miktex\/bin\/miktex-console/' usr/share/applications/miktex-console.desktop
    cp -R opt/miktex/share/applications/icons usr/share/

    mv opt/miktex/man usr/share/man
    #rm $pkgdir/usr/share/man/man5/updmap.cfg.5.gz
}
