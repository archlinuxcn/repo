# Maintainer: Shengyu Zhang <la@archlinuxcn.org>

pkgname=srain-git
pkgver=1.0.1.2.g0c86dc7
pkgrel=1
pkgdesc="Modern IRC client written in GTK, git version"
arch=('i686' 'x86_64')
license=('GPL')
url="https://srain.im"
makedepends=('git' 'make' 'gcc' 'pkg-config' 'gettext' 'python-sphinx')
depends=('glib2' 'gtk3' 'libconfig' 'libsoup')
optdepends=(
    'glib-networking: TLS connection support'
    )
conflicts=('srain')
provides=('srain')
source=("git+https://github.com/SrainApp/srain.git#branch=master")
sha256sums=('SKIP')

_prefix='/usr'

pkgver() {
    cd ${pkgname%-git}
    git describe --tags | sed 's/-/./g'
}

build() {
    cd ${pkgname%-git}

    ./configure                         \
        --prefix="${_prefix}"           \
        --datadir="${_prefix}/share"    \
        --sysconfdir="/etc"             \
        --disable-debug
    make
    make doc
}

package() {
    cd ${pkgname%-git}

    make DESTDIR="${pkgdir}" install
    make DESTDIR="${pkgdir}" install-doc
}
