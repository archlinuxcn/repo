# Maintainer: Antonio Rojas <arojas@archlinux.org>

pkgname=kscreen-frameworks
pkgver=2.0git_d6380ef
pkgrel=1
pkgdesc='KDE screen management software'
arch=('i686' 'x86_64')
url='https://projects.kde.org/projects/extragear/libs/libkscreen'
license=('LGPL')
depends=('kxmlgui' 'libkscreen-frameworks' 'kdeclarative')
makedepends=('extra-cmake-modules' 'git' 'python')
conflicts=('kscreen')
install=$pkgname.install
source=('git://anongit.kde.org/kscreen.git#commit=d6380ef')
md5sums=('SKIP')

prepare() {
  mkdir -p build
}

build() {
  cd build
  cmake ../kscreen \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DLIB_INSTALL_DIR=lib \
    -DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
    -DBUILD_TESTING=OFF
  make
}

package() {
  cd build
  make DESTDIR="$pkgdir" install
}
