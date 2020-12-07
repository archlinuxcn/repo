# Maintainer: justforlxz <justforlxz@gmail.com>

pkgname=deepin-qt5platform-plugins-git
pkgver=5.0.21.r3.ga7f58a2
pkgrel=2
pkgdesc='Qt platform plugins for DDE'
arch=('x86_64')
url="https://github.com/linuxdeepin/qt5platform-plugins"
license=('GPL3')
provides=('deepin-qt5platform-plugins')
conflicts=('deepin-qt5platform-plugins')
depends=('cairo' 'kwayland' 'qt5-wayland' 'qt5-x11extras')
makedepends=('git' 'expac' 'qt5-xcb-private-headers' 'libglvnd' 'libxcb')
groups=('deepin-git')
source=("$pkgname::git://github.com/linuxdeepin/qt5platform-plugins")
sha512sums=('SKIP')

pkgver() {
    cd $pkgname
    git describe --long --tags | sed 's/\([^-]*-g\)/r\1/;s/-/./g'
}

prepare() {
  cd $pkgname

  rm -r xcb/libqt5xcbqpa-dev wayland/qtwayland-dev
  # Disable wayland for now: https://github.com/linuxdeepin/qt5platform-plugins/issues/47
  sed -i '/wayland/d' qt5platform-plugins.pro

  sed -i 's|error(Not support Qt Version: .*)|INCLUDEPATH += /usr/include/qtxcb-private|' xcb/linux.pri
  sed -i "/qtwayland-dev/a /usr/include/qt/QtWaylandClient/$(expac %v qt5-wayland | cut -d - -f 1) /usr/include/qt/QtXkbCommonSupport/$(expac %v qt5-base | cut -d - -f 1) \\\\" wayland/wayland.pro

  # https://github.com/linuxdeepin/qt5platform-plugins/pull/48
  sed -i 's/xcbWindow-/window-/' xcb/windoweventhook.cpp
}

build() {
  cd $pkgname
  qmake-qt5 PREFIX=/usr
  make
}

package() {
  cd $pkgname
  make INSTALL_ROOT="$pkgdir" install
}
