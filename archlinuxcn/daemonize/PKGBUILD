# Maintainer: Erik Westrup <erik.westrup@gmail.com>
pkgname=daemonize
pkgver=1.7.7
pkgrel=1
pkgdesc="Run a program as a Unix daemon"
arch=(i686 x86_64 armv7h)
url="http://bmc.github.com/daemonize/"
license=('BSD')
depends=(glibc)
provides=(daemonize)
conflicts=(daemonize-git)
makedepends=(python-markdown)
source=("$pkgname-$pkgver.tar.gz::https://github.com/bmc/$pkgname/tarball/release-$pkgver")
md5sums=('84877ef65f01ccf8cd5da1bf4045883e')

build() {
  local _dirname=$(tar tf "$srcdir/$pkgname-$pkgver.tar.gz" | sed 1q);
  cd "$srcdir/$_dirname"
  sed -i -e 's|/sbin|/bin|' Makefile.in
  ./configure --prefix=/usr
  make
}

package() {
  local _dirname=$(tar tf "$srcdir/$pkgname-$pkgver.tar.gz" | sed 1q);
  cd "$srcdir/$_dirname"
  make DESTDIR="$pkgdir/" install
  install -dm755 "$pkgdir/usr/share/doc/$pkgname"
  install -m644 CHANGELOG.md README.md "$pkgdir/usr/share/doc/$pkgname"
  install -Dm644 LICENSE.md "$pkgdir/usr/share/licenses/$pkgname/LICENSE.md"
}

# vim:set ts=2 sw=2 et:
