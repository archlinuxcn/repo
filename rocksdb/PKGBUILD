pkgname=rocksdb
pkgver=5.4.6
pkgrel=1
pkgdesc='Embedded key-value store for fast storage'
arch=(i686 x86_64)
url='http://rocksdb.org'
license=(BSD)
depends=(
	'bzip2'
	'gcc-libs'
	'lz4'
	'snappy'
	'zlib'
	)
makedepends=('gcc' 'make')
checkdepends=(python2)
source=(https://github.com/facebook/rocksdb/archive/rocksdb-$pkgver.zip)
sha256sums=('b130935c3c59a3cdc0193a87f985d559b7f6bd26548fe039293172227ec8ae5a')

prepare() {
  cd rocksdb-rocksdb-$pkgver
  sed -e 's/\bpython\b/python2/' -i Makefile
  if [ "$CARCH"  == "armv6h" ]; then
    sed -e 's/-momit-leaf-frame-pointer//' -i Makefile
  fi
}

build() {
  cd rocksdb-rocksdb-$pkgver
  make shared_lib -j4
}

#check() {
#  cd rocksdb-rocksdb-$pkgver
#  make check
#}

package() {
  cd rocksdb-rocksdb-$pkgver
  install -d "$pkgdir"/usr/include
  cp -r include/rocksdb "$pkgdir"/usr/include
  install -m755 -D librocksdb.so "$pkgdir"/usr/lib/librocksdb.so
  install -D -m644 LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
