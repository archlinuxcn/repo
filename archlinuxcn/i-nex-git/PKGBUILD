# Maintainer : Vassilis Palassopoulos <palasso [at] gmail [dot] com>
# Based on the PKGBUILD from eloaders <eloaders at linux dot pl>

pkgname=i-nex-git
_pkgname=i-nex
pkgver=7.6.1.r0.gcd1b78d
pkgrel=4
pkgdesc="System information tool like hardinfo, sysinfo"
arch=('i686' 'x86_64')
url="http://i-nex.linux.pl/"
license=('LGPL3')
depends=('gambas3-runtime'
         'gambas3-gb-image'
         'gambas3-gb-form'
         'gambas3-gb-desktop'
         'gambas3-gb-qt5'
         'gambas3-gb-desktop-x11'
         'python2'
         'libcpuid-git'
         'lsb-release'
         'curl'
         'procps-ng')
makedepends=('git' 'gambas3-dev-tools' 'gcc' 'imagemagick')
source=(${_pkgname}::"git+https://github.com/i-nex/I-Nex.git"
        "Fix-error-if-proc-mtrr-doesn-t-exist.patch"
		"Fix-libcpuid-SOVERSION.patch"
		"Adapt-for-new-libcpuid-structure.patch")
sha256sums=('SKIP'
            '5c812da66cf8627e1749722d8e98f0871e6b3dbc30efbce29b785912ff39e96b'
            'a6cee05fcf07c2d2ddbabd4012a3975178c07e0f9d1e876425567d9504eb99cd'
            'fb286cf3bc0b1104e59219e0ba9a236129b20db52b70cd44d65f578404a93cbe')
conflicts=('i-nex')
provides=('i-nex')
backup=('etc/i-nex/Database/i2c/devices.json'
        'etc/i-nex/Database/A6.json'
        'etc/i-nex/Database/amd.json'
        'etc/i-nex/Database/atom.json'
        'etc/i-nex/Database/i3.json'
        'etc/i-nex/Database/i5.json'
        'etc/i-nex/Database/i7.json'
        'etc/i-nex/Database/intel_Core_2_Duo.json'
        'etc/i-nex/Database/intel.json'
        'etc/i-nex/Database/Opteron.json'
        'etc/i-nex/Database/Xeon.json')

pkgver() {
    cd $_pkgname
    git describe --long --tags | sed -r 's/([^-]*-g)/r\1/;s/-/./g'
}

prepare() {
    cd "${srcdir}/${_pkgname}"

	patch -Np1 -i "${srcdir}/Fix-error-if-proc-mtrr-doesn-t-exist.patch"
	patch -Np1 -i "${srcdir}/Fix-libcpuid-SOVERSION.patch"
	patch -Np1 -i "${srcdir}/Adapt-for-new-libcpuid-structure.patch"

    sed -i -e 's|^STATIC.*|STATIC = false|' i-nex.mk
    sed -i -e 's|^UDEV_RULES_DIR.*|UDEV_RULES_DIR = /usr/lib/udev/rules.d|' i-nex.mk
    cd "I-Nex"
    autoreconf -i
}

build() {
    cd "${srcdir}/${_pkgname}"
    cd "I-Nex"
    ./configure --prefix=/usr
    cd ..
    MAGICK_OCL_DEVICE=OFF make -j1
}

package() {
    cd "${srcdir}/${_pkgname}"
    MAGICK_OCL_DEVICE=OFF make -j1 DESTDIR="${pkgdir}/" install
}
