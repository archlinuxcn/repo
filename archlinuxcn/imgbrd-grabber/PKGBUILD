# Maintainer: HurricanePootis <hurricanepootis@protonmail.com>
pkgname=imgbrd-grabber
pkgver=7.11.2
pkgrel=6
pkgdesc="Very customizable imageboard/booru downloader with powerful filenaming features."
arch=('x86_64')
url="https://github.com/Bionus/imgbrd-grabber"
license=('Apache-2.0')
depends=('qt5-multimedia' 'qt5-declarative' 'nodejs' 'qt5-networkauth' 'hicolor-icon-theme' 'gcc-libs' 'glibc' 'qt5-base')
makedepends=('git' 'cmake' 'qt5-tools' 'npm')
optdepends=('openssl: Access HTTPS sources')
conflicts=("imgbrd-grabber-git" 'imgbrd-grabber-bin' 'imgbrd-grabber-appimage')
source=('git+https://github.com/Bionus/imgbrd-grabber.git#tag=v'${pkgver}''
        'git+https://github.com/LaurentGomila/qt-android-cmake.git'
        'git+https://github.com/sakra/cotire.git'
        'git+https://github.com/lexbor/lexbor.git'
        'git+https://github.com/catchorg/Catch2.git')
sha256sums=('7e2e90768266caa806e0db74630bd58df96fe192a08f17ec85d71196e834621a'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP')

prepare() {
    cd "$srcdir/${pkgname}"
    git submodule init
    git config submodule.cmake/qt-android-cmake.url "$srcdir/qt-android-cmake"
    git config submodule.cmake/cotire.url "$srcdir/cotire"
    git config submodule.tests/src/vendor/catch.url "$srcdir/Catch2"
    git config submodule.lib/vendor/lexbor.url "$srcdir/lexbor"
    git -c protocol.file.allow=always submodule update
}

build() {
    cd "$srcdir/${pkgname}/src/sites"

    npm install --no-optional

    cd "$srcdir" 

    cmake -S $pkgname/src -B build \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DUSE_QSCINTILLA=0 \
    -DUSE_BREAKPAD=O \
    -Wno-dev

    cmake --build build
}

package() {
    cd "$srcdir"

    DESTDIR="$pkgdir/" cmake --install build && rm -rf "$pkgdir/usr/include" "$pkgdir/usr/lib"

    touch "$pkgdir/usr/share/Grabber/settings.ini"
}
