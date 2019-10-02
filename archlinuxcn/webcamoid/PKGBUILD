# Maintainer: Gonzalo Exequiel Pedone <hipersayan DOT x AT gmail DOT com>

pkgname=webcamoid
pkgver=8.7.0
pkgrel=1
pkgdesc="Webcamoid is a full featured webcam capture application."
url='https://webcamoid.github.io/'
license=('GPL')
arch=('i686' 'x86_64' 'armv6h')
depends=('qt5-quickcontrols'
         'qt5-quickcontrols2'
         'qt5-svg')
optdepends=('v4l-utils: Extra formats support for webcams'
            'akvcam-dkms: Virtual camera support (Recommended)'
            'v4l2loopback-dkms: Virtual camera support'
            'ffmpeg: Video playing/recording/conversion (Recommended)'
            'gst-plugins-base: Video playing/recording/conversion'
            'gst-plugins-good: Video playing/recording/conversion'
            'gst-plugins-bad: Video playing/recording/conversion'
            'gst-plugins-ugly: Video playing/recording/conversion'
            'libpulse: Audio playback (Recommended)'
            'alsa-lib: Audio playback'
            'jack: Audio playback'
            'qt5-multimedia: Audio playback'
            'libuvc: Camera capture'
            'polkit: Root privileges for virtual camera module (Recommended)'
            'kde-cli-tools: Root privileges for virtual camera module'
            'gksu: Root privileges for virtual camera module'
            'kdesudo: Root privileges for virtual camera module')
makedepends=('v4l-utils'
             'qt5-tools'
             'qt5-multimedia'
             'ffmpeg'
             'gst-plugins-base-libs'
             'libpulse'
             'alsa-lib'
             'jack'
             'libuvc')
provides=('webcamoid')
conflicts=('webcamoid-git')
install="${pkgname}.install"
source=("https://github.com/${pkgname}/${pkgname}/archive/${pkgver}.tar.gz")
sha256sums=('6fb9c55b574f06700802f10a5c20105c6c53ba4da43d842d1580bcefe7e9dbe6')

build() {
    cd "$srcdir/${pkgname}-${pkgver}"
    qmake-qt5 Webcamoid.pro CONFIG+=silent
    make $MAKEFLAGS
}

package() {
    cd "$srcdir/${pkgname}-${pkgver}"
    make INSTALL_ROOT="${pkgdir}" install
}
