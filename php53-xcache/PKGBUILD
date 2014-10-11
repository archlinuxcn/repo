# Maintainer: Felix Yan <felixonmars@archlinux.org>
# Contributor: Pierre Schmitz <pierre@archlinux.de>

pkgname=php53-xcache
pkgver=3.2.0
pkgrel=1
arch=('i686' 'x86_64')
pkgdesc='A PHP 5.3 opcode cacher'
url='http://xcache.lighttpd.net/'
depends=('php53')
license=('custom')
source=("http://xcache.lighttpd.net/pub/Releases/${pkgver}/xcache-${pkgver}.tar.bz2"
        'xcache.ini')
backup=('etc/php/conf.d/xcache.ini')
md5sums=('3655bd20483dc23d24f87f9dc924a62e'
         '8fd9ce537ada9463c4b0c042243158c0')

build() {
	cd $srcdir/xcache-$pkgver
	phpize
	./configure --prefix=/usr
	make
}

check() {
	cd $srcdir/xcache-$pkgver
	export NO_INTERACTION=1
	make test
	echo
}

package() {
	cd $srcdir/xcache-$pkgver
	make INSTALL_ROOT=$pkgdir install

	install -Dm644 $srcdir/xcache.ini $pkgdir/etc/php/conf.d/xcache.ini

	install -dm755 $pkgdir/usr/share/webapps/php53-xcache
	cp -r htdocs/* $pkgdir/usr/share/webapps/php53-xcache/

	install -Dm644 COPYING $pkgdir/usr/share/licenses/php53-xcache/COPYING
}
