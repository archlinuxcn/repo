# Maintainer: DingYuan Zhang <justforlxz@gmail.com>

pkgname=deepin-qt5platform-plugins-git
pkgver=5.0.13.r30.g8586e63
pkgrel=1
pkgdesc='Qt platform plugins for DDE'
arch=('x86_64')
url="https://github.com/linuxdeepin/qt5platform-plugins"
license=('GPL3')
provides=('deepin-qt5platform-plugins')
conflicts=('deepin-qt5platform-plugins')
replaces=('deepin-qt5platform-plugins')
depends=('cairo' 'kwayland' 'qt5-wayland' 'qt5-x11extras')
makedepends=('expac' 'qt5-xcb-private-headers' 'libglvnd' 'libxcb')
groups=('deepin-git')
source=("git://github.com/linuxdeepin/qt5platform-plugins")
sha512sums=('SKIP')

pkgver() {
    cd qt5platform-plugins
    git describe --long --tags | sed 's/\([^-]*-g\)/r\1/;s/-/./g'
}

prepare() {
  cd qt5platform-plugins

  rm -r xcb/libqt5xcbqpa-dev wayland/qtwayland-dev
  # Disable wayland for now: https://github.com/linuxdeepin/qt5platform-plugins/issues/47
  sed -i '/wayland/d' qt5platform-plugins.pro

  sed -i 's|error(Not support Qt Version: .*)|INCLUDEPATH += /usr/include/qtxcb-private|' xcb/linux.pri
  sed -i "/qtwayland-dev/a /usr/include/qt/QtWaylandClient/$(expac %v qt5-wayland | cut -d - -f 1) /usr/include/qt/QtXkbCommonSupport/$(expac %v qt5-base | cut -d - -f 1) \\\\" wayland/wayland.pro

  # https://github.com/linuxdeepin/qt5platform-plugins/pull/48
  sed -i 's/xcbWindow-/window-/' xcb/windoweventhook.cpp
}

build() {
  cd qt5platform-plugins
  qmake-qt5 PREFIX=/usr
  make
}

package() {
  cd qt5platform-plugins
  make INSTALL_ROOT="$pkgdir" install
}
