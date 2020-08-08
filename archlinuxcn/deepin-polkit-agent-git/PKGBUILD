# Maintainer: DingYuan Zhang <justforlxz@gmail.com>

pkgname=deepin-polkit-agent-git
pkgver=5.2.0.7.r1.g9d192f2
pkgrel=1
pkgdesc='Deepin Polkit Agent'
arch=('x86_64')
url="https://github.com/linuxdeepin/dde-polkit-agent"
license=('GPL3')
depends=('deepin-qt5integration-git' 'deepin-qt-dbus-factory-git' 'polkit-qt5')
makedepends=('git' 'qt5-tools')
conflicts=('deepin-polkit-agent')
replaces=('deepin-polkit-agent')
provides=('deepin-polkit-agent')
groups=('deepin-git')
source=('git://github.com/linuxdeepin/dde-polkit-agent')
sha512sums=('SKIP')

pkgver() {
    cd dde-polkit-agent
    git describe --long --tags | sed 's/\([^-]*-g\)/r\1/;s/-/./g'
}

prepare() {
  cd dde-polkit-agent
  # https://github.com/linuxdeepin/developer-center/issues/1721
  sed -i 's/bool is_deepin = true/bool is_deepin = false/' policykitlistener.cpp
}

build() {
  cd dde-polkit-agent
  qmake-qt5 PREFIX=/usr
  make
}

package() {
  cd dde-polkit-agent
  make INSTALL_ROOT="$pkgdir" install
}
