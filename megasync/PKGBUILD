# Maintainer: Alfonso Saavedra "Son Link" <sonlink.dourden@gmail.com>
# Maintainer: Hexchain Tong <i at hexchain dot org>
pkgname=megasync
pkgver=2.9.8.0
_pkgver=${pkgver//./_}
pkgrel=2
pkgdesc="Sync your files to your Mega account. Official app"
arch=('i686' 'x86_64')
url="https://github.com/meganz/megasync"
license=('custom:MEGA LIMITED CODE REVIEW LICENCE')
depends=('curl' 'c-ares' 'crypto++' 'libsodium' 'hicolor-icon-theme' 'qt5-base' 'libuv')
makedepends=('git' 'qt5-tools')
optdepends=('sni-qt: fix systray issue on KDE and LXQt')
source=("git+https://github.com/meganz/MEGAsync.git#tag=v${_pkgver}_Linux")
md5sums=('SKIP')

prepare(){
    cd "$srcdir/MEGAsync"
    git submodule update --init --recursive
}

build(){
    cd "$srcdir/MEGAsync/src/MEGASync/mega"
    ./autogen.sh
    ./configure \
        --enable-gcc-hardening \
        --disable-silent-rules \
        --disable-megaapi \
        --with-cryptopp \
        --with-sodium \
        --with-zlib \
        --with-sqlite \
        --with-cares \
        --with-curl \
        --without-freeimage \
        --without-readline \
        --without-termcap \
        --disable-examples \
        --prefix=/usr

    cd "$srcdir/MEGAsync/src"
    qmake-qt5 CONFIG+="release" MEGA.pro
    lrelease-qt5 MEGASync/MEGASync.pro
    make
}

package (){
    cd "$srcdir/MEGAsync"
    install -Dm 644 LICENCE.md "$pkgdir/usr/share/licenses/megasync/LICENCE.md"
    install -Dm 644 installer/terms.txt "$pkgdir/usr/share/licenses/megasync/terms.txt"

    cd src/MEGASync
    install -Dm 755 megasync "$pkgdir/usr/bin/megasync"

    cd platform/linux/data
    install -Dm 644 megasync.desktop "$pkgdir/usr/share/applications/megasync.desktop"

    cd icons/hicolor
    for size in 16x16 32x32 48x48 128x128 256x256
    do
        install -Dm 644 "$size/apps/mega.png" "$pkgdir/usr/share/icons/hicolor/$size/apps/mega.png"
    done
}
