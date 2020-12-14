# Maintainer: justforlxz <justforlxz@gmail.com>

pkgname=deepin-dock-git
pkgver=5.3.0.49.r17.g30b1ce633
pkgrel=1
pkgdesc='Deepin desktop-environment - dock module'
arch=('x86_64')
url="https://github.com/linuxdeepin/dde-dock"
license=('GPL3')
depends=('qt5-svg' 'deepin-daemon-git' 'deepin-qt5integration-git'
         'deepin-qt-dbus-factory-git' 'deepin-network-utils-git' 'libdbusmenu-qt5')
makedepends=('git' 'cmake' 'ninja' 'qt5-tools' 'deepin-qt5integration-git' 'deepin-qt-dbus-factory' 'deepin-network-utils-git')
conflicts=('deepin-dock')
provides=('deepin-dock')
groups=('deepin-git')
source=("$pkgname::git://github.com/linuxdeepin/dde-dock")
sha512sums=('SKIP')

pkgver() {
    cd $pkgname
    git describe --long --tags | sed 's/\([^-]*-g\)/r\1/;s/-/./g'
}

build() {
  cd $pkgname
  cmake . -GNinja -DCMAKE_INSTALL_PREFIX=/usr -DCMAKE_INSTALL_LIBDIR=lib -DDOCK_TRAY_USE_NATIVE_POPUP=YES
  ninja
}

package() {
  cd $pkgname
  DESTDIR="$pkgdir" ninja install
}
