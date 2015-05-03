# Original uploader in CCR: FranzMari 
# Original uploader in AUR: á¸¶á¸·umex03
# Fixes in AUR by: ogarcia

pkgname=libqtelegram-bzr
_pkgname=libqtelegram
pkgver=82
pkgrel=1
pkgdesc="Telegram library written in Qt based on telegram-cli code"
arch=('x86_64' 'x64')
license=('GPL3')
url=("https://launchpad.net/libqtelegram")
depends=('qt5-base' 'openssl' 'libmediainfo' 'thumbnailer-bzr' 'qt5-multimedia')
makedepends=('cmake' 'bzr')
source=(bzr+lp:libqtelegram)
md5sums=('SKIP')
 
pkgver() {
    cd $_pkgname
    bzr revno
}
 
prepare() {
  cd $_pkgname
  mkdir -p build
}
 
build() {
  cd $_pkgname/build
 
  cmake .. \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DCMAKE_INSTALL_LIBDIR=lib \
    -DUSE_QT4=OFF
  make
} 
 
package() {
  cd $_pkgname/build
  make DESTDIR="$pkgdir" install
  install -m644 $srcdir/libqtelegram/lib/secret/secretchatmessage.h $pkgdir/usr/include/libqtelegram/secret/
  install -m644 $srcdir/libqtelegram/lib/secret/decryptedmessagebuilder.h $pkgdir/usr/include/libqtelegram/secret/
}