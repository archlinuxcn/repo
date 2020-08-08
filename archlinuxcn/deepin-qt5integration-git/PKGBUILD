# Maintainer: DingYuan Zhang <justforlxz@gmail.com>

pkgname=deepin-qt5integration-git
pkgver=5.1.0.3.r18.g8a8e950
pkgrel=1
pkgdesc='Qt platform theme integration plugins for DDE'
arch=('x86_64')
url="https://github.com/linuxdeepin/qt5integration"
license=('GPL3')
depends=('dtkwidget-git' 'libqtxdg' 'deepin-qt5platform-plugins-git')
makedepends=('xcb-util-renderutil')
conflicts=('deepin-qt5integration')
replaces=('deepin-qt5integration')
provides=('deepin-qt5integration')
groups=('deepin-git')
source=("git://github.com/linuxdeepin/qt5integration")
sha512sums=('SKIP')

pkgver() {
    cd qt5integration
    git describe --long --tags | sed 's/\([^-]*-g\)/r\1/;s/-/./g'
}

build() {
  cd qt5integration
  qmake-qt5 PREFIX=/usr
  make
}

package() {
  cd qt5integration
  make INSTALL_ROOT="$pkgdir" install
}
