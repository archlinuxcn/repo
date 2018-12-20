# Maintainer: Joey Dumont <joey.dumont@gmail.com>
# Contributor: Giuseppe Borzi <gborzi@ieee.org>
pkgname=superlu
pkgver=5.2.1
pkgrel=6
pkgdesc="Set of subroutines to solve a sparse linear system"
arch=('i686' 'x86_64')
url="http://crd-legacy.lbl.gov/~xiaoye/SuperLU/"
license=('custom')
depends=('gcc-libs' 'blas')
makedepends=('gcc-fortran' 'tcsh')
install=${pkgname}.install
source=(${url}${pkgname}_$pkgver.tar.gz ${url}License.txt
        ${url}ug.pdf)
sha512sums=('30538b4c2809294b8f34646bce6445944f21a1dffaf3ec0a0f29a55d5261caa56e4279d7722bb95cc9d89450d36ded969617edc82ecce7d0f1dfb24040d80d07'
            '10d4e497b4cc3aa2aaa2807e75641f9c0046f38876587adda33202546b7218a5d77843742e43ceca917726be0b985e7364b924e40d7377efafeba27bbbb5b7de'
            '19f8c8609f6c6d77c657756695c40da0dd0554a511b7090d8d17566e0d770c32e7f2d087530cc51aae80042e6068b0182a01ddaed6a7a086a77e087459b271e2')
options=('staticlibs')

build() {
  cd "$srcdir/SuperLU_$pkgver"
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
  install -m644 $srcdir/ug.pdf $pkgdir/usr/share/doc/$pkgname/ug.pdf
  install -m644 $srcdir/SuperLU_$pkgver/README $pkgdir/usr/share/doc/$pkgname
  install -m644 $srcdir/License.txt $pkgdir/usr/share/licenses/$pkgname
}

