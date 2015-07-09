# Maintainer: farseerfc <farseerfc@gmail.com>
# Contributor: nylocx <just18@gmx.de>
# Contributor: Llumex03 <l.lumex03@gmail.com>
# Original uploader in CCR: FranzMari
# Original uploader in AUR: á¸¶á¸·umex03
# Fixes in AUR by: ogarcia

pkgname=libqtelegram-ae
_pkgname=libqtelegram-aseman-edition
epoch=2
pkgver=0.5.0
pkgrel=1
pkgdesc="Telegram library written in Qt based on telegram-cli code"
arch=('x86_64' 'i686')
license=('GPL3')
url=("https://launchpad.net/libqtelegram")
depends=('qt5-base' 'qt5-multimedia')
makedepends=('cmake')
source=("https://github.com/Aseman-Land/libqtelegram-aseman-edition/archive/v$pkgver-stable.tar.gz")
sha256sums=('de3126af8369d0db36e2aa9fcd7a914c23fe4c819d0bbd8a0b33af97cc237829')

prepare() {
  cd $_pkgname-$pkgver-stable
  sed -i 's#target.path = $$PREFIX/lib/$$LIB_PATH#target.path = $$PREFIX/lib#' libqtelegram-ae.pro
  mkdir -p build
}

build() {
  cd $_pkgname-$pkgver-stable/build
  qmake-qt5 -r .. PREFIX=/usr
  make
}

package() {
  cd $_pkgname-$pkgver-stable/build
  make INSTALL_ROOT="$pkgdir" install
}
