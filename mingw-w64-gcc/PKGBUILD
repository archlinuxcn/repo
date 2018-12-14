# Contributor: Sergej Pupykin <pupykin.s+arch@gmail.com>
# Contributor: rubenvb vanboxem <dottie> ruben <attie> gmail <dottie> com

_targets="i686-w64-mingw32 x86_64-w64-mingw32"

pkgname=mingw-w64-gcc
pkgver=8.2.0
_islver=0.19
pkgrel=2
pkgdesc="Cross GCC for the MinGW-w64 cross-compiler"
arch=('x86_64')
url="http://gcc.gnu.org"
license=('GPL' 'LGPL' 'FDL' 'custom')
groups=('mingw-w64-toolchain' 'mingw-w64')
depends=('zlib' 'libmpc'
	 'mingw-w64-crt' 'mingw-w64-binutils' 'mingw-w64-winpthreads'
	 'mingw-w64-headers')
makedepends=("gcc-ada")
optdepends=()
provides=('mingw-w64-gcc-base')
replaces=()
backup=()
options=('!strip' 'staticlibs' '!emptydirs' '!buildflags')
#source=(https://sources.archlinux.org/other/gcc/gcc-${pkgver/+/-}.tar.xz{,.sig}
source=(https://ftp.gnu.org/gnu/gcc/gcc-$pkgver/gcc-$pkgver.tar.xz{,.sig}
       "http://isl.gforge.inria.fr/isl-${_islver}.tar.bz2"
       bz86593.patch)
validpgpkeys=(F3691687D867B81B51CE07D9BBE43771487328A9  # bpiotrowski@archlinux.org
              13975A70E63C361C73AE69EF6EEB81F8981C74C7  # richard.guenther@gmail.com
              33C235A34C46AA3FFB293709A328C3A2C3C45C06) # Jakub Jelinek <jakub@redhat.com>
sha256sums=('196c3c04ba2613f893283977e6011b2345d1cd1af9abeac58e916b1aab3e0080'
            'SKIP'
            'd59726f34f7852a081fbd3defd1ab2136f174110fc2e0c8d10bb122173fa9ed8'
            '5e8e3819f493749e5fac1a786661e014c9e1d7819796092b5768d2fc37778476')

prepare() {
  ln -sf gcc-${pkgver/+/-} gcc
  cd gcc

  # https://gcc.gnu.org/bugzilla/show_bug.cgi?id=86593
  rm -f gcc/testsuite/g++.dg/pr86593.C
  patch -p1 -i "$srcdir/bz86593.patch"

  # link isl for in-tree builds
  ln -sf ../isl-${_islver} isl
}

build() {
  for _target in ${_targets}; do
    mkdir -p "$srcdir"/gcc-build-${_target} && cd "$srcdir"/gcc-build-${_target}

    "$srcdir"/gcc/configure --prefix=/usr --libexecdir=/usr/lib \
        --target=${_target} \
        --enable-languages=c,lto,c++,objc,obj-c++,fortran,ada \
        --enable-shared --enable-static \
        --enable-threads=posix --enable-fully-dynamic-string --enable-libstdcxx-time=yes \
        --with-system-zlib --enable-cloog-backend=isl \
        --enable-lto --disable-dw2-exceptions --enable-libgomp \
        --disable-multilib --enable-checking=release
    make all
  done
}

package() {
  for _target in ${_targets}; do
    cd "$srcdir"/gcc-build-${_target}
    make DESTDIR="$pkgdir" install
    ${_target}-strip "$pkgdir"/usr/${_target}/lib/*.dll
    strip "$pkgdir"/usr/bin/${_target}-*
    strip "$pkgdir"/usr/lib/gcc/${_target}/${pkgver:0:5}/{cc1*,collect2,gnat1,f951,lto*}
    ln -s ${_target}-gcc "$pkgdir"/usr/bin/${_target}-cc
    # mv dlls
    mkdir -p "$pkgdir"/usr/${_target}/bin/
    mv "$pkgdir"/usr/${_target}/lib/*.dll "$pkgdir"/usr/${_target}/bin/
  done
  strip "$pkgdir"/usr/bin/*
  # remove unnecessary files
  rm -r "$pkgdir"/usr/share
  rm -f "$pkgdir"/usr/lib/libcc1.so*
  rm -f "$pkgdir"/usr/lib/libcc1.a
}
