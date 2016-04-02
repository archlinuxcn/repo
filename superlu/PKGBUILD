# Contributor: Giuseppe Borzi <gborzi@ieee.org>
pkgname=superlu
pkgver=4.3
pkgrel=1
pkgdesc="Set of subroutines to solve a sparse linear system"
arch=('i686' 'x86_64')
url="http://crd.lbl.gov/~xiaoye/SuperLU/"
license=('custom')
depends=('gcc-libs' 'blas')
makedepends=('gcc-fortran' 'tcsh')
install=${pkgname}.install
source=(${url}${pkgname}_$pkgver.tar.gz ${url}License.txt
        ${url}superlu_ug.pdf)
md5sums=('b72c6309f25e9660133007b82621ba7c'
         'f78e2ac527dbb50f53766475a9c542bd'
         '0097d559fa73f8fc182ac05635537454')

build() {
  cd "$srcdir/SuperLU_$pkgver"

  mkdir shared static
  msg "Building shared library..."
  cd shared
  make -f ../SRC/Makefile VPATH=../SRC srcdir=../SRC CC=cc \
          CFLAGS="$CFLAGS -fPIC" FORTRAN=gfortran FFLAGS="$CFLAGS -fPIC" \
          PLAT="" BLASDEF="" BLASLIB="-lblas" CDEFS="-DAdd_" NOOPTS="-fPIC" \
          ARCH="echo" ARCHFLAGS="" RANLIB="echo" \
          SUPERLULIB=$srcdir/SuperLU_$pkgver/lib/lib$pkgname.a
  gcc -shared -Wl,-soname,lib$pkgname.so.4 -o ../lib/lib$pkgname.so.$pkgver \
      *.o -lblas -lm -lgfortran
  cd ../static
  msg "Building static library..."
  make -f ../SRC/Makefile VPATH=../SRC srcdir=../SRC CC=cc \
          CFLAGS="$CFLAGS" FORTRAN=gfortran FFLAGS="$CFLAGS" \
          PLAT="" BLASDEF="" BLASLIB="-lblas" CDEFS="-DAdd_" \
          ARCH="echo" ARCHFLAGS="" RANLIB="echo" \
          SUPERLULIB=$srcdir/SuperLU_$pkgver/lib/lib$pkgname.a
  ar cr ../lib/lib$pkgname.a *.o
}

check() {
  cd "$srcdir/SuperLU_$pkgver"

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
  cd "$srcdir/SuperLU_$pkgver"
  mkdir -p $pkgdir/usr/lib $pkgdir/usr/include/$pkgname \
           $pkgdir/usr/share/doc/$pkgname \
           $pkgdir/usr/share/licenses/$pkgname
  install -p -m644 $srcdir/SuperLU_$pkgver/lib/lib$pkgname.a $pkgdir/usr/lib
  install -p -m755 $srcdir/SuperLU_$pkgver/lib/lib$pkgname.so.$pkgver $pkgdir/usr/lib
  cd $pkgdir/usr/lib
  ln -s lib$pkgname.so.$pkgver lib$pkgname.so.4
  ln -s lib$pkgname.so.4 lib$pkgname.so
  install -m644 $srcdir/SuperLU_$pkgver/SRC/*.h $pkgdir/usr/include/$pkgname
  install -m644 $srcdir/superlu_ug.pdf $pkgdir/usr/share/doc/$pkgname/superlu_ug.pdf
  install -m644 $srcdir/SuperLU_$pkgver/README $pkgdir/usr/share/doc/$pkgname
  install -m644 $srcdir/License.txt $pkgdir/usr/share/licenses/$pkgname
}

# vim:set ts=2 sw=2 et:
