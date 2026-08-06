# Maintainer: Gonzalo Exequiel Pedone <hipersayan DOT x AT gmail DOT com>

pkgname=webcamoid
pkgver=9.4.0
pkgrel=1
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
            'pipewire: Screen capture'
            'libpulse: Audio playback (Recommended)'
            'alsa-lib: Audio playback'
            'portaudio: Audio playback'
            'libuvc: Camera capture'
            'qt6-multimedia: Camera capture'
            'polkit: Root privileges for virtual camera module')
makedepends=('alsa-lib'
             'cmake'
             'ffmpeg'
             'git'
             'libpulse'
             'libuvc'
             'pipewire'
             'portaudio'
             'qt6-multimedia'
             'qt6-tools'
             'v4l-utils')
provides=('webcamoid')
conflicts=('webcamoid')
install="${pkgname}.install"
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/${pkgname}/${pkgname}/archive/${pkgver}.tar.gz")
md5sums=('b48673f1b8e947c8c41b4b0090b39f1d')

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
