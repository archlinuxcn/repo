# Maintainer: Brian Bidlock <bidulock@openss7.org>

pkgname=libpcl
pkgver=1.12
pkgrel=4
pkgdesc='The Portable Coroutine Library (PCL) implements the low level functionality for coroutines'
license=(GPL2)
url='http://xmailserver.org/libpcl.html'
arch=('x86_64' 'i686')
depends=(glibc)
source=(http://xmailserver.org/pcl-$pkgver.tar.gz)
sha1sums=('a206c8fb5a96e65005f414ac46aeccd4b3603c8d')

build() {
  cd pcl-$pkgver
  ./configure --prefix=/usr
  make
}

package() {
  cd pcl-$pkgver
  make DESTDIR="$pkgdir" install
}
