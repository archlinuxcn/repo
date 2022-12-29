# Maintainer: justforlxz <justforlxz@gmail.com>

pkgname=dtkgui-git
pkgver=5.6.3.r8.ga69ed2e
pkgrel=1
pkgdesc='Deepin Toolkit, gui module for DDE look and feel'
arch=('x86_64' 'aarch64')
url="https://github.com/linuxdeepin/dtkgui"
license=('LGPL3')
depends=('dtkcore-git' 'librsvg' 'qt5-x11extras' 'libqtxdg' 'freeimage')
makedepends=('git' 'qt5-tools' 'dtkcommon-git' 'dtkcore-git' 'librsvg' 'qt5-x11extras' 'gtest' 'gmock' 'cmake' 'ninja' 'doxygen' 'libqtxdg' 'freeimage')
conflicts=('dtkgui')
provides=('dtkgui')
groups=('deepin-git')
source=("$pkgname::git+https://github.com/linuxdeepin/dtkgui")
sha512sums=('SKIP')

pkgver() {
    cd $pkgname
    git describe --long --tags | sed 's/\([^-]*-g\)/r\1/;s/-/./g'
}

build() {
  cd $pkgname
  cmake -B build -GNinja \
    -DNOTPACKAGE=OFF \
    -DMKSPECS_INSTALL_DIR=lib/qt/mkspecs/modules/ \
    -DBUILD_DOCS=ON \
    -DQCH_INSTALL_DESTINATION=share/doc/qt \
    -DCMAKE_INSTALL_LIBDIR=lib \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DCMAKE_BUILD_TYPE=Release
  cmake --build build
}

package() {
  cd $pkgname/build
  DESTDIR="$pkgdir" ninja install
}
