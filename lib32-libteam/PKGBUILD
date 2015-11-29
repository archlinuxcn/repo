# Maintainer: oi_wtf <brainpower at mailbox dot org>

pkgname=lib32-libteam
_pkgname=libteam
pkgver=1.18
pkgrel=1
pkgdesc="Library for controlling team network device"
arch=(x86_64)
url="http://libteam.org/"
license=(LGPL2.1)
depends=(lib32-libnl lib32-libdaemon lib32-jansson lib32-libdbus) # lib32-zeromq)
source=($url/files/$_pkgname-$pkgver.tar.gz)
sha256sums=('9f1f7a830331f50a5d67365fba7c8ab8db677350f101420a12255152e6058737')

build() {
  cd $_pkgname-$pkgver

  export CC='gcc -m32'
  export CXX='g++ -m32'
  export PKG_CONFIG_PATH='/usr/lib32/pkgconfig'

  ./configure --prefix=/usr --sysconfdir=/etc --localstatedir=/var \
    --disable-static --libdir=/usr/lib32 --libexecdir=/usr/lib \
    --disable-zmq # disabled till I get lib32-zeromq to build
  make
}

check() {
  cd $_pkgname-$pkgver
  make check
}

package() {
  cd $_pkgname-$pkgver
  make DESTDIR="$pkgdir" install

  # lib32 cleanup
  rm -rf "$pkgdir"/usr/{bin,lib,include,share} "$pkgdir/etc"
}
