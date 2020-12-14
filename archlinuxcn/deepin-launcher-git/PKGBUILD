# Maintainer: justforlxz <justforlxz@gmail.com>

pkgname=deepin-launcher-git
pkgver=5.3.0.35.r27.g52252e2d
pkgrel=1
pkgdesc='Deepin desktop-environment - Launcher module'
arch=('x86_64')
url="https://github.com/linuxdeepin/dde-launcher"
license=('GPL3')
depends=('gsettings-qt' 'qt5-svg' 'qt5-x11extras' 'startdde-git' 'deepin-daemon-git' 'deepin-qt-dbus-factory-git' 'xdg-user-dirs')
makedepends=('git' 'cmake' 'ninja' 'qt5-tools' 'qt5-base' 'qt5-x11extras' 'qt5-svg' 'dtkwidget-git')
conflicts=('deepin-launcher')
provides=('deepin-launcher')
groups=('deepin-git')
source=("$pkgname::git://github.com/linuxdeepin/dde-launcher.git")
sha512sums=('SKIP')

pkgver() {
    cd $pkgname
    git describe --long --tags | sed 's/\([^-]*-g\)/r\1/;s/-/./g'
}

build() {
  cd $pkgname
  cmake . -GNinja -DCMAKE_INSTALL_PREFIX=/usr -DWITHOUT_UNINSTALL_APP=
  ninja
}

package() {
  cd $pkgname
  DESTDIR="$pkgdir" ninja install
}
