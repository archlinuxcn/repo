# Maintainer: Rafał Kozdrój <kozeid2+aur@gmail.com>
# Contributor: kikadf <kikadf.01@gmail.com>
# Contributor: Daniel Henry <d at hackr dot pl>
# Contributor: Miguel Revilla <yo at  miguelrevilla dot com>
# Contributor: Alfonso Saavedra "Son Link" <sonlink.dourden@gmail.com>
# Contributor: Hexchain Tong <i at hexchain dot org>

pkgname=megasync
pkgver=4.7.3.0
pkgrel=1
pkgdesc="Easy automated syncing between your computers and your MEGA cloud drive"
arch=('i686' 'x86_64')
url="https://github.com/meganz/MEGAsync"
license=('custom:MEGA LIMITED CODE REVIEW LICENCE')
depends=('c-ares' 'crypto++' 'libsodium' 'hicolor-icon-theme' 'libuv'
         'qt5-svg' 'qt5-x11extras' 'libmediainfo' 'libraw' 'qt5-base'
         'ffmpeg' 'libpdfium' 'freeimage' 'libudev.so')
makedepends=('qt5-tools' 'swig' 'doxygen' 'lsb-release' 'git')
_extname="_Linux"
source=("git+https://github.com/meganz/MEGAsync.git#tag=v${pkgver}${_extname}"
        "meganz-sdk::git+https://github.com/meganz/sdk.git"
        "pdfium.patch"
        "ffmpeg.patch")
sha256sums=('SKIP'
            'SKIP'
            'bdad237f67d772789bf6e6835108827201296fc5cf793d28d94af8a1b04e56c9'
            '939a46fb0c54f900156e9e68ec4369926e9610b1ca6e9fd6ca09e538fbb84688')

prepare() {
    cd "MEGAsync"
    git submodule init
    git config submodule.src/MEGASync/mega.url "../meganz-sdk"
    git -c protocol.file.allow=always submodule update

    cd "src/MEGASync/mega"
    patch -Np1 -i "$srcdir/pdfium.patch"
    patch -Np1 -i "$srcdir/ffmpeg.patch"
}

build() {
    # build sdk
    cd "MEGAsync/src/MEGASync/mega"

    ./autogen.sh
    ./configure \
        --disable-shared \
        --enable-static \
        --disable-silent-rules \
        --disable-curl-checks \
        --disable-megaapi \
        --with-cryptopp \
        --with-sodium \
        --with-zlib \
        --with-sqlite \
        --with-cares \
        --with-curl \
        --with-freeimage \
        --with-libuv \
        --disable-posix-threads \
        --disable-examples \
        --with-libzen \
        --with-libmediainfo \
        --with-ffmpeg \
        --enable-drive-notifications \
        --prefix="${srcdir}/MEGAsync/src/MEGASync/mega/bindings/qt/3rdparty"

    # build megasync
    cd "../.."
    qmake-qt5 \
        "CONFIG += FULLREQUIREMENTS" \
        MEGA.pro
    lrelease-qt5 MEGASync/MEGASync.pro
    make
}

package () {
    cd "MEGAsync"
    install -Dm 644 LICENCE.md "${pkgdir}/usr/share/licenses/megasync/LICENCE"
    install -Dm 644 installer/terms.txt "${pkgdir}/usr/share/licenses/megasync/terms.txt"
    install -Dm 644 src/MEGASync/mega/LICENSE "${pkgdir}/usr/share/licenses/megasync/SDK-LICENCE"

    cd "src"
    mkdir -pm 755 "${pkgdir}/usr/bin"
    make INSTALL_ROOT="${pkgdir}" TARGET="${pkgdir}/usr/bin/megasync" install

    install -Dm 755 "MEGASync/megasync" "${pkgdir}/usr/bin/megasync"
}
