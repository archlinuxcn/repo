# Maintainer: Joey Dumont <joey.dumont@gmail.com>
# Contributor: Giuseppe Borzi <gborzi@ieee.org>
pkgname=superlu
pkgver=5.2.1
pkgrel=7
pkgdesc="Set of subroutines to solve a sparse linear system"
arch=('i686' 'x86_64')
url="https://github.com/xiaoyeli/superlu/"
license=('custom')
depends=('gcc-libs' 'blas')
makedepends=('gcc-fortran' 'tcsh')
install=${pkgname}.install
source=("${url}/archive/v${pkgver}.tar.gz")
sha512sums=('c5f9ca6055b6861dcc89e31c446c9f57a4e16333f9f24f109e8f375eded878005fa520ab39d2c1dd0ce12f289f9e251aef47da58c975bf5b1f09ca7539194e90')
options=('staticlibs')

build() {
  cd "$srcdir/$pkgname-$pkgver"
  cp MAKE_INC/make.linux make.inc
  mkdir -p shared static
  msg "Building shared library..."
  cd shared
  make -f ../SRC/Makefile VPATH=../SRC srcdir=../SRC CC=cc \
          CFLAGS="$CFLAGS -fPIC" FORTRAN=gfortran FFLAGS="$CFLAGS -fPIC" \
          PLAT="" BLASDEF="-DUSE_VENDOR_BLAS" BLASLIB="-lblas" CDEFS="-DAdd_" NOOPTS="-fPIC" \
          ARCH="echo" ARCHFLAGS="" RANLIB="echo" \
          SUPERLULIB=$srcdir/SuperLU_$pkgver/lib/lib$pkgname.a
  gcc -shared -Wl,-soname,lib$pkgname.so.4 -o ../lib/lib$pkgname.so.$pkgver \
      *.o -lblas -lm -lgfortran

cd ../static
  msg "Building static library..."
  make -f ../SRC/Makefile VPATH=../SRC srcdir=../SRC CC=cc \
          CFLAGS="$CFLAGS -fPIC" FORTRAN=gfortran FFLAGS="$CFLAGS -fPIC" \
          PLAT="" BLASDEF="" BLASLIB="-lblas" CDEFS="-DAdd_" NOOPTS="-fPIC" \
          ARCH="echo" ARCHFLAGS="" RANLIB="echo" \
          SUPERLULIB=$srcdir/SuperLU_$pkgver/lib/lib$pkgname.a
  ar cr ../lib/lib$pkgname.a *.o
}

check() {
  cd "$srcdir/$pkgname-$pkgver"

  msg "Testing library..."
  cd TESTING
  LS_COLORS="" make -j1 SUPERLULIB=../lib/libsuperlu.a BLASLIB=-lblas \
          CC=cc CFLAGS="-O2" LOADER="cc" LOADOPTS=""
  if [ "x`grep failed *.out`" != "x" ]; then
    msg 'Testing failed'
    return 1
  fi
}

package() {
  cd "$srcdir/$pkgname-$pkgver"
  mkdir -p $pkgdir/usr/lib $pkgdir/usr/include/$pkgname \
           $pkgdir/usr/share/doc/$pkgname \
           $pkgdir/usr/share/licenses/$pkgname
  install -p -m644 $srcdir/$pkgname-$pkgver/lib/lib$pkgname.a $pkgdir/usr/lib
  install -p -m755 $srcdir/$pkgname-$pkgver/lib/lib$pkgname.so.$pkgver $pkgdir/usr/lib
  cd $pkgdir/usr/lib
  ln -s lib$pkgname.so.$pkgver lib$pkgname.so.4
  ln -s lib$pkgname.so.4 lib$pkgname.so
  install -m644 $srcdir/$pkgname-$pkgver/SRC/*.h $pkgdir/usr/include/$pkgname
  install -m644 $srcdir/$pkgname-$pkgver/README $pkgdir/usr/share/doc/$pkgname
  install -m644 $srcdir/$pkgname-$pkgver/License.txt $pkgdir/usr/share/licenses/$pkgname
  install -m644 $srcdir/$pkgname-$pkgver/DOC/ug.pdf $pkgdir/usr/share/doc/$pkgname/ug.pdf
  
}

