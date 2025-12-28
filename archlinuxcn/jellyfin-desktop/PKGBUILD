# Maintainer: Andrew Rabert <ar@nullsum.net>

pkgname=jellyfin-desktop
pkgver=2.0.0
pkgrel=2
pkgdesc='Jellyfin Desktop Client'
arch=('i686' 'x86_64')
license=('GPL')
url='https://github.com/jellyfin/jellyfin-desktop'
depends=('mpv' 'mpvqt' 'libcec' 'sdl2' 'p8-platform' 'protobuf' 'qt6-webengine' 'qt6-declarative')
makedepends=('cmake' 'git' 'ninja' 'python')
source=("https://github.com/jellyfin/jellyfin-desktop/archive/refs/tags/v${pkgver}.tar.gz")
sha256sums=('782e0e7f916efa04b8714ca895f60276320c9682f6c82aea6ff3b82bce466ee7')

build() {
    cd "${srcdir}/jellyfin-desktop-${pkgver}"
    rm -rf build
    mkdir build
    cmake \
        -B build \
        -G Ninja \
        -DCMAKE_BUILD_TYPE='Release' \
        -DCMAKE_INSTALL_PREFIX='/usr/' \
        -DCMAKE_SKIP_RPATH=1 \
        -DQTROOT=build/qt \
        -Wno-dev
    cmake --build build
}

package() {
    cd "${srcdir}/jellyfin-desktop-${pkgver}"
    DESTDIR="${pkgdir}" cmake --install build
}
