# Maintainer: Darshit Shah <darnir@gmail.com>
# Contributor: speps <speps at aur dot archlinux dot org>

pkgname=libmetalink
pkgver=0.1.3
pkgrel=1
pkgdesc="A Metalink library written in C language."
arch=(i686 x86_64)
url="https://launchpad.net/libmetalink/"
license=('custom:MIT')
depends=('expat')
makepdepends=('libtool')
options=('!libtool')
source=("${url}trunk/$pkgname-$pkgver/+download/$pkgname-$pkgver.tar.bz2")
md5sums=('292f290d55ab76a68759483c10f0b110')

build() {
  cd "$srcdir/$pkgname-$pkgver"
  ./configure --prefix=/usr \
              --enable-static=no
  make
}

package() {
  cd "$srcdir/$pkgname-$pkgver"
  make DESTDIR="$pkgdir/" install

  # license
  install -Dm644 COPYING \
    "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}

# vim:set ts=2 sw=2 et:
