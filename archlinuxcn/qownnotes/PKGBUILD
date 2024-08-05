# Maintainer: Patrizio Bekerle <patrizio at bekerle dot com>

pkgname=qownnotes
pkgver=24.8.3
tag="380bc11bf7966e8d6198040adb1eaf2f6a5347fa"
pkgrel=1
pkgdesc="Plain-text file markdown note taking with Nextcloud/ownCloud integration"
arch=('i686' 'x86_64' 'armv7h' 'aarch64')
url='https://www.qownnotes.org/'
license=('GPL2')
groups=('qownnotes')
depends=('qt5-base' 'qt5-svg' 'qt5-declarative' 'openssl' 'qt5-websockets' 'qt5-x11extras' 'aspell')
makedepends=('qt5-tools')
source=("https://github.com/pbek/QOwnNotes/releases/download/v${pkgver}/qownnotes-${pkgver}.tar.xz")
sha256sums=('95b3494fa21b2204d82e9b0c58ae8d9345d7870d437bec1982b1f80c4d6f0ca8')

prepare() {
    cd "${pkgname}-${pkgver}"
    echo "#define RELEASE \"AUR\"" > release.h
}

build() {
    cd "${pkgname}-${pkgver}"
    qmake QMAKE_CFLAGS_RELEASE="${CFLAGS}" QMAKE_CXXFLAGS_RELEASE="${CXXFLAGS}" QMAKE_LFLAGS_RELEASE="${LDFLAGS}"
    make
}

package() {
    cd "${pkgname}-${pkgver}"

    # install application
    install -D -m755 QOwnNotes "${pkgdir}/usr/bin/QOwnNotes"

    # install visuals
    install -D -m644 PBE.QOwnNotes.desktop "${pkgdir}/usr/share/applications/PBE.QOwnNotes.desktop"
    for format in {16x16,24x24,32x32,48x48,64x64,96x96,128x128,256x256,512x512}; do
        install -D -m644 "images/icons/${format}/apps/QOwnNotes.png" "${pkgdir}/usr/share/icons/hicolor/$format/apps/QOwnNotes.png"
    done
    install -D -m644 "images/icons/scalable/apps/QOwnNotes.svg" "${pkgdir}/usr/share/icons/hicolor/scalable/apps/QOwnNotes.svg"

    # install languages
    install -d "${pkgdir}/usr/share/qt5/translations/"
    install -D -m644 languages/*.qm "${pkgdir}/usr/share/qt5/translations/"
}
