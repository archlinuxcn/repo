# Maintainer: Andrew Rabert <ar@nullsum.net>

pkgname=jellyfin-media-player
pkgver=1.9.0
_webver=10.8.9
pkgrel=2
pkgdesc='Jellyfin Desktop Client'
arch=('i686' 'x86_64')
license=('GPL')
url='https://github.com/jellyfin/jellyfin-media-player'
depends=('mpv' 'libcec' 'sdl2' 'p8-platform' 'protobuf' 'qt5-webengine' 'qt5-x11extras' 'qt5-quickcontrols')
makedepends=('cmake' 'git' 'python')
source=("https://github.com/jellyfin/jellyfin-media-player/archive/refs/tags/v${pkgver}.tar.gz"
        "jellyfin-web_${_webver}.tar.gz::https://repo.jellyfin.org/releases/server/portable/versions/stable/web/${_webver}/jellyfin-web_${_webver}_portable.tar.gz")
sha256sums=('366aac5a355d9dd435037442e0fff091a85019ea8b27ce6db3f957c8dd54d1ca'
            'e5b74735c370f665adc5122a9037e615ceb49fce00060a172328979adcb69ef9')

build() {
    cd "${srcdir}/jellyfin-media-player-${pkgver}"
    mkdir -p build
    cd build
    cp -r "${srcdir}/jellyfin-web_${_webver}" dist
    cmake \
        -DCMAKE_BUILD_TYPE='Release' \
        -DCMAKE_INSTALL_PREFIX='/usr/' \
        -DCMAKE_SKIP_RPATH=1 \
        -DLINUX_X11POWER=ON \
        -DQTROOT=./qt \
        ..
    make
}

package() {
    cd "${srcdir}/jellyfin-media-player-${pkgver}/build"
    DESTDIR="${pkgdir}" make install
}
