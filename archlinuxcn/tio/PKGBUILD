# Maintainer: Martin Hundebøll <martin@hundeboll.net>
pkgname=tio
pkgver=1.32
pkgrel=1
pkgdesc="The simple TTY terminal I/O application"
url="http://tio.github.io/"
arch=('x86_64' 'i686')
license=('GPLv2')
source=("https://github.com/tio/tio/releases/download/v$pkgver/$pkgname-$pkgver.tar.xz")
sha256sums=('a8f5ed6994cacb96780baa416b19e5a6d7d67e8c162a8ea4fd9eccd64984ae44')

build() {
  cd "$srcdir/$pkgname-$pkgver"
  ./configure --prefix=/usr
  make
}

package() {
  cd "$srcdir/$pkgname-$pkgver"
  make DESTDIR="$pkgdir" install
}

# vim:set ts=2 sw=2 et:
