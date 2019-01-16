# Maintainer: Rafał Kozdrój <kozeid2@gmail.com>
# Contributor: kikadf <kikadf.01@gmail.com>
# Contributor: Daniel Henry <d at hackr dot pl>
# Contributor: Miguel Revilla <yo at  miguelrevilla dot com>
# Contributor: Alfonso Saavedra "Son Link" <sonlink.dourden@gmail.com>
# Contributor: Hexchain Tong <i at hexchain dot org>

pkgname=megasync
_extname=Linux
pkgver=3.7.1.0
pkgrel=2
pkgdesc="Sync your files to your Mega account. Official app"
arch=('i686' 'x86_64')
url="https://github.com/meganz/MEGAsync"
license=('custom:MEGA LIMITED CODE REVIEW LICENCE')
depends=('c-ares' 'crypto++' 'libsodium' 'hicolor-icon-theme' 'libuv'
         'qt5-svg' 'libmediainfo' 'libraw')
makedepends=('qt5-tools' 'swig' 'doxygen' 'lsb-release' 'git')
optdepends=('sni-qt: fix systray issue on KDE and LXQt')
source=("git+https://github.com/meganz/MEGAsync.git#tag=v${pkgver}_${_extname}"
        "git+https://github.com/meganz/sdk.git")
sha256sums=('SKIP'
            'SKIP')

prepare(){
    cd "MEGAsync"
    git submodule init
    git config submodule.src/MEGASync/mega.url "$srcdir/sdk"
    git submodule update
}

build(){
    cd "MEGAsync/src/MEGASync/mega"
    ./autogen.sh
    ./configure \
        --prefix=/usr \
        --disable-examples \
        --disable-java \
        --disable-php \
        --disable-python \
        --enable-chat \
        --with-cares \
        --with-cryptopp \
        --with-curl \
        --with-sodium \
        --with-sqlite \
        --with-zlib \
        --without-freeimage \
        --without-termcap \
        --without-ffmpeg

    cd "../.."
    qmake-qt5 CONFIG+="release" MEGA.pro
    lrelease-qt5 MEGASync/MEGASync.pro
    make
}

package (){
    cd "MEGAsync"
    install -Dm 644 LICENCE.md "${pkgdir}/usr/share/licenses/megasync/LICENCE"
    install -Dm 644 installer/terms.txt "${pkgdir}/usr/share/licenses/megasync/terms.txt"

    cd "src"
    make INSTALL_ROOT="${pkgdir}" install

    cd "MEGASync"
    install -Dm 755 megasync "${pkgdir}/usr/bin/megasync"
}
