# Maintainer:  Bruce Zhang
# Contributor: 吕海涛 <aur@lvht.net>
pkgname=php-swoole
_extname=swoole
_reponame=swoole-src
pkgver=4.4.4
pkgrel=1
pkgdesc="Event-driven asynchronous and concurrent networking engine with high performance for PHP."
url="https://github.com/swoole/swoole-src"
arch=('x86_64')
license=('Apache')
depends=('nghttp2' 'php')
provides=('php-swoole')
backup=("etc/php/conf.d/$_extname.ini")
source=("$pkgname-$pkgver.src.tar.gz::https://github.com/swoole/$_reponame/archive/v$pkgver.tar.gz")
sha256sums=('5b3ca66c80e5eeacf2a7a39023ae10fe758f580d99f58478b2ab2f9b57cf1dd1')
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
