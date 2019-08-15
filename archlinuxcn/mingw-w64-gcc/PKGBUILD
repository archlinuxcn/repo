# Contributor: Sergej Pupykin <pupykin.s+arch@gmail.com>
# Contributor: rubenvb vanboxem <dottie> ruben <attie> gmail <dottie> com

_targets="i686-w64-mingw32 x86_64-w64-mingw32"

pkgname=mingw-w64-gcc
pkgver=9.2.0
_islver=0.21
pkgrel=1
pkgdesc="Cross GCC for the MinGW-w64 cross-compiler"
arch=('x86_64')
url="https://gcc.gnu.org"
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
       "http://isl.gforge.inria.fr/isl-${_islver}.tar.bz2")
validpgpkeys=(F3691687D867B81B51CE07D9BBE43771487328A9  # bpiotrowski@archlinux.org
              13975A70E63C361C73AE69EF6EEB81F8981C74C7  # richard.guenther@gmail.com
              33C235A34C46AA3FFB293709A328C3A2C3C45C06) # Jakub Jelinek <jakub@redhat.com>
sha256sums=('ea6ef08f121239da5695f76c9b33637a118dcf63e24164422231917fa61fb206'
            'SKIP'
            'd18ca11f8ad1a39ab6d03d3dcb3365ab416720fcb65b42d69f34f51bf0a0e859')

prepare() {
  ln -sf gcc-${pkgver/+/-} gcc
  cd gcc

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
        --enable-threads=posix --enable-fully-dynamic-string \
        --enable-libstdcxx-time=yes --enable-libstdcxx-filesystem-ts=yes \
        --with-system-zlib --enable-cloog-backend=isl \
        --enable-lto --disable-dw2-exceptions --enable-libgomp \
        --disable-multilib --enable-checking=release
    make
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
  rm "$pkgdir"/usr/lib/libcc1.*
}
