# Maintainer: Andrew Rabert <ar@nullsum.net>

pkgname=jellyfin-media-player
pkgver=1.12.0
pkgrel=2
pkgdesc='Jellyfin Desktop Client'
arch=('i686' 'x86_64')
license=('GPL')
url='https://github.com/jellyfin/jellyfin-media-player'
depends=('mpv' 'libcec' 'sdl2' 'p8-platform' 'protobuf' 'qt5-webengine' 'qt5-x11extras' 'qt5-quickcontrols')
makedepends=('cmake' 'git' 'python')
source=("https://github.com/jellyfin/jellyfin-media-player/archive/refs/tags/v${pkgver}.tar.gz"
        "disable-update-check.patch"
        "fix-cmake-4.patch")
sha256sums=('a90c8ced214f7f66f440bb690c64ac333e18bdfb5bc54d845ea5fc2d04f31ed5'
            '23727ef8f727ac17af228f29aa5508230caac9d02f37d6c12908fcf50d4f382a'
            '7ff8a15d9e9a7bc9a75bc9f0ee730408827827f6f6d564686ac9f9ca26525342')

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
