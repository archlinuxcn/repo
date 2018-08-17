# Maintainer: kikadf <kikadf.01@gmail.com>
# Contributor: Daniel Henry <d at hackr dot pl>
# Contributor: Miguel Revilla <yo at  miguelrevilla dot com>
# Contributor: Alfonso Saavedra "Son Link" <sonlink.dourden@gmail.com>
# Contributor: Hexchain Tong <i at hexchain dot org>

pkgname=megasync
_extname=Win
pkgver=3.6.7.0
_sdkver=3.4.0
pkgrel=1
pkgdesc="Sync your files to your Mega account. Official app"
arch=('i686' 'x86_64')
url="https://github.com/meganz/megasync"
license=('custom:MEGA LIMITED CODE REVIEW LICENCE')
depends=('c-ares' 'crypto++' 'libsodium' 'hicolor-icon-theme' 'libuv' 'qt5-svg' 'libmediainfo')
makedepends=('qt5-tools' 'swig' 'doxygen')
optdepends=('sni-qt: fix systray issue on KDE and LXQt')
source=("https://github.com/meganz/MEGAsync/archive/v${pkgver}_${_extname}.tar.gz"
        "https://github.com/meganz/sdk/archive/v${_sdkver}.tar.gz")
sha256sums=('7c896e97cc5de168ee75ce6b99f72e33c90dfe31da62ce00d9f4f5ae9f9a96ee'
            '0a13576ac3efb741dd67c43698a99ff1ff721cc806f28908cc0bdba808d4988b')

prepare(){
    rm -rf MEGAsync-${pkgver}_${_extname}/src/MEGASync/mega
    mv sdk-${_sdkver} MEGAsync-${pkgver}_${_extname}/src/MEGASync/mega
}

build(){
    cd "MEGAsync-${pkgver}_${_extname}/src/MEGASync/mega"
    ./autogen.sh
    ./configure \
        --prefix=/usr \
        --disable-examples \
        --disable-java \
        --disable-php \
        --disable-python \
        --enable-chat \
        --enable-gcc-hardening \
        --with-cares \
        --with-cryptopp \
        --with-curl \
        --with-sodium \
        --with-sqlite \
        --with-zlib \
        --without-freeimage \
        --without-termcap \
	--without-ffmpeg

    cd "${srcdir}/MEGAsync-${pkgver}_${_extname}/src"
    qmake-qt5 CONFIG+="release" MEGA.pro
    lrelease-qt5 MEGASync/MEGASync.pro
    make
}

package (){
    cd "MEGAsync-${pkgver}_${_extname}"
    install -Dm 644 LICENCE.md "${pkgdir}/usr/share/licenses/megasync/LICENCE.md"
    install -Dm 644 installer/terms.txt "${pkgdir}/usr/share/licenses/megasync/terms.txt"

    cd src/MEGASync
    install -Dm 755 megasync "${pkgdir}/usr/bin/megasync"

    cd platform/linux/data
    install -Dm 644 megasync.desktop "${pkgdir}/usr/share/applications/megasync.desktop"

    cd icons/hicolor
    for size in 16x16 32x32 48x48 128x128 256x256
    do
        install -Dm 644 "${size}/apps/mega.png" "${pkgdir}/usr/share/icons/hicolor/${size}/apps/mega.png"
    done
}
