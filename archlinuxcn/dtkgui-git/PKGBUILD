# Maintainer: justforlxz <justforlxz@gmail.com>

pkgname=dtkgui-git
_commit=5204f570ef298afd3555edd2e3b718e6423681ac
_pkgname=dtkgui
pkgver=5.6.0.2.r14.g5204f57
pkgrel=1
pkgdesc='Deepin Toolkit, gui module for DDE look and feel'
arch=('x86_64' 'aarch64')
url="https://github.com/linuxdeepin/dtkgui"
license=('LGPL3')
depends=('dtkcore-git' 'librsvg' 'qt5-x11extras')
makedepends=('git' 'qt5-tools' 'dtkcore-git' 'librsvg' 'qt5-x11extras' 'gtest' 'gmock' 'cmake' 'ninja' 'doxygen' 'libqtxdg')
conflicts=('dtkgui')
provides=('dtkgui')
groups=('deepin-git')
source=("$_pkgname.tar.gz::https://github.com/linuxdeepin/$_pkgname/archive/$_commit.tar.gz")
sha512sums=('5a9591fb487ec085a3b460da624ffb7433c44cddd4c4fec80f7337f9a5b61027d1b6e1ab7ad6b710f32aa38905357f44ef062f2311944048f89227c9ad0387c9')

build() {
  cd $_pkgname-$_commit
  cmake -GNinja \
    -DNOTPACKAGE=OFF \
    -DMKSPECS_INSTALL_DIR=/usr/lib/qt/mkspecs/modules/ \
    -DBUILD_DOCS=ON \
    -DQCH_INSTALL_DESTINATION=/usr/share/doc/qt \
    -DCMAKE_INSTALL_LIBDIR=/usr/lib \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DCMAKE_BUILD_TYPE=Release
  ninja
}

package() {
  cd $_pkgname-$_commit
  DESTDIR="$pkgdir" ninja install
}
