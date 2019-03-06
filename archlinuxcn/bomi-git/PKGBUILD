# Maintainer: Taegil Bae <esrevinu@gmail.com>
# Contributor: Ben Reedy <breed808 *AT* breed808 *DOT* com>
# Contributor: xylosper <darklin20@gmail.com>
# Contributor: Kaan Kasım <kaankasim88@gmail.com>

_pkgbase=bomi

pkgname=$_pkgbase-git
pkgver=0.9.11.r39.g5f0cc0a7
pkgrel=3
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
source=(git+https://github.com/d-s-x/${_pkgbase}.git
        add_sup_subext.patch
        upgrade_waf.patch)
md5sums=('SKIP'
         'dacb0df199eea0f6e3d5c037c8c5429d'
         'fbcd3b66086bb2f7c94c07c63c335fb3')
#options=(debug !strip)

pkgver() {
    cd "$srcdir/$_pkgbase"
    echo $(git describe --tags | sed -E 's/([^-]*-g)/r\1/;s/-/./g' | cut -c2-)
}

prepare() {
    cd "$srcdir/$_pkgbase"

    patch -Np1 -i $srcdir/add_sup_subext.patch

    # While compiling mpv, an error occurs in waf python code.
    # Upgrading waf version fixes it.
    patch -Np1 -i $srcdir/upgrade_waf.patch
    pushd src/mpv
    rm waf
    ./bootstrap.py
    popd

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
