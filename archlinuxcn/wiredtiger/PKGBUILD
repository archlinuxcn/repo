# Maintainer: Christoph Bayer <chrbayer@criby.de>
# Maintainer: James P. Harvey <jamespharvey20 at gmail dot com>
# Contributor: Stefan Husmann <stefan-husmann@t-online.de>
# Contributor: Fredy García <frealgagu at gmail dot com>

pkgname=wiredtiger
pkgver=3.1.1.20190401
_commit=4f2ed4c4cb122342711ce82d553482124501fcd4
pkgrel=1
pkgdesc="High performance, scalable, production quality, NoSQL, Open Source extensible platform for data management"
arch=('x86_64')
url="http://source.wiredtiger.com/"
license=('GPL')
depends=('snappy' 'lz4' 'zlib' 'gperftools')
makedepends=('aspell-en')
source=("$pkgname-$_commit.tar.gz::https://github.com/wiredtiger/wiredtiger/archive/$_commit.tar.gz")
sha512sums=('3917dd47231c9e6f5220bc472249ea1e9b5ba081e14d8052ebd64e9c7d21090b0754be4f5793513063122dd1ff0e51366761d749bb25e04372fce25178de4509')

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
