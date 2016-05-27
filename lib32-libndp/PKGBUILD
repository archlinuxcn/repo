# Maintainer: oi_wtf <brainpower at mailbox dot org>
# Original-Maintainer: Jan Alexander Steffens (heftig) <jan.steffens@gmail.com>

pkgname=lib32-libndp
_pkgname=libndp
pkgver=1.6
pkgrel=1
pkgdesc="Library for Neighbor Discovery Protocol"
arch=(i686 x86_64)
url="http://libndp.org/"
license=(LGPL2.1)
depends=(lib32-glibc)
source=($url/files/$_pkgname-$pkgver.tar.gz)
sha256sums=('0c7dfa84e013bd5e569ef2c6292a6f72cfaf14f4ff77a77425e52edc33ffac0e')

build() {
  cd $_pkgname-$pkgver
  export CC='gcc -m32'
  export CXX='g++ -m32'
  export PKG_CONFIG_PATH='/usr/lib32/pkgconfig'

  ./configure --prefix=/usr --sysconfdir=/etc --localstatedir=/var \
    --disable-static --libexecdir=/usr/lib --libdir=/usr/lib32
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
