# Maintainer: ccat3z <c0ldcat3z@gmail.com>
# Maintainer: heavysink <winstonwu91 at gmail>

pkgname=miktex
pkgver=24.4
pkgrel=3
pkgdesc="a distribution of the TeX/LaTeX typesetting system"
arch=('x86_64')
url="https://miktex.org"
license=('custom')
depends=('apr' 'boost-libs' 'apr-util' 'bzip2' 'cairo' 'expat' 'fontconfig' 'freetype2'
         'fribidi' 'gd' 'gmp' 'graphite' 'harfbuzz-icu' 'hunspell' 'icu'
         'libjpeg' 'log4cxx' 'xz' 'mpfr' 'libmspack' 'openssl' 'pixman' 'libpng'
         'poppler' 'popt' 'potrace' 'uriparser' 'hicolor-icon-theme' 'zziplib' 'poppler-qt6' 'qt6-declarative' 'qt6-5compat' 'mpfi')
makedepends=('cmake' 'coreutils' 'fop' 'sed' 'libxslt' 'qt6-tools' 'boost')
source=("https://github.com/MiKTeX/miktex/archive/${pkgver}.tar.gz")
md5sums=('d9dbaedcc2efe3020d00be0ce0548d99')
options=('!buildflags')

prepare() {
    cd "$srcdir/$pkgname-$pkgver"
    find . -name "*.h" -exec sed -i 's|log4cxx/rollingfileappender.h|log4cxx/rolling/rollingfileappender.h|g' {} +
    find . -name "*.cpp" -exec sed -i 's|log4cxx/rollingfileappender.h|log4cxx/rolling/rollingfileappender.h|g' {} +
    cp cmake/modules/FindPOPPLER_QT5.cmake cmake/modules/FindPOPPLER_QT6.cmake
    sed -i 's/QT5/QT6/g' cmake/modules/FindPOPPLER_QT6.cmake
    sed -i 's/qt5/qt6/g' cmake/modules/FindPOPPLER_QT6.cmake
    sed -i 's|tm/packages/|tm/packages|g' CMakeLists.txt
}
build() {
    cd "$srcdir/$pkgname-$pkgver"
    [ -d build ] || mkdir build
    cd build
    export MIKTEX_REPOSITORY=https://mirrors.aliyun.com/CTAN/systems/win32/miktex/tm/packages/
    cmake -DCMAKE_INSTALL_PREFIX=/opt/miktex -DWITH_UI_QT=ON -DUSE_SYSTEM_POPPLER=TRUE -DUSE_SYSTEM_POPPLER_QT=TRUE ..
    make -j2
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
