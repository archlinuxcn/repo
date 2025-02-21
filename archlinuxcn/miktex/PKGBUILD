# Maintainer: ccat3z <c0ldcat3z@gmail.com>
# Maintainer: heavysink <winstonwu91 at gmail>

pkgname=miktex
pkgver=24.12
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
source=("https://github.com/MiKTeX/miktex/archive/${pkgver}.tar.gz"
        0001-prefer-inline-function-to-macro.patch::https://github.com/MiKTeX/miktex/commit/06beeeaa0e6e7f1df13ccb1fbef6b003e8f3dd4e.patch
        0002-unxemu-refurb.patch::https://github.com/MiKTeX/miktex/commit/8a06a5589be57462e2c812e17359d940e71a13a5.patch)
md5sums=('2d0a5c6a52ecdeb0a6ef21e8a0d2f161'
         'e93284bd71ef2821379261e6a19faed4'
         '0abe1600d26b404738f5fd160426531f')
options=('!buildflags')

prepare() {
    cd "$srcdir/$pkgname-$pkgver"
    patch -p1 -i ../0001-prefer-inline-function-to-macro.patch
    patch -p1 -i ../0002-unxemu-refurb.patch
    find . -name "*.h" -exec sed -i 's|log4cxx/rollingfileappender.h|log4cxx/rolling/rollingfileappender.h|g' {} +
    find . -name "*.cpp" -exec sed -i 's|log4cxx/rollingfileappender.h|log4cxx/rolling/rollingfileappender.h|g' {} +
    cp cmake/modules/FindPOPPLER_QT5.cmake cmake/modules/FindPOPPLER_QT6.cmake
    sed -i 's/QT5/QT6/g' cmake/modules/FindPOPPLER_QT6.cmake
    sed -i 's/qt5/qt6/g' cmake/modules/FindPOPPLER_QT6.cmake
    #sed -i 's|tm/packages/|tm/packages|g' CMakeLists.txt
}
build() {
    cd "$srcdir/$pkgname-$pkgver"
    [ -d build ] || mkdir build
    cd build
    #export MIKTEX_REPOSITORY=https://mirrors.aliyun.com/CTAN/systems/win32/miktex/tm/packages/
    cmake -DCMAKE_BUILD_TYPE='None' -DCMAKE_INSTALL_PREFIX=/opt/miktex -DWITH_UI_QT=ON -DUSE_SYSTEM_POPPLER=TRUE -DUSE_SYSTEM_POPPLER_QT=TRUE ..
    make -j2
}

package() {
    cd "$srcdir/$pkgname-$pkgver/build"
    make DESTDIR="$pkgdir/" install
 
    cd "$srcdir/$pkgname-$pkgver"
    install -vDm644 "README.md"    "${pkgdir}/usr/share/doc/${pkgname}/README.md"
    install -vDm644 "HACKING.md"   "${pkgdir}/usr/share/doc/${pkgname}/HACKING.md"
    install -vDm644 "CHANGELOG.md" "${pkgdir}/usr/share/doc/${pkgname}/CHANGELOG.md"
    install -vDm644 "COPYING.md"   "${pkgdir}/usr/share/licenses/${pkgname}/COPYING.md"

    cd "${pkgdir}/opt/${pkgname}"
    find "share" -type f -exec install -Dm644 "{}" "${pkgdir}/usr/{}" \;
    find "man"   -type f -exec install -Dm644 "{}" "${pkgdir}/usr/share/{}" \;
    rm -rf "share" "man"

    cd "${pkgdir}/usr/share/applications"
    find "icons" -type f -exec install -Dm644 "{}" "${pkgdir}/usr/share/{}" \;
    rm -rf "icons"


    sed -i 's|Exec=|Exec=/opt/miktex/bin/|' "miktex-console.desktop"

    cd "${pkgdir}/usr/share/polkit-1/actions"
    sed -i 's|/usr/bin|/opt/miktex/bin|' "miktex-console.policy"

    cd "${pkgdir}/opt/${pkgname}/bin"
    for _gsu in pkexec kdesu gksu; do
        ln -s "/usr/bin/${_gsu}" "${_gsu}"
    done

    install -dm755 "${pkgdir}/usr/bin"
    find . -type f -name 'miktex*' -exec ln -s "/opt/miktex/bin/{}" "${pkgdir}/usr/bin/{}" \;
}
