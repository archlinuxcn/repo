# Maintainer: Taegil Bae <esrevinu@gmail.com>
# Contributor: Ben Reedy <breed808 *AT* breed808 *DOT* com>
# Contributor: xylosper <darklin20@gmail.com>
# Contributor: Kaan Kasım <kaankasim88@gmail.com>

_pkgbase=bomi

pkgname=$_pkgbase-git
pkgver=0.9.11.r25.g90f18ff
pkgrel=1
pkgdesc="Powerful and easy-to-use GUI multimedia player based on mpv (git version)"
arch=('i686' 'x86_64')
url="http://bomi-player.github.io"
license=('GPL')
#install=$_pkgbase.install
depends=('qt5-base' 'qt5-declarative' 'qt5-x11extras' 'qt5-quickcontrols' 'qt5-svg'
         'libdvdread' 'libdvdnav' 'libcdio-paranoia' 'libcdio' 'smbclient'
         'alsa-lib' 'libpulse' 'jack' 'libchardet' 'libbluray'
         'libva' 'libvdpau' 'libgl' 'fribidi' 'libass' 'ffmpeg')
makedepends=('git' 'mesa' 'gcc' 'pkg-config' 'python' 'qt5-tools')
optdepends=('libva-intel-driver: hardware acceleration support for Intel GPU'
            'mesa-vdpau: hardware acceleration support for AMD/NVIDIA opensource driver'
            'youtube-dl: streaming website support including YouTube'
            'libaacs: AACS decryption for Blu-ray support'
            'libbdplus: BD+ decryption for Blu-ray support')
provides=('bomi')
conflicts=('cmplayer' 'bomi')
source=(git+https://github.com/xylosper/${_pkgbase}.git
        compilation_fix.patch)
md5sums=('SKIP'
         '787abc07aa2de7403657a060e2971dec')
#options=(debug !strip)

pkgver() {
    cd "$srcdir/$_pkgbase"
    echo $(git describe --tags | sed -E 's/([^-]*-g)/r\1/;s/-/./g' | cut -c2-)
}

prepare() {
    cd "$srcdir/$_pkgbase"
    patch -p1 -i ${srcdir}/compilation_fix.patch

    ./configure --prefix=/usr
}

build() {
    cd "$srcdir/$_pkgbase"
    make
}

package() {
    cd "$srcdir/$_pkgbase"
    make DEST_DIR="$pkgdir" install
}
