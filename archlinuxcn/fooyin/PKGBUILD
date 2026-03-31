# Maintainer: zxp19821005 <zxp19821005 at 163 dot com>
pkgname=fooyin
_pkgname=Fooyin
pkgver=0.10.2
pkgrel=2
pkgdesc="A customisable music player."
arch=('x86_64')
url="https://www.fooyin.org/"
_ghurl="https://github.com/ludouzi/fooyin"
license=('GPL-3.0-only')
depends=(
    'qt6-base'
    'alsa-lib'
    'taglib'
    'ffmpeg'
    'kdsingleapplication'
    'libvgm-git'
    'qcoro'
)
makedepends=(
    'qt6-svg'
    'qt6-tools'
    'ninja'
    'cmake'
    'libpipewire'
    'icu'
    'libopenmpt'
    'libsndfile'
    'libebur128'
    'libarchive'
    'libgme'
    'soundtouch'
    'git'
)
optdepends=(
    'sdl2: For the SDL2 audio output plugin'
    'libpipewire: For the PipeWire audio output plugin'
    'libopenmpt: For the OpenMPT audio input plugin'
    'libgme: For the GME audio input plugin'
    'libsndfile: For the GME audio input plugin'
    'libarchive: For the libarchive archive plugin'
    'libebur128: For the ReplayGain scanner plugin'
    'soundtouch: Enable building a dsp plugin based on soundtouch.'
)
source=(
    "${pkgname}-${pkgver}.tar.gz::${_ghurl}/archive/refs/tags/v${pkgver}.tar.gz"
)
sha256sums=('5cdd33835679578c940ac5d3dfabaa94406a707d44f0b4b1f7fff11417c5457c')
build() {
    cd "${srcdir}/${pkgname}-${pkgver}"
    cmake -S . -B build -G Ninja \
        -DCMAKE_INSTALL_PREFIX=/usr \
        -DBUILD_PCH=ON \
        -DBUILD_WERROR=OFF \
        -DINSTALL_HEADERS=ON \
        -DCMAKE_BUILD_TYPE=None
    cmake --build build
}
package() {
    cd "${srcdir}/${pkgname}-${pkgver}"
    DESTDIR="${pkgdir}" cmake --install build
    install -Dm644 "${srcdir}/${pkgname}-${pkgver}/COPYING" "${pkgdir}/usr/share/licenses/fooyin/LICENSE"
}
