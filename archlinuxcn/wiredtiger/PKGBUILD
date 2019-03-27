# Maintainer: Christoph Bayer <chrbayer@criby.de>
# Maintainer: James P. Harvey <jamespharvey20 at gmail dot com>
# Maintainer: Fredy García <frealgagu at gmail dot com>
# Contributor: Stefan Husmann <stefan-husmann@t-online.de>

pkgname=wiredtiger
pkgver=3.1.1.20190314
_commit=db5942dc1dc27f35f334ff3fb4d103b0cceb7968
pkgrel=3
pkgdesc="High performance, scalable, production quality, NoSQL, Open Source extensible platform for data management"
arch=('x86_64')
url="http://source.wiredtiger.com/"
license=('GPL')
depends=('snappy' 'lz4' 'zlib' 'gperftools')
makedepends=('aspell-en')
source=("$pkgname-$_commit.tar.gz::https://github.com/wiredtiger/wiredtiger/archive/$_commit.tar.gz")
sha512sums=('fec8597eb6a48dc49f1fb7f3b0de854759e29024c0688db2aa7ab7fed48d1ce13b5bc4bcc283623fbbfe1b2a1c17f416be366a9a894b2cf1281490e28b37f76c')

prepare() {
  mv wiredtiger-{$_commit,$pkgver}
  sed -i 's/print\(.*\)$/print(\1)/' ${srcdir}/wiredtiger-${pkgver}/dist/wtperf_config.py
  sed -i 's/\\n/^^/g' ${srcdir}/wiredtiger-${pkgver}/src/docs/Doxyfile
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
