# Maintainer: Behnam Momeni <sbmomeni [at the] gmail [dot] com>
# Contributor: Andrew Sun <adsun701 at gmail dot com>
# Contributor: orumin <dev at orum.in>

pkgbase=lib32-lapack
_basename=lapack
pkgname=('lib32-lapack' 'lib32-blas' 'lib32-cblas' 'lib32-lapacke')
pkgver=3.11.0
pkgrel=1
url="https://www.netlib.org/lapack"
pkgdesc="Linear Algebra PACKage (32-bit)"
makedepends=('gcc-fortran' 'lib32-gcc-libs' 'cmake' 'python')
arch=('x86_64')
license=("custom")
source=($_basename-$pkgver.tar.gz::"https://github.com/Reference-LAPACK/lapack/archive/v$pkgver.tar.gz")
sha256sums=('4b9ba79bfd4921ca820e83979db76ab3363155709444a787979e81c22285ffa9')

build() {
  mkdir -p ${srcdir}/build
  cd ${srcdir}/build

  export FFLAGS='-m32'
  export CC='gcc -m32'
  export CXX='g++ -m32'
  export PKG_CONFIG_PATH='/usr/lib32/pkgconfig'

  cmake ../${_basename}-${pkgver} \
    -DCMAKE_SKIP_RPATH=ON \
    -DBUILD_SHARED_LIBS=ON \
    -DBUILD_TESTING=OFF \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DCMAKE_INSTALL_LIBDIR=lib32 \
    -DCMAKE_Fortran_COMPILER=gfortran \
    -DLAPACKE_WITH_TMG=ON \
    -DCBLAS=ON \
    -DBUILD_DEPRECATED=ON
  make
}

package_lib32-lapack() {
  depends=('lib32-blas' 'lapack')
  
  cd build
  make DESTDIR="$pkgdir" install

  rm -r "$pkgdir"/usr/lib32/{libblas.*,libcblas.*,liblapacke.*}
  rm -r "$pkgdir"/usr/lib32/pkgconfig/{blas.*,cblas.*,lapacke.*}
  rm -r "$pkgdir"/usr/lib32/cmake/{cblas*,lapacke*}
  rm -r "$pkgdir"/usr/include
}

package_lib32-blas() {
  pkgdesc="Basic Linear Algebra Subprograms (32-bit)"
  depends=('lib32-gcc-libs' 'blas')

  cd build/BLAS
  make DESTDIR="$pkgdir" install
  
}

package_lib32-cblas() {
  pkgdesc="C interface to BLAS (32-bit)"
  depends=('lib32-blas' 'cblas')

  cd build/CBLAS
  make DESTDIR="$pkgdir" install
  rm -r "$pkgdir"/usr/include
}

package_lib32-lapacke() {
  pkgdesc="C interface to LAPACK (32-bit)"
  depends=('lib32-lapack' 'lapacke')

  cd build/LAPACKE
  make DESTDIR="$pkgdir" install
  rm -r "$pkgdir"/usr/include
}

