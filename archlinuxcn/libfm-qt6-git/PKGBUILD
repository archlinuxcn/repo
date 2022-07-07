# Maintainer: Chih-Hsuan Yen <yan12125@archlinux.org>
# Contributor: Peter Mattern <pmattern at arcor dot de>

_pkgname=libfm-qt6
pkgname=$_pkgname-git
pkgver=1.2.1.2.gaa82aa8
pkgrel=1
pkgdesc='Qt port of libfm, a library providing components to build desktop file managers'
arch=('i686' 'x86_64')
url='https://github.com/lxqt/libfm-qt'
license=('LGPL')
depends=('qt6-base' 'menu-cache' 'libexif')
makedepends=('git' 'cmake' 'qt6-tools' 'lxqt-build-tools-qt6-git')
optdepends=(
  'gvfs: support for the trash bin and network devices'
)
provides=("$_pkgname=$pkgver")
conflicts=("$_pkgname")
source=("$_pkgname"::'git+https://github.com/lxqt/libfm-qt.git#branch=wip_qt6')
sha256sums=('SKIP')

pkgver() {
  cd $_pkgname
  git describe --always | sed 's:-:.:g'
}

prepare() {
  mkdir -p build
}

build() {
  cd build

  cmake \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DCMAKE_INSTALL_LIBDIR=lib \
    ../$_pkgname

  make
}

package() {
  cd build

  make DESTDIR="$pkgdir" install

  # CMake installs empty folders unexpectedly
  # https://gitlab.kitware.com/cmake/cmake/issues/17122
  rmdir "$pkgdir"/usr/include/libfm-qt6/{tests,translations}
}
