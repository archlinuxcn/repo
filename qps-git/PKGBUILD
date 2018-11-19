# Maintainer:  Peter Mattern <pmattern at arcor dot de>

_pkgname=qps
pkgname=$_pkgname-git
pkgver=r37.3e80692
pkgrel=1
pkgdesc='Qt process manager'
arch=('i686' 'x86_64')
url='https://github.com/QtDesktop/qps'
license=('GPL')
depends=('qt5-x11extras' 'gtk-update-icon-cache')
makedepends=('git' 'cmake' 'qt5-tools')
provides=("$_pkgname")
conflicts=("$_pkgname")
source=("git+https://github.com/QtDesktop/qps.git")
sha256sums=("SKIP")

pkgver() {
    cd $_pkgname
    printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
}

build() {
    mkdir build ; cd build
    cmake ../$_pkgname -DCMAKE_INSTALL_PREFIX=/usr
    make
}

package() {
    cd build
    make DESTDIR=$pkgdir install
}
