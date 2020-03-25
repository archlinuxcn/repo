# $Id: PKGBUILD 226039 2017-04-27 13:52:30Z felixonmars $
# Maintainer: Felix Yan <felixonmars@archlinux.org>
# Contributor: csslayer <wengxt AT gmail com>

_pkgname=fcitx5-qt
pkgbase=$_pkgname-git
pkgname=(fcitx5-qt5-git fcitx5-qt4-git)
pkgver=r154.b22d216
pkgrel=1
pkgdesc="Fcitx Qt Library"
arch=('x86_64')
url="https://github.com/fcitx/fcitx5-qt"
license=('GPL')
depends=('fcitx5-git')
makedepends=('extra-cmake-modules' 'git' 'qt4' 'qt5-x11extras' 'qt5-quickcontrols')
source=("git+$url.git")
sha512sums=('SKIP')

pkgver() {
  cd $_pkgname
  printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
}

build(){
  cd $_pkgname

  cmake -DCMAKE_INSTALL_PREFIX=/usr -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_LIBDIR=/usr/lib .
  make

  # install into /tmp and split the package
  make DESTDIR="/tmp/$_pkgname/" install
}

_mv_pkg(){
  mkdir -p "$pkgdir/$(dirname $1)"
  mv "$@" "$pkgdir/$(dirname $1)"
}

package_fcitx5-qt5-git(){
  depends=('fcitx5-git' 'qt5-x11extras' 'qt5-quickcontrols')
  provides=('fcitx5-qt5' 'fcitx5-qt')
  conflicts=('fcitx5-qt5' 'fcitx5-qt')
  pkgdesc="Fcitx Qt Library, for Qt5"

  cd /tmp/$_pkgname
  _mv_pkg usr/share
  _mv_pkg usr/lib/qt
  _mv_pkg usr/lib/libFcitx5Qt5*
  _mv_pkg usr/lib/fcitx5
  _mv_pkg usr/lib/cmake/Fcitx5Qt5DBusAddons
  _mv_pkg usr/lib/cmake/Fcitx5Qt5WidgetsAddons
  _mv_pkg usr/include/Fcitx5Qt5
}

package_fcitx5-qt4-git(){
  depends=('fcitx5-git' 'qt4')
  provides=('fcitx5-qt4')
  conflicts=('fcitx5-qt4')
  pkgdesc="Fcitx Qt Library, for Qt4"

  cd /tmp/$_pkgname
  _mv_pkg usr/lib/qt4
  _mv_pkg usr/lib/libFcitx5Qt4*
  _mv_pkg usr/lib/cmake/Fcitx5Qt4DBusAddons
  _mv_pkg usr/include/Fcitx5Qt4
}
