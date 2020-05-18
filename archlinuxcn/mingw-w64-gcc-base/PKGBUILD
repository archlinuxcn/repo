pkgname=mingw-w64-gcc-base
pkgver=10.1.0
_islver=0.21
pkgrel=1
pkgdesc="Cross GCC for the MinGW-w64 cross-compiler (bootstrap)"
arch=('x86_64')
url="http://gcc.gnu.org"
license=('GPL' 'LGPL' 'FDL' 'custom')
groups=('mingw-w64-bootstrap' 'mingw-w64')
depends=('zlib' 'libmpc' 'mingw-w64-binutils' 'mingw-w64-headers' 'mingw-w64-headers-bootstrap')
conflicts=('mingw-w64-gcc')
options=('staticlibs' '!emptydirs')
source=(https://ftp.gnu.org/gnu/gcc/gcc-$pkgver/gcc-$pkgver.tar.xz{,.sig}
       "http://isl.gforge.inria.fr/isl-${_islver}.tar.bz2")
validpgpkeys=(33C235A34C46AA3FFB293709A328C3A2C3C45C06) # Jakub Jelinek <jakub@redhat.com>
sha256sums=('b6898a23844b656f1b68691c5c012036c2e694ac4b53a8918d4712ad876e7ea2'
            'SKIP'
            'd18ca11f8ad1a39ab6d03d3dcb3365ab416720fcb65b42d69f34f51bf0a0e859')

_architectures="i686-w64-mingw32 x86_64-w64-mingw32"

prepare() {
  cd ${srcdir}/gcc-${pkgver}

  #do not install libiberty
  sed -i 's/install_to_$(INSTALL_DEST) //' libiberty/Makefile.in
  # hack! - some configure tests for header files using "$CPP $CPPFLAGS"
  sed -i "/ac_cpp=/s/\$CPPFLAGS/\$CPPFLAGS -O2/" {libiberty,gcc}/configure

  # link isl for in-tree builds
  ln -sf ../isl-${_islver} isl
}

build() {
  for _arch in ${_architectures}; do
    mkdir -p "${srcdir}"/gcc-build-${_arch} && cd "${srcdir}"/gcc-build-${_arch}
    "${srcdir}"/gcc-${pkgver}/configure --prefix=/usr \
        --target=${_arch} \
        --enable-languages=c,lto \
        --enable-static \
        --with-system-zlib \
        --enable-lto \
        --disable-nls --enable-version-specific-runtime-libs \
        --disable-multilib --enable-checking=release \
        --disable-sjlj-exceptions --with-dwarf2
    make all-gcc
  done
}

package() {
  for _arch in ${_architectures}; do
    cd "${srcdir}"/gcc-build-${_arch}
    make DESTDIR=${pkgdir} install-gcc
    strip ${pkgdir}/usr/bin/${_arch}-*
    strip ${pkgdir}/usr/libexec/gcc/${_arch}/${pkgver}/{cc1,collect2,lto*}
  done
  rm -r ${pkgdir}/usr/share/{man,info}
}
