# Maintainer: taotieren <admin@taotieren.com>

pkgname=usbfluxd-git
pkgver=1.0.r9.g0723a9a
pkgrel=5
epoch=
pkgdesc="Redirects the standard usbmuxd socket to allow connections to local and remote usbmuxd instances so remote devices appear connected locally."
arch=('x86_64' 'aarch64' 'riscv64')
url="https://github.com/corellium/usbfluxd"
license=(GPL-2.0 GPL-3.0)
groups=()
depends=(libplist avahi)
makedepends=(git autoconf automake gcc)
checkdepends=()
optdepends=('usbmuxd: USB Multiplex Daemon'
            'socat: Multipurpose relay')
provides=(${pkgname%-git})
conflicts=()
replaces=(${pkgname%-git})
backup=()
options=()
install=
changelog=
source=("${pkgname%-git}::git+${url}.git"
        "fix.patch")
noextract=()
sha256sums=('SKIP'
            '43191a2062ed366bde68da8397c9331164a942eeadff2a39056f2907d5bb52cf')
#validpgpkeys=()

pkgver() {
    cd "${srcdir}/${pkgname%-git}"

    git describe --long --tags | sed 's/^v//;s/\([^-]*-g\)/r\1/;s/-/./g'
}

prepare() {
    cd "${srcdir}/${pkgname%-git}"

    sed -i 's|sbin|bin|g'  usbfluxd/Makefile.am
    patch -p1 < ../fix.patch
    autoreconf -i
}

build() {
    cd "${srcdir}/${pkgname%-git}"

    ./autogen.sh
    ./configure --prefix=/usr \
                --enable-shared=yes \
                --enable-static=no

    make
}

package() {
    cd "${srcdir}/${pkgname%-git}"

    make DESTDIR=${pkgdir} install
}
