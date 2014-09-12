# Maintainer: Antonio Rojas <nqn1976 @ gmail.com>
# Contributor: Andrea Scarpino <andrea@archlinux.org>

pkgname=plasmate
pkgver=1.0
pkgrel=1
pkgdesc="A plasma add-on creation tool"
arch=('i686' 'x86_64')
url="http://www.kde.org/"
license=('GPL')
depends=('kdepimlibs')
makedepends=('cmake' 'automoc4' 'boost')
optdepends=('git: to use the TimeLine feature')
source=("http://download.kde.org/stable/plasmate/$pkgver/src/$pkgname-$pkgver.tar.gz")
install="$pkgname.install"
md5sums=('342e5cdc36e4e1a524b258ca32f1acad')

build() {
  cd $pkgname-$pkgver
  mkdir build
  cd build
  cmake .. -DCMAKE_INSTALL_PREFIX=`kde4-config --prefix` -DCMAKE_BUILD_TYPE=Release -DQT_QMAKE_EXECUTABLE=qmake-qt4
  make
}

package() {
  cd $pkgname-$pkgver/build
  make DESTDIR=${pkgdir} install
}
