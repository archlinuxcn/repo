pkgname=mingw-w64-gcc
pkgver=10.1.0
_islver=0.21
pkgrel=1
pkgdesc="Cross GCC for the MinGW-w64 cross-compiler"
arch=('x86_64')
url="https://gcc.gnu.org"
license=('GPL' 'LGPL' 'FDL' 'custom')
groups=('mingw-w64-toolchain' 'mingw-w64')
depends=('zlib' 'libmpc' 'mingw-w64-crt' 'mingw-w64-binutils' 'mingw-w64-winpthreads' 'mingw-w64-headers')
makedepends=("gcc-ada>=${pkgver:0:2}")
provides=('mingw-w64-gcc-base')
options=('!strip' 'staticlibs' '!emptydirs' '!buildflags')
source=(https://ftp.gnu.org/gnu/gcc/gcc-$pkgver/gcc-$pkgver.tar.xz{,.sig}
       "http://isl.gforge.inria.fr/isl-${_islver}.tar.bz2")
validpgpkeys=(33C235A34C46AA3FFB293709A328C3A2C3C45C06) # Jakub Jelinek <jakub@redhat.com>
sha256sums=('b6898a23844b656f1b68691c5c012036c2e694ac4b53a8918d4712ad876e7ea2'
            'SKIP'
            'd18ca11f8ad1a39ab6d03d3dcb3365ab416720fcb65b42d69f34f51bf0a0e859')

_architectures="i686-w64-mingw32 x86_64-w64-mingw32"

prepare() {
  ln -sf gcc-${pkgver/+/-} gcc
  cd gcc

  # mmapio.c:69:14: error: implicit declaration of function ‘getpagesize’
  sed -i 's|\-Werror||g' libbacktrace/configure

  # link isl for in-tree builds
  ln -sf ../isl-${_islver} isl
}

build() {
  for _arch in ${_architectures}; do
    mkdir -p "$srcdir"/build-${_arch} && cd "$srcdir"/build-${_arch}
    "$srcdir"/gcc/configure --prefix=/usr --libexecdir=/usr/lib \
        --target=${_arch} \
        --with-bugurl=https://bugs.archlinux.org/ \
        --enable-languages=c,lto,c++,ada,objc,obj-c++,fortran \
        --enable-shared --enable-static \
        --enable-threads=posix --enable-fully-dynamic-string \
        --enable-libstdcxx-time=yes --enable-libstdcxx-filesystem-ts=yes \
        --with-system-zlib --enable-cloog-backend=isl \
        --enable-lto --enable-libgomp \
        --disable-multilib --enable-checking=release \
        --disable-sjlj-exceptions --with-dwarf2
    make
  done
}

package() {
  for _arch in ${_architectures}; do
    cd "$srcdir"/build-${_arch}
    make DESTDIR="$pkgdir" install
    ${_arch}-strip "$pkgdir"/usr/${_arch}/lib/*.dll
    strip "$pkgdir"/usr/bin/${_arch}-*
    strip "$pkgdir"/usr/lib/gcc/${_arch}/${pkgver}/{cc1*,collect2,gnat1,f951,lto*}
    ln -s ${_arch}-gcc "$pkgdir"/usr/bin/${_arch}-cc
    # mv dlls
    mkdir -p "$pkgdir"/usr/${_arch}/bin/
    mv "$pkgdir"/usr/${_arch}/lib/*.dll "$pkgdir"/usr/${_arch}/bin/
  done
  strip "$pkgdir"/usr/bin/*
  # remove unnecessary files
  rm -r "$pkgdir"/usr/share
  rm "$pkgdir"/usr/lib/libcc1.*
}
