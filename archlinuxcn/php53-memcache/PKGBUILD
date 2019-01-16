# Maintainer: Felix Yan <felixonmars@archlinux.org>
# Contributor: Evangelos Foutras <evangelos@foutrelis.com>

pkgname=php53-memcache
pkgver=3.0.8
_commit=fdbd46bbc6f53ed6e024521895e142cbfc9b3340
pkgrel=3
pkgdesc="Memcache module for PHP 5.3"
arch=('i686' 'x86_64')
url="http://pecl.php.net/package/memcache"
license=('PHP')
depends=('php53')
makedepends=('git')
backup=('etc/php53/conf.d/memcache.ini')
install=php-memcache.install
source=("git+https://github.com/websupport-sk/pecl-memcache.git#commit=$_commit")
sha256sums=('SKIP')

build() {
  cd "$srcdir/pecl-memcache"

  phpize53
  ./configure --prefix=/usr --sysconfdir=/etc/php53 --with-php-config=/usr/bin/php-config53
  make
}

package() {
  cd "$srcdir/pecl-memcache"

  make INSTALL_ROOT="$pkgdir" install
  echo ';extension=memcache.so' >memcache.ini
  install -Dm644 memcache.ini "$pkgdir/etc/php53/conf.d/memcache.ini"
}

# vim:set ts=2 sw=2 et:
