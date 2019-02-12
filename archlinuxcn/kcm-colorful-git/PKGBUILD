# Maintainer: Jianqiu Zhang <void001@archlinuxcn.org>


pkgname=kcm-colorful-git
pkgver=0.0.1
pkgrel=1
pkgdesc='Make your KDE plasma colorful'
arch=('x86_64')
url="https://github.com/IsoaSFlus/kcm-colorful"
license=('GPL2')
depends=('kconfigwidgets')
makedepends=('cmake' 'git' 'extra-cmake-modules' 'qt5-base' 'frameworkintegration' 'kcmutils')

source=(
    "kcm-colorful::git+https://github.com/IsoaSFlus/kcm-colorful"
)

sha256sums=('SKIP')

prepare() {
    cd $srcdir/kcm-colorful
    git submodule init
    git submodule update
}

build() {
    cd $srcdir/kcm-colorful
    mkdir -p build
    cd build
    cmake -DCMAKE_INSTALL_PREFIX="$pkgdir/usr" ..
    make
}

package() {
    cd $srcdir/kcm-colorful/build
    make install
}
