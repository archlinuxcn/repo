# Maintainer: Peter Mattern <pmattern at arcor dot de>

_pkgname=libfm-qt
pkgname=$_pkgname-git
pkgver=r301.f0f38ac
pkgrel=1
pkgdesc='Qt port of libfm, a library providing components to build desktop file managers'
arch=('i686' 'x86_64')
url='https://github.com/lxde/libfm-qt'
license=('LGPL')
depends=('qt5-x11extras' 'libfm>=1.2.0')
makedepends=('cmake' 'qt5-tools')
provides=("$_pkgname")
conflicts=("$_pkgname")
source=('git+https://github.com/lxde/libfm-qt.git')
sha256sums=("SKIP")

pkgver() {
  cd $_pkgname
  printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
}

build() {
  mkdir -p build ; cd build
  cmake $srcdir/$_pkgname -DCMAKE_INSTALL_PREFIX=/usr -DCMAKE_INSTALL_LIBDIR=lib
  make
}

package() {
  cd build
  make DESTDIR=$pkgdir install
}
