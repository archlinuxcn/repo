# Maintainer:  Bruce Zhang
# Contributor: 吕海涛 <aur@lvht.net>
pkgname=php-swoole
_extname=swoole
_reponame=swoole-src
pkgver=4.6.3
pkgrel=1
pkgdesc="Event-driven asynchronous and concurrent networking engine with high performance for PHP."
url="https://github.com/swoole/swoole-src"
arch=('x86_64')
license=('Apache')
depends=('nghttp2' 'php')
provides=('php-swoole')
backup=("etc/php/conf.d/$_extname.ini")
source=("$pkgname-$pkgver.src.tar.gz::https://github.com/swoole/$_reponame/archive/v$pkgver.tar.gz")
sha256sums=('e93fee47c66cce13852d52e074a211d352f05f5c2644b280f653242d87c6159e')
install=php-swoole.install

build() {
  cd "$srcdir/$_reponame-$pkgver"
	phpize
	./configure --enable-http2 --enable-openssl
	make
}

package() {
  cd "$srcdir/$_reponame-$pkgver"
	install -m0755 -d "$pkgdir/etc/php/conf.d/"
	install -m0644 -D "LICENSE" "${pkgdir}/usr/share/licenses/$pkgname/LICENSE"
	echo ";extension=$_extname.so" > "$pkgdir/etc/php/conf.d/$_extname.ini"
	chmod 0644 "$pkgdir/etc/php/conf.d/$_extname.ini"
	install -m0755 -D ".libs/$_extname.so" "$pkgdir$(php-config --extension-dir)/$_extname.so"
}
