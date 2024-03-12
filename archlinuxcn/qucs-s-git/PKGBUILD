# Maintainer: taotieren <admin@taotieren.com>

pkgname=qucs-s-git
pkgver=1.0.0.r0.g0656ee80
pkgrel=1
epoch=
pkgdesc="Qucs-S provides GUI for different circuit simulation kernels. "
arch=('x86_64')
url="https://github.com/ra3xdh/qucs_s"
license=('GPL-2.0')
groups=()
depends=(qt5-base)
makedepends=(cmake ninja git autoconf automake perl-gd perl-xml-libxml gperf libtool flex bison qt5-tools qt5-script qt5-svg)
optdepends=('ngspice: recommended simulation backend'
            'qucs: for Qucsator simulation backend'
            'freehdl: to permit digital circuit simulation'
            'asco: to enable circuit optimization'
            )
checkdepends=()
optdepends=()
provides=(${pkgname%-git})
conflicts=(${pkgname%-git})
replaces=()
backup=()
options=('!makeflags')
install=
changelog=
source=("${pkgname%-git}::git+${url}.git")
noextract=()
sha256sums=('SKIP')
validpgpkeys=()

pkgver() {
    cd "${srcdir}/${pkgname%-git}"
    git describe --long --tags | sed 's/^v//g;s/\([^-]*-g\)/r\1/;s/-/./g'
}

build() {
    cd "${srcdir}/${pkgname%-git}"
    cmake -DCMAKE_INSTALL_PREFIX=/usr \
          -B build \
          -G Ninja

    ninja -C build
}

package() {
    cd "${srcdir}/${pkgname%-git}"
    DESTDIR="${pkgdir}" ninja -C "${srcdir}"/${pkgname%-git}/build install
}
