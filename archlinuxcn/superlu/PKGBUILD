# Maintainer: Joey Dumont <joey.dumont@gmail.com>
# Contributor: Giuseppe Borzi <gborzi@ieee.org>
# Contributor: Stefan Paquay <stefanpaquay@gmail.com>
pkgname=superlu
pkgver=5.2.1
pkgrel=9
pkgdesc="Set of subroutines to solve a sparse linear system"
arch=('i686' 'x86_64')
url="https://github.com/xiaoyeli/superlu/"
license=('custom')
depends=('gcc-libs' 'blas')
makedepends=('gcc-fortran' 'tcsh' 'cmake')
install=${pkgname}.install
source=("${url}archive/v${pkgver}.tar.gz")
sha512sums=('c5f9ca6055b6861dcc89e31c446c9f57a4e16333f9f24f109e8f375eded878005fa520ab39d2c1dd0ce12f289f9e251aef47da58c975bf5b1f09ca7539194e90')
options=('staticlibs')

build() {  cd "$srcdir/$pkgname-$pkgver"
  mkdir -p build-shared build-static

  msg "Building shared library..."
  cd build-shared
  cmake -DCMAKE_BUILD_TYPE=Release \
        -Denable_blaslib=Off \
        -DBUILD_SHARED_LIBS=True \
	-DCMAKE_C_FLAGS="-fPIC" \
	-DCMAKE_Fortran_FLAGS="-fPIC" \
	-DCMAKE_EXE_LINKER_FLAGS="-shared" \
	../
  make
	
  msg "Building static library..."
  cd ../build-static
  cmake -DCMAKE_BUILD_TYPE=Release \
        -Denable_blaslib=OFF \
        -DBUILD_SHARED_LIBS=False \
	-DCMAKE_C_FLAGS="-fPIC" \
	-DCMAKE_Fortran_FLAGS="-fPIC" \
	../
  make
}

check() {
  cd "$srcdir/$pkgname-$pkgver"

  msg "Testing shared library..."
  cd build-shared
  make test

  msg "Testing static library.."
  cd ../build-static
  make test
}

package() {
  cd "$srcdir/$pkgname-$pkgver"
  mkdir -p $pkgdir/usr/lib $pkgdir/usr/include/$pkgname \
           $pkgdir/usr/share/doc/$pkgname \
           $pkgdir/usr/share/licenses/$pkgname
  install -p -m644 $srcdir/$pkgname-$pkgver/build-static/SRC/lib$pkgname.a $pkgdir/usr/lib
  install -p -m755 $srcdir/$pkgname-$pkgver/build-shared/SRC/lib$pkgname.so.$pkgver $pkgdir/usr/lib
  cd $pkgdir/usr/lib
  ln -s lib$pkgname.so.$pkgver lib$pkgname.so.4
  ln -s lib$pkgname.so.4 lib$pkgname.so
  install -m644 $srcdir/$pkgname-$pkgver/SRC/*.h $pkgdir/usr/include/$pkgname
  install -m644 $srcdir/$pkgname-$pkgver/README $pkgdir/usr/share/doc/$pkgname
  install -m644 $srcdir/$pkgname-$pkgver/License.txt $pkgdir/usr/share/licenses/$pkgname
  install -m644 $srcdir/$pkgname-$pkgver/DOC/ug.pdf $pkgdir/usr/share/doc/$pkgname/ug.pdf
  
}

