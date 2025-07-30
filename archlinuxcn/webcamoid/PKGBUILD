# Maintainer: Gonzalo Exequiel Pedone <hipersayan DOT x AT gmail DOT com>

pkgname=webcamoid
pkgver=9.3.0
pkgrel=2
pkgdesc="Webcamoid is a full featured webcam capture application."
url='https://webcamoid.github.io/'
license=('GPL')
arch=('i686' 'x86_64' 'armv6h' 'aarch64')
depends=('qt6-declarative'
         'qt6-svg')
optdepends=('v4l-utils: Extra formats support for webcams'
            'akvcam-dkms-git: Virtual camera support (Recommended)'
            'v4l2loopback-dkms: Virtual camera support'
            'ffmpeg: Video playback/recording/conversion (Recommended)'
            'gst-plugins-base: Video playback/conversion'
            'gst-plugins-good: Video playback/conversion'
            'gst-plugins-bad: Video playback/conversion'
            'gst-plugins-ugly: Video playback/conversion'
            'vlc: Video playback (Recommended)'
            'pipewire: Screen capture'
            'libpulse: Audio playback (Recommended)'
            'alsa-lib: Audio playback'
            'jack: Audio playback'
            'portaudio: Audio playback'
            'sdl3: Audio playback'
            'libuvc: Camera capture'
            'qt6-multimedia: Camera capture'
            'polkit: Root privileges for virtual camera module')
makedepends=('alsa-lib'
             'cmake'
             'ffmpeg'
             'git'
             'gst-plugins-base-libs'
             'jack'
             'libpulse'
             'libuvc'
             'pipewire'
             'portaudio'
             'qt6-multimedia'
             'qt6-tools'
             'sdl3'
             'v4l-utils'
             'vlc')
provides=('webcamoid')
conflicts=('webcamoid')
install="${pkgname}.install"
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/${pkgname}/${pkgname}/archive/${pkgver}.tar.gz")
md5sums=('62e0e0f530e74f9c8e17bf9228ada507')

build() {
    cd "${srcdir}/${pkgname}-${pkgver}"

    cmake \
        -S . \
        -B build \
        -DCMAKE_BUILD_TYPE=Release \
        -DCMAKE_INSTALL_PREFIX=/usr
    make -C build $MAKEFLAGS
}

package() {
    cd "${srcdir}/${pkgname}-${pkgver}"

    make -C build DESTDIR="${pkgdir}" install
}
