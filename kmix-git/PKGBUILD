# Maintainer: Antonio Rojas 

pkgname=kmix-git
pkgver=r1972.9814a23
pkgrel=1
pkgdesc='KDE volume control program'
arch=('i686' 'x86_64')
url='http://kde.org/applications/multimedia/kmix/'
license=('GPL')
depends=('kdelibs4support' 'kcmutils' 'libcanberra')
makedepends=('extra-cmake-modules' 'git' 'kdoctools' 'python')
conflicts=('kdemultimedia-kmix' 'kmix')
provides=('kmix')
source=("git://anongit.kde.org/kmix.git")
install=$pkgname.install
sha256sums=('SKIP')

pkgver() {
  cd kmix
  printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
}

prepare() {
  mkdir -p build
  
  cd kmix
  sed -e 's|CMAKE_MODULE_PATH ${ECM_MODULE_PATH} ${ECM_KDE_MODULE_DIR}|CMAKE_MODULE_PATH ${ECM_MODULE_PATH} ${ECM_KDE_MODULE_DIR} ${CMAKE_SOURCE_DIR}/cmake/modules|' -i CMakeLists.txt
}

build() { 
  cd build
  cmake ../kmix \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DCMAKE_BUILD_TYPE=Release \
    -DKMIX_KF5_BUILD=ON \
    -DLIB_INSTALL_DIR=lib \
    -DKDE_INSTALL_USE_QT_SYS_PATHS=ON
  make
}

package() {
  cd build
  make DESTDIR="$pkgdir" install
}
