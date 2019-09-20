# Maintainer: László Várady <laszlo.varady93@gmail.com>

pkgname=rocksdb
pkgver=6.2.4
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
sha256sums=('7f34d1b55501f5273d11cd064bd34aef87c51ff114452968b86457f06cdb8ced')

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
