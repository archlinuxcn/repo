# Maintainer: Martin Hundebøll <martin@hundeboll.net>
pkgname=tio
pkgver=1.34
pkgrel=1
pkgdesc="The simple TTY terminal I/O application"
url="http://tio.github.io/"
arch=('x86_64' 'i686')
license=('GPLv2')
depends=('glibc')
makedepends=('meson')
source=("https://github.com/tio/tio/releases/download/v$pkgver/$pkgname-$pkgver.tar.xz")
sha256sums=('ec5f659fcab6ebab5ff3aa8737d67809441e6f69f62fc8f38ab11986908254e1')

build() {
  cd "$srcdir/$pkgname-$pkgver"
  meson --prefix=/usr --buildtype=plain . build
  meson compile -C build
}

package() {
  cd "$srcdir/$pkgname-$pkgver"
  meson install -C build --destdir "$pkgdir"
}

# vim:set ts=2 sw=2 et:
