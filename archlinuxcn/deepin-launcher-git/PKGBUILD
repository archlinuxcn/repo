# Maintainer: Dingyuan Zhang <justforlxz@gmail.com>
# Contributor: Dingyuan Zhang <justforlxz@gmail.com>

pkgname=deepin-launcher-git
_pkgname=deepin-launcher
pkgver=5.2.0.14.r2.g8a4be27
pkgrel=1
pkgdesc='Deepin desktop-environment - Launcher module'
arch=('x86_64')
url="https://github.com/linuxdeepin/dde-launcher"
license=('GPL3')
depends=('gsettings-qt' 'qt5-svg' 'qt5-x11extras' 'startdde' 'deepin-qt5integration' 'deepin-daemon' 'deepin-qt-dbus-factory' 'xdg-user-dirs')
makedepends=('git' 'cmake' 'ninja' 'qt5-tools')
conflicts=('deepin-launcher')
replaces=('deepin-launcher')
provides=('deepin-launcher')
groups=('deepin-git')
source=("git://github.com/linuxdeepin/dde-launcher.git")
sha512sums=('SKIP')

pkgver() {
    cd dde-launcher
    git describe --long --tags | sed 's/\([^-]*-g\)/r\1/;s/-/./g'
}

build() {
  cd dde-launcher
  cmake . -GNinja -DCMAKE_INSTALL_PREFIX=/usr -DWITHOUT_UNINSTALL_APP=
  ninja
}

package() {
  cd dde-launcher
  DESTDIR="$pkgdir" ninja install
}
