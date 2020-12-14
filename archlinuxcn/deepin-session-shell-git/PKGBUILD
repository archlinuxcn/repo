# Maintainer: justforlxz <justforlxz@gmail.com>

pkgname=deepin-session-shell-git
pkgver=5.3.0.39.r27.g91b33e6
pkgrel=1
pkgdesc='Deepin desktop-environment - session-shell module'
arch=('x86_64')
url="https://github.com/linuxdeepin/dde-session-shell"
license=('GPL3')
depends=('deepin-daemon-git' 'deepin-wallpapers' 'gsettings-qt' 'liblightdm-qt5' 'startdde-git')
makedepends=('git' 'cmake' 'ninja' 'qt5-tools')
conflicts=('deepin-session-ui<5' 'deepin-session-shell')
provides=('lightdm-deepin-greeter' 'deepin-session-shell')
groups=('deepin-git')
source=("$pkgname::git://github.com/linuxdeepin/dde-session-shell")
sha512sums=('SKIP')

pkgver() {
    cd $pkgname
    git describe --long --tags | sed 's/\([^-]*-g\)/r\1/;s/-/./g'
}

prepare() {
  cd $pkgname
  sed -i '/darrowrectangle/d' CMakeLists.txt src/widgets/widgets.pri
  sed -i '1i#include <QPainterPath>' src/widgets/useravatar.cpp

  # We don't have common-auth on Arch
  sed -i 's/common-auth/system-login/' src/libdde-auth/authagent.cpp
}

build() {
  cd $pkgname
  cmake . -GNinja -DCMAKE_INSTALL_PREFIX=/usr
  ninja
}

package() {
  cd $pkgname
  DESTDIR="$pkgdir" ninja install

  chmod +x "$pkgdir"/usr/bin/deepin-greeter
}
