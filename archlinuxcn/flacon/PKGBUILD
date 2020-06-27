# Maintainer: ValHue <vhuelamo at gmail dot com>
#
# Contributor: satanselbow <igdfpm at gmail dot com>
# Contributor: Artem Sereda <overmind88 at gmail dot com>
#
pkgname="flacon"
pkgver="6.1.0"
pkgrel="1"
pkgdesc="An Audio File Encoder. Extracts audio tracks from an audio CD image to separate tracks."
arch=('i686' 'x86_64' 'aarch64')
url="https://flacon.github.io/"
license=('LGPL2.1')
makedepends=('cmake' 'icu' 'qt5-tools')
depends=('hicolor-icon-theme' 'qt5-base' 'uchardet' 'ffmpeg')
optdepends=('flac: For FLAC support'
            'vorbis-tools: For OGG support'
            'mac: For APE support'
            'wavpack: For WavPack support'
            'ttaenc: For TrueAudio support'
            'lame: For MP3 support'
            'mp3gain: For MP3 Replay Gain support'
            'opus-tools: For OPUS support'
            'vorbisgain: For OGG Replay Gain support'
)
conflicts=('flacon-git')

source=("https://github.com/${pkgname}/${pkgname}/archive/v${pkgver}.tar.gz")
sha256sums=('b6af83ed30697ed82369d3eefaf8fcceabea69fc86a1d6d1a5594cc5768bad7b')

build() {
    cd "${srcdir}/${pkgname}-${pkgver}"
    mkdir build

    cd build
    cmake .. -DCMAKE_INSTALL_PREFIX=/usr
    make
}

package() {
    cd "${srcdir}/${pkgname}-${pkgver}/build"
    install -d ${pkgdir}/usr/share/licenses/${pkgname}
    install -m 644 ../LICENSE ${pkgdir}/usr/share/licenses/${pkgname}/LICENSE
    make DESTDIR="${pkgdir}" install
}

# vim:set ts=4 sw=4 et syn=sh ft=sh:
