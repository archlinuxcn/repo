# Maintainer: Jiachen Yang <farseerfc@archlinux.org>
# Co-Maintainer: Felix Yan <felixonmars@archlinux.org>
# Contributor: poplarch <poplarch@gmail.com>

_pkgname=kcm-fcitx5
pkgname=$_pkgname-git
pkgver=r253.d33ce56
pkgrel=3
pkgdesc="KDE Config Module for Fcitx5"
arch=('i686' 'x86_64')
url="https://github.com/fcitx/kcm-fcitx5"
license=('GPL')
depends=('fcitx5-qt5-git' 'knewstuff' 'kcmutils')
makedepends=('extra-cmake-modules' 'python' 'git')
conflicts=("$_pkgname")
provides=("$_pkgname")
source=("git+$url.git")
sha512sums=('SKIP')

pkgver() {
  cd $_pkgname
  printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
}



prepare() {
  mkdir build
}

build() {
  cd build

  cmake ../$_pkgname \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_INSTALL_LIBDIR=lib \
    -DKDE_INSTALL_USE_QT_SYS_PATHS=ON
  make
}

package() {
  cd build
  make DESTDIR="$pkgdir" install
}
