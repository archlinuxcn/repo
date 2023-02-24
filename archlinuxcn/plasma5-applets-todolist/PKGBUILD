# Maintainer: Stephan Springer <buzo+arch@Lini.de>
# Contributor: kikadf <kikadf.01@gmail.com>

_pkgname=plasma-applet-todolist
pkgname=plasma5-applets-todolist
pkgver=13
pkgrel=1
pkgdesc="Extension of the kdeplasma-applets notes widget, where it's organized as a list"
url="https://github.com/Zren/$_pkgname"
license=(GPL)
depends=('plasma-workspace' 'qt5-declarative')
makedepends=('extra-cmake-modules')
arch=('any')
source=("$pkgname-$pkgver.tar.gz::https://github.com/Zren/$_pkgname/archive/v$pkgver.tar.gz"
        'CMakeLists.txt')
sha256sums=('f6de06bf11a2efbe3f4bebcb078743e8d32e1aa5a68b5e438b10a12571ecc7ea'
            '94af6eb61a665717e30a8a58d5609dc631149cd5a44d7c3f5f059503bca5b6e9')

prepare() {
    cp "$srcdir"/CMakeLists.txt "$_pkgname-$pkgver"
    mkdir -p build
}

build() {
    cd build
    cmake ../"$_pkgname-$pkgver" \
          -DCMAKE_INSTALL_PREFIX=/usr \
          -DCMAKE_BUILD_TYPE=Release \
          -DCMAKE_INSTALL_LIBDIR=lib \
          -DKDE_INSTALL_USE_QT_SYS_PATHS=ON
}

package() {
    cd build
    make DESTDIR="$pkgdir" install
}
