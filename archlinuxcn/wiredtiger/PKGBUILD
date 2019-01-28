# Maintainer: Felix Yan <felixonmars@archlinux.org>
# Contributor: Stefan Husmann <stefan-husmann@t-online.de>

pkgname=wiredtiger
pkgver=3.1.0.20181203
_commit=b51da4ed903efd9daf4b9c04385f01bbb8d37d7d
pkgrel=1
pkgdesc="High performance, scalable, production quality, NoSQL, Open Source extensible platform for data management"
arch=('x86_64')
url="http://source.wiredtiger.com/"
license=('GPL')
depends=('snappy' 'lz4' 'zlib' 'gperftools')
source=("$pkgname-$_commit.tar.gz::https://github.com/wiredtiger/wiredtiger/archive/$_commit.tar.gz")
sha512sums=('af935628a7149924e0cd89b5f82054acd2cca58d4814794693de83d79ba28612b74d186d5d49e761d8a428408aad36cdfcb76aaf6d9c8ae9351e67535b5175ed')

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
