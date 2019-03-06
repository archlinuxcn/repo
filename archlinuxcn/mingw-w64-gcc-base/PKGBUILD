# Maintainer: Sergej Pupykin <pupykin.s+arch@gmail.com>
# Maintainer: rubenvb vanboxem <dottie> ruben <attie> gmail <dottie> com

_targets="i686-w64-mingw32 x86_64-w64-mingw32"

pkgname=mingw-w64-gcc-base
pkgver=8.3.0
_islver=0.20
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
sha256sums=('64baadfe6cc0f4947a84cb12d7f0dfaf45bb58b7e92461639596c21e02d97d2c'
            'SKIP'
            'b587e083eb65a8b394e833dea1744f21af3f0e413a448c17536b5549ae42a4c2')

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
  for _target in ${_targets}; do
    msg "Building ${_target} GCC C compiler"
    mkdir -p ${srcdir}/gcc-build-${_target} && cd ${srcdir}/gcc-build-${_target}

    ${srcdir}/gcc-${pkgver}/configure --prefix=/usr \
        --target=${_target} \
        --enable-languages=c,lto \
        --enable-static \
        --with-system-zlib \
        --enable-lto --disable-dw2-exceptions \
        --disable-nls --enable-version-specific-runtime-libs \
        --disable-multilib --enable-checking=release
    make all-gcc
  done
}

package() {
  for _target in ${_targets}; do
    msg "Installing ${_target} GCC C compiler"
    cd ${srcdir}/gcc-build-${_target}
    make DESTDIR=${pkgdir} install-gcc
    strip ${pkgdir}/usr/bin/${_target}-*
    strip ${pkgdir}/usr/libexec/gcc/${_target}/${pkgver}/{cc1,collect2,lto*}
  done
  # remove unnecessary files
  msg "Removing man and info pages"
  rm -r ${pkgdir}/usr/share/man
  rm -r ${pkgdir}/usr/share/info
}
