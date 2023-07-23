# Maintainer: Gonzalo Exequiel Pedone <hipersayan DOT x AT gmail DOT com>

pkgname=webcamoid
pkgver=9.1.1
pkgrel=1
pkgdesc="Webcamoid is a full featured webcam capture application."
url='https://webcamoid.github.io/'
license=('GPL')
arch=('i686' 'x86_64' 'armv6h' 'aarch64')
depends=('qt5-quickcontrols2'
         'qt5-svg')
optdepends=('v4l-utils: Extra formats support for webcams'
            'akvcam-dkms-git: Virtual camera support (Recommended)'
            'v4l2loopback-dkms: Virtual camera support'
            'ffmpeg: Video playback/recording/conversion (Recommended)'
            'gst-plugins-base: Video playback/recording/conversion'
            'gst-plugins-good: Video playback/recording/conversion'
            'gst-plugins-bad: Video playback/recording/conversion'
            'gst-plugins-ugly: Video playback/recording/conversion'
            'vlc: Video playback (Recommended)'
            'pipewire: Screen capture'
            'libpulse: Audio playback (Recommended)'
            'alsa-lib: Audio playback'
            'jack: Audio playback'
            'portaudio: Audio playback'
            'sdl2: Audio playback'
            'libuvc: Camera capture'
            'qt5-multimedia: Camera capture'
            'polkit: Root privileges for virtual camera module (Recommended)')
makedepends=('alsa-lib'
             'cmake'
             'ffmpeg4.4'
             'git'
             'gst-plugins-base-libs'
             'jack'
             'libpulse'
             'libuvc'
             'pipewire'
             'portaudio'
             'qt5-multimedia'
             'qt5-tools'
             'sdl2'
             'v4l-utils'
             'vlc')
provides=('webcamoid')
conflicts=('webcamoid')
install="${pkgname}.install"
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/${pkgname}/${pkgname}/archive/${pkgver}.tar.gz")
md5sums=('39ca28c17a9c1c6380c59e41989ebb0e')

build() {
    cd "$srcdir/${pkgname}-${pkgver}"
    export PKG_CONFIG_PATH='/usr/lib/ffmpeg4.4/pkgconfig'
    cmake \
        -DCMAKE_BUILD_TYPE=Release \
        -DCMAKE_INSTALL_PREFIX=/usr \
        .
    make $MAKEFLAGS
}

package() {
    cd "$srcdir/${pkgname}-${pkgver}"
    make DESTDIR="${pkgdir}" install
}
