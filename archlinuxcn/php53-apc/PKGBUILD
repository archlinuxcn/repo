# Maintainer: Felix Yan <felixonmars@archlinux.org>
# Contributor: Pierre Schmitz <pierre at archlinux.de>

pkgname=php53-apc
pkgver=3.1.13
pkgrel=1
arch=('i686' 'x86_64')
pkgdesc='A free, open, and robust framework for caching and optimizing PHP intermediate code'
url='http://pecl.php.net/package/APC'
depends=('php53')
license=('PHP')
source=("http://pecl.php.net/get/APC-${pkgver}.tgz")
backup=('etc/php/conf.d/apc.ini')
md5sums=('c9e47002e3a67ebde3a6f81437c7b6e0')

build() {
  cd "$srcdir/APC-$pkgver"
  phpize
  ./configure --prefix=/usr
  make
}

# check() {
#   cd "$srcdir/APC-$pkgver"
#   make test
# }

package() {
  cd "$srcdir/APC-$pkgver"
  make INSTALL_ROOT="$pkgdir" install
  echo ';extension=apc.so' > apc.ini
  install -D -m644 apc.ini "$pkgdir/etc/php/conf.d/apc.ini"
  install -D -m644 apc.php "$pkgdir/usr/share/php53-apc/apc.php"
  install -D -m644 INSTALL "$pkgdir/usr/share/doc/php53-apc/install.txt"
}
