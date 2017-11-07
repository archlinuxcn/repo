# Contributor: Lukas Jirkovsky <l.jirkovsky@gmail.com>
# Maintainer: gucong <gucong43216@gmail.com>

pkgname=embree-isa
pkgver=2.17.0
pkgrel=1
pkgdesc="A collection of high-performance ray tracing kernels (with build-time ISA detection)"
arch=('x86_64')
url="https://embree.github.io/"
license=('Apache')
depends=('intel-tbb')
provides=('embree')
conflicts=('embree')
makedepends=('cmake' 'ispc' 'freeglut' 'libxmu' 'openexr')
source=("embree-${pkgver}.tar.gz::https://github.com/embree/embree/archive/v${pkgver}.tar.gz")
md5sums=('3ea7a72546baee497ae8098bc12f3de6')

build() {
  cd "$srcdir/embree-$pkgver"

  MAX_ISA="SSE2"
  cat /proc/cpuinfo | grep sse3 > /dev/null && MAX_ISA="SSE3"
  cat /proc/cpuinfo | grep sse4_1 > /dev/null && MAX_ISA="SSE4.1"
  cat /proc/cpuinfo | grep sse4_2 > /dev/null && MAX_ISA="SSE4.2"
  cat /proc/cpuinfo | grep avx > /dev/null && MAX_ISA="AVX"
  cat /proc/cpuinfo | grep avx2 > /dev/null && MAX_ISA="AVX2"
  # ICC required for avx512 ?

  echo MAX_ISA:  $MAX_ISA

  cmake . \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DCMAKE_INSTALL_LIBDIR=lib \
    -DCMAKE_BUILD_TYPE=Release \
    -DEMBREE_TUTORIALS=OFF \
    -DEMBREE_MAX_ISA="$MAX_ISA"
  make
}

package() {
  cd "$srcdir/embree-$pkgver"
  make DESTDIR="$pkgdir" install
}

