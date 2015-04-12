# Maintainer: Jiachen Yang <farseerfc@gmail.com>
# Contributor: Evan Gates      <evan.gates@gmail.com>
#              Dag  Odenhall   <dag.odenhall@gmail.com>
#              Raphael Nestler
pkgname=lsw
pkgver=0.3
pkgrel=1
pkgdesc="List window names"
license=(MIT)
arch=(i686 x86_64)
url="http://tools.suckless.org/lsw"
depends=(libx11)
source=("http://dl.suckless.org/tools/$pkgname-$pkgver.tar.gz"
        "makefile.patch")

md5sums=('3ae42c41a7ceda8ddf6e0fbab0866f79'
         'ae850a6a044a11f01a73f56c2f1c5520')

build() {
	cd -- "$srcdir/$pkgname-$pkgver"
	sed -i "s/CFLAGS = /CFLAGS = ${CFLAGS} /" config.mk

	patch "$srcdir/$pkgname-$pkgver/Makefile" "$srcdir/makefile.patch"
	make X11INC=/usr/lib/X11 X11LIB=/usr/lib/X11
}

package(){
	cd -- "$srcdir/$pkgname-$pkgver"
	make PREFIX=/usr MANPREFIX=/usr/share/man DESTDIR="$pkgdir" install

	install -m644 -D LICENSE "$pkgdir/usr/share/licenses/$pkgname/COPYING"
}

