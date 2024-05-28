# Maintainer: Andrew Rabert <ar@nullsum.net>

pkgname=jellyfin-media-player
pkgver=1.10.1
_webver=10.9.3
pkgrel=2
pkgdesc='Jellyfin Desktop Client'
arch=('i686' 'x86_64')
license=('GPL')
url='https://github.com/jellyfin/jellyfin-media-player'
depends=('mpv' 'libcec' 'sdl2' 'p8-platform' 'protobuf' 'qt5-webengine' 'qt5-x11extras' 'qt5-quickcontrols')
makedepends=('cmake' 'git' 'python')
source=("https://github.com/jellyfin/jellyfin-media-player/archive/refs/tags/v${pkgver}.tar.gz"
        "jellyfin_${_webver}.tar.xz::https://repo.jellyfin.org/files/server/portable/stable/v${_webver}/any/jellyfin_${_webver}.tar.xz"
        "disable-update-check.patch")
sha256sums=('1d8dfc2695a1796bb05c9030eb0611fe251e9c45f7414f400fc7ca446235adb5'
            'bffffd8a1da06852ad903587f497f9af348fa5aa2209c65eb1d8792a58543048'
            '23727ef8f727ac17af228f29aa5508230caac9d02f37d6c12908fcf50d4f382a')

prepare() {
    cd "${srcdir}/jellyfin-media-player-${pkgver}"
    for patch_file in ../*.patch; do
        patch -Np1 < "${patch_file}"
    done
}

build() {
    cd "${srcdir}/jellyfin-media-player-${pkgver}"
    rm -rf build
    mkdir build
    cp -r "${srcdir}/jellyfin/jellyfin-web" build/dist
    cmake \
        -B build \
        -DCMAKE_BUILD_TYPE='Release' \
        -DCMAKE_INSTALL_PREFIX='/usr/' \
        -DCMAKE_SKIP_RPATH=1 \
        -DQTROOT=build/qt \
        -Wno-dev
    cmake --build build
}

package() {
    cd "${srcdir}/jellyfin-media-player-${pkgver}"
    DESTDIR="${pkgdir}" cmake --install build
}
