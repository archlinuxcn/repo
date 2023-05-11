# Maintainer: Chih-Hsuan Yen <yan12125@archlinux.org>

_pkgname=lxqt-menu-data
pkgname=$_pkgname-git
pkgver=r10.616b94a
pkgrel=2
pkgdesc='LXQt menu files'
arch=(any)
#groups=(lxqt)
url='https://github.com/lxqt/lxqt-menu-data'
license=('GPL' 'LGPL')
makedepends=(git cmake lxqt-build-tools-git qt5-tools)
source=('git+https://github.com/lxqt/lxqt-menu-data.git')
sha256sums=('SKIP')

pkgver() {
  cd lxqt-menu-data
  printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
}

build() {
  cmake -B build -S lxqt-menu-data \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DCMAKE_BUILD_TYPE=None
  make -C build
}

package() {
  cd build
  make DESTDIR="$pkgdir" install
}
