# Maintainer: farseerfc <farseerfc@gmail.com>
# Contributor: nylocx <just18@gmx.de>
# Contributor: Llumex03 <l.lumex03@gmail.com>
# Original uploader in CCR: FranzMari
# Original uploader in AUR: á¸¶á¸·umex03
# Fixes in AUR by: ogarcia

pkgname=libqtelegram-ae
_pkgname=libqtelegram-aseman-edition
epoch=2
pkgver=6.0
pkgrel=3
pkgdesc="Telegram library written in Qt based on telegram-cli code"
arch=('x86_64' 'i686')
license=('GPL3')
url=("https://launchpad.net/libqtelegram")
depends=('qt5-base>=5.5' 'qt5-multimedia')
makedepends=('cmake')
source=("https://github.com/Aseman-Land/libqtelegram-aseman-edition/archive/v$pkgver.tar.gz")
sha256sums=('5406ebee3e69aefa397e0edab5cc084f46e46e1b917a22868da38d4e83034dbb')

prepare() {
  cd $_pkgname-$pkgver
  mkdir -p build
}

build() {
  cd $_pkgname-$pkgver/build
  qmake-qt5 -r .. PREFIX=/usr INSTALL_LIBS_PREFIX=/usr/lib INSTALL_HEADERS_PREFIX=/usr/include
  make
}

package() {
  cd $_pkgname-$pkgver/build
  make INSTALL_ROOT="$pkgdir" install
}
