# Maintainer: Andrew Rabert <ar@nullsum.net>

pkgname=jellyfin-media-player
pkgver=1.9.1
_webver=10.9.0
pkgrel=6
pkgdesc='Jellyfin Desktop Client'
arch=('i686' 'x86_64')
license=('GPL')
url='https://github.com/jellyfin/jellyfin-media-player'
depends=('mpv' 'libcec' 'sdl2' 'p8-platform' 'protobuf' 'qt5-webengine' 'qt5-x11extras' 'qt5-quickcontrols')
makedepends=('cmake' 'git' 'python')
source=("https://github.com/jellyfin/jellyfin-media-player/archive/refs/tags/v${pkgver}.tar.gz"
        "jellyfin_${_webver}.tar.xz::https://repo.jellyfin.org/files/server/portable/stable/v${_webver}/any/jellyfin_${_webver}.tar.xz"
        "disable-update-check.patch"
        "fix-mpv-0_38_0.patch"
        "fix-mpv-volume.patch")
sha256sums=('8d119bb78e897ace3041cf332114a79c51be4d8e0cc8c68f5745fd588c2b9bde'
            'b041e01f4eedf06fbfe24cab7cc6a3e9c884fc9b823d6f5393ae0025f11bea74'
            'add2430dec35bef4fbf028273f8492cc8a530e9f6a3c2ae4b0a33d83e743aec1'
            '3cb05f527df63ce34b50099a5676ee65d2c5a902c47d238e355a615c8b439f66'
            '9c64e8b2535be5545fa4bdff9984298b67ae490478d224b7b4f6a202f7ba64b3')

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
