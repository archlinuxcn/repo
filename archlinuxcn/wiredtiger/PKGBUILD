# Maintainer: Christoph Bayer <chrbayer@criby.de>
# Contributor: Stefan Husmann <stefan-husmann@t-online.de>

pkgname=wiredtiger
pkgver=3.1.0.20190207
_commit=bedf230af338faa9b9ba8741b9a2e5f36353e2f0
pkgrel=1
pkgdesc="High performance, scalable, production quality, NoSQL, Open Source extensible platform for data management"
arch=('x86_64')
url="http://source.wiredtiger.com/"
license=('GPL')
depends=('snappy' 'lz4' 'zlib' 'gperftools')
source=("$pkgname-$_commit.tar.gz::https://github.com/wiredtiger/wiredtiger/archive/$_commit.tar.gz")
sha512sums=('57153f1ea8b7278fcd724d5aa910bf0d5dabebeb8754f5eabd49be9cae8cb83b266a962224fc2784b15d7f1d22e57a7ff2202b84838b147879401a24e30e78af')

prepare() {
  mv wiredtiger-{$_commit,$pkgver}
}

build() {
  cd wiredtiger-$pkgver

  ./autogen.sh
  ./configure --prefix=/usr \
              --enable-leveldb \
              --enable-lz4 \
              --enable-tcmalloc \
              --enable-verbose \
              --with-builtins=snappy,zlib
  make
}

check() {
  cd wiredtiger-$pkgver
  make test
}

package() {
  cd wiredtiger-$pkgver
  make DESTDIR="$pkgdir" install
}
