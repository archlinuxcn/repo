# Maintainer: Shengyu Zhang <lastavengers at archlinuxcn dot org>

pkgname=srain-git
pkgver=0.602.40e16be
pkgrel=1
pkgdesc="Modern, beautiful IRC client written in GTK+ 3"
arch=('i686' 'x86_64')
license=('GPL')
url="https://github.com/SilverRainZ/srain"
depends=('gtk3' 'python' 'curl' 'libnotify')
optdepends=('python-urllib3' 'python-requests')
makedepends=('git' 'make' 'gcc' 'pkg-config' 'gettext' 'imagemagick')
conflicts=('srain')
provides=('srain')
source=("git+https://github.com/SilverRainZ/srain.git")
sha256sums=('SKIP')

pkgver() {
    cd ${pkgname%-git}
    echo "0.$(git rev-list --count HEAD).$(git describe --always)"
}

build() {
    cd ${pkgname%-git}

    mkdir build || true
    ./configure --prefix=/usr --config-dir=/etc --disable-debug
    make
}

package() {
    cd ${pkgname%-git}

    make DESTDIR=$pkgdir install
}
