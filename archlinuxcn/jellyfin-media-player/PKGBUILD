# Maintainer: Andrew Rabert <ar@nullsum.net>

pkgname=jellyfin-media-player
pkgver=1.9.1
_webver=10.8.10
pkgrel=1
pkgdesc='Jellyfin Desktop Client'
arch=('i686' 'x86_64')
license=('GPL')
url='https://github.com/jellyfin/jellyfin-media-player'
depends=('mpv' 'libcec' 'sdl2' 'p8-platform' 'protobuf' 'qt5-webengine' 'qt5-x11extras' 'qt5-quickcontrols')
makedepends=('cmake' 'git' 'python')
source=("https://github.com/jellyfin/jellyfin-media-player/archive/refs/tags/v${pkgver}.tar.gz"
        "jellyfin-web_${_webver}.tar.gz::https://repo.jellyfin.org/releases/server/portable/versions/stable/web/${_webver}/jellyfin-web_${_webver}_portable.tar.gz")
sha256sums=('8d119bb78e897ace3041cf332114a79c51be4d8e0cc8c68f5745fd588c2b9bde'
            'd6145a247239fb9a9f2cc7e69549ca08b0c33878c0b249670fcc64d4dfb20552')

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
