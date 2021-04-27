# Maintainer: justforlxz <justforlxz@gmail.com>

pkgname=deepin-qt5integration-git
pkgver=5.1.11.r7.g970e863
pkgrel=1
pkgdesc='Qt platform theme integration plugins for DDE'
arch=('x86_64')
url="https://github.com/linuxdeepin/qt5integration"
license=('GPL3')
depends=('dtkwidget-git' 'libqtxdg' 'deepin-qt5platform-plugins-git')
makedepends=('git' 'qt5-tools' 'xcb-util-renderutil' 'gtest')
conflicts=('deepin-qt5integration')
provides=('deepin-qt5integration')
groups=('deepin-git')
source=("$pkgname::git://github.com/linuxdeepin/qt5integration")
sha512sums=('SKIP')

pkgver() {
    cd $pkgname
    git describe --long --tags | sed 's/\([^-]*-g\)/r\1/;s/-/./g'
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
