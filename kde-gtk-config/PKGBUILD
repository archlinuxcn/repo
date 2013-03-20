# Maintainer: birdflesh <antkoul at gmail dot com>

pkgname=kde-gtk-config
pkgver=2.2.1
pkgrel=1
pkgdesc="GTK2 and GTK3 Configurator for KDE"
arch=('i686' 'x86_64')
url="https://projects.kde.org/kde-gtk-config"
license=('GPL3')
depends=('kdelibs')
makedepends=('cmake' 'automoc4' 'gtk2' 'gtk3')
optdepends=('gtk2: GTK+ v2 support'
	    'gtk3: GTK+ v3 support')
conflicts=('kde-gtk-config-git' 'chakra-gtk-config' 'chakra-gtk-config-git')
source=("http://download.kde.org/stable/$pkgname/$pkgver/src/$pkgname-$pkgver.tar.xz")
install=$pkgname.install
md5sums=('d155ed431d509e54a60383a70b700e1c')

build() {
  cd "$srcdir"
  mkdir build
  cd build
  cmake ../$pkgname-$pkgver \
    -DQT_QMAKE_EXECUTABLE=qmake-qt4 \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_INSTALL_PREFIX=/usr
  make
}

package(){
  cd "$srcdir/build"
  make DESTDIR="$pkgdir" install
}
