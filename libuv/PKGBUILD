# Maintainer: Massimiliano Torromeo <massimiliano.torromeo@gmail.com>

pkgname=libuv
pkgver=0.11.19
pkgrel=1
pkgdesc="A new platform layer for Node.JS"
arch=('i686' 'x86_64')
url="https://github.com/joyent/libuv"
license=('custom')
depends=('glibc')
source=("https://github.com/joyent/libuv/archive/v$pkgver.tar.gz")
options=(!libtool)

build() {
	cd "$srcdir/$pkgname-$pkgver"
	./autogen.sh
	./configure --prefix=/usr
	make
}

check() {
	cd "$srcdir/$pkgname-$pkgver"
	make check
}

package() {
	cd "$srcdir/$pkgname-$pkgver"

	make DESTDIR="$pkgdir" install

	install -Dm644 LICENSE \
		"$pkgdir/usr/share/licenses/$pkgname/LICENSE"
	install -Dm644 AUTHORS \
		"$pkgdir/usr/share/doc/$pkgname/AUTHORS"
	install -Dm644 README.md \
		"$pkgdir/usr/share/doc/$pkgname/README.md"
	install -Dm644 ChangeLog \
		"$pkgdir/usr/share/doc/$pkgname/ChangeLog"
}

sha256sums=('2d2d17be846d0fe459ad1b56f10eab1e6cdf9693f7d9dbd89bb2b0de3e24ef58')
