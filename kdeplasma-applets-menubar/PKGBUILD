# Contributor: Andrea Scarpino <andrea@archlinux.org>
# Contributor: György Balló <ballogy@freestart.hu>
# Maintainer: der_FeniX <derfenix@gmail.com>

pkgname=kdeplasma-applets-menubar
pkgver=0.2.0
pkgrel=4
pkgdesc="A Plasma widget to display menubar of application windows"
arch=('i686' 'x86_64')
url='https://launchpad.net/plasma-widget-menubar'
license=('GPL')
depends=('kdelibs' 'qjson')
makedepends=('cmake' 'automoc4')
conflicts=('plasma-widget-menubar')
replaces=('plasma-widget-menubar')
optdepends=('gtk2-appmenu: support for GTK+ 2 apps'
            'gtk3-appmenu: support for GTK+ 3 apps'
            'appmenu-qt: support for Qt apps'
            'libreoffice-extension-menubar: support for LibreOffice')
source=("https://launchpad.net/plasma-widget-menubar/trunk/$pkgver/+download/plasma-widget-menubar-$pkgver.tar.bz2"{,.sig})
md5sums=('68852bf8612b9a1336fc2485b268445e'
         '15c21acc6b01655cc783b28bae0f7e8f')

build() {
  mkdir build
  cd build
  cmake ../plasma-widget-menubar-${pkgver} \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_INSTALL_PREFIX=$(kde4-config --prefix) \
    -DQT_QMAKE_EXECUTABLE=qmake-qt4
  make
}

package() {
  cd build
  make DESTDIR="${pkgdir}" install
}
