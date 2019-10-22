# Maintainer: László Várady <laszlo.varady93@gmail.com>

pkgname=rocksdb
pkgver=6.3.6
pkgrel=1
pkgdesc='Embedded key-value store for fast storage'
arch=('x86_64')
url="https://rocksdb.org/"
license=('GPL2' 'Apache')
depends=('bzip2' 'gcc-libs' 'gflags' 'jemalloc' 'lz4' 'snappy' 'zlib' 'zstd')
makedepends=('cmake')
#checkdepends=('python2')
conflicts=('rocksdb-lite' 'rocksdb-release')
source=("https://github.com/facebook/rocksdb/archive/v$pkgver.tar.gz")
sha256sums=('9878beb4e9b74a5f0d9500772235a39066fd019ba7af9ae6afe483ca713e3c7c')

build() {
  cd "$pkgname-$pkgver"
  cmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=/usr -DCMAKE_INSTALL_LIBDIR=lib \
        -DWITH_BZ2=ON -DWITH_LZ4=ON -DWITH_SNAPPY=ON -DWITH_ZLIB=ON -DWITH_ZSTD=ON \
        -DUSE_RTTI=ON -DWITH_JEMALLOC=ON -DWITH_TESTS=OFF -DFAIL_ON_WARNINGS=OFF -S . -B build
  cmake --build build
}

check() {
  cd "$pkgname-$pkgver"
  # cmake --build build --target test
}

package() {
  cd "$pkgname-$pkgver"
  cmake --build build --target install -- DESTDIR="$pkgdir/"
}
