# Maintainer: Felix Yan <felixonmars@archlinux.org>
# Contributor: Evangelos Foutras <evangelos@foutrelis.com>

pkgname=php53-memcached
pkgver=2.2.0
pkgrel=1
pkgdesc="PHP 5.3 extension for interfacing with memcached via libmemcached library"
arch=('i686' 'x86_64')
url="http://pecl.php.net/package/memcached"
license=('PHP')
depends=('php53' 'libmemcached')
conflicts=('php-memcached')
provides=('php-memcached')
backup=('etc/php/conf.d/memcached.ini')
source=(http://pecl.php.net/get/memcached-$pkgver.tgz)
sha256sums=('17b9600f6d4c807f23a3f5c45fcd8775ca2e61d6eda70370af2bef4c6e159f58')

build() {
  cd "$srcdir/memcached-$pkgver"

  phpize
  ./configure --prefix=/usr
  make
}

package() {
  cd "$srcdir/memcached-$pkgver"

  make INSTALL_ROOT="$pkgdir" install

  install -d "$pkgdir/etc/php/conf.d"
  echo ';extension=memcached.so' >"$pkgdir/etc/php/conf.d/memcached.ini"
}

# vim:set ts=2 sw=2 et:
