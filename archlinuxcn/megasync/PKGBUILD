# Maintainer : Daniel Bermond <dbermond@archlinux.org>
# Contributor: Rafał Kozdrój <kozeid2+aur@gmail.com>
# Contributor: kikadf <kikadf.01@gmail.com>
# Contributor: Daniel Henry <d at hackr dot pl>
# Contributor: Miguel Revilla <yo at  miguelrevilla dot com>
# Contributor: Alfonso Saavedra "Son Link" <sonlink.dourden@gmail.com>
# Contributor: Hexchain Tong <i at hexchain dot org>

pkgname=megasync
pkgver=5.2.1.0
pkgrel=1
pkgdesc='Official MEGA desktop application for syncing with MEGA Cloud Drive'
arch=('x86_64')
url='https://github.com/meganz/MEGAsync/'
license=('LicenseRef-Mega-Limited-Code-License')
depends=('c-ares' 'crypto++' 'curl' 'ffmpeg' 'freeimage' 'icu' 'libmediainfo'
         'libpdfium' 'libsodium' 'libudev.so' 'libuv' 'libxcb' 'libzen' 'openssl'
         'qt5-base' 'qt5-quickcontrols' 'qt5-svg' 'qt5-x11extras' 'sqlite' 'zlib'
         'hicolor-icon-theme')
makedepends=('git' 'doxygen' 'lsb-release' 'qt5-tools' 'swig')
source=("git+https://github.com/meganz/MEGAsync.git#tag=v${pkgver}_Linux"
        'meganz-sdk'::'git+https://github.com/meganz/sdk.git'
        '010-megasync-libpdfium.patch'
        '020-megasync-ffmpeg.patch')
sha256sums=('b3ef84d4a33f6fbced388b882c3189a367cfba63bcc4a55e4ba0ad97dfecad81'
            'SKIP'
            '9a1c1b15f99a5858f91f892a17f80dc3ad08850b90e07d8226f1f2412c97025a'
            '49690421d98e8f61a600ee1ec97adc3e4d1cbe2f736fcf56056da23d02db378b')

prepare() {
    git -C MEGAsync submodule init
    git -C MEGAsync config --local submodule.src/MEGASync/mega.url "${srcdir}/meganz-sdk"
    git -C MEGAsync -c protocol.file.allow='always' submodule update
    
    patch -d MEGAsync/src/MEGASync/mega -Np1 -i "${srcdir}/010-megasync-libpdfium.patch"
    patch -d MEGAsync/src/MEGASync/mega -Np1 -i "${srcdir}/020-megasync-ffmpeg.patch"
    
    cd MEGAsync/src/MEGASync/mega
    ./autogen.sh
}

build() {
    # sdk
    cd MEGAsync/src/MEGASync/mega
    ./configure \
        --prefix="${srcdir}/MEGAsync/src/MEGASync/mega/bindings/qt/3rdparty" \
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
        --enable-drive-notifications
    
    # megasync
    cd "${srcdir}/MEGAsync/src"
    qmake-qt5 'CONFIG += FULLREQUIREMENTS' MEGA.pro
    lrelease-qt5 MEGASync/MEGASync.pro
    make
}

package () {
    make -C MEGAsync/src INSTALL_ROOT="$pkgdir" TARGET="${pkgdir}/usr/bin/megasync" install
    install -D -m755 MEGAsync/src/MEGASync/megasync -t "${pkgdir}/usr/bin"
    install -D -m644 MEGAsync/LICENCE.md -t "${pkgdir}/usr/share/licenses/megasync"
    install -D -m644 MEGAsync/installer/terms.txt -t "${pkgdir}/usr/share/licenses/megasync"
    install -D -m644 MEGAsync/src/MEGASync/mega/LICENSE "${pkgdir}/usr/share/licenses/megasync/SDK-LICENCE"
    rm -r "${pkgdir}/usr/share/icons/ubuntu-mono-dark"
}
