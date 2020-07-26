pkgname=mingw-w64-binutils
pkgver=2.35
pkgrel=1
pkgdesc="Cross binutils for the MinGW-w64 cross-compiler"
arch=('x86_64')
url="http://www.gnu.org/software/binutils"
license=('GPL')
groups=('mingw-w64-toolchain' 'mingw-w64')
depends=('zlib')
options=('!libtool' '!emptydirs')
validpgpkeys=('3A24BC1E8FB409FA9F14371813FCEF89DD9E3C4F')  # Nick Clifton (Chief Binutils Maintainer) <nickc@redhat.com>
source=("https://ftp.gnu.org/gnu/binutils/binutils-${pkgver}.tar.gz"{,.sig})
sha256sums=('a3ac62bae4f339855b5449cfa9b49df90c635adbd67ecb8a0e7f3ae86a058da6'
            'SKIP')

_targets="i686-w64-mingw32 x86_64-w64-mingw32"

prepare() {
  cd "$srcdir"/binutils-${pkgver}
  #do not install libiberty
  sed -i 's/install_to_$(INSTALL_DEST) //' libiberty/Makefile.in
  # hack! - libiberty configure tests for header files using "$CPP $CPPFLAGS"
  sed -i "/ac_cpp=/s/\$CPPFLAGS/\$CPPFLAGS -O2/" libiberty/configure
}

build() {
  for _target in $_targets; do
    msg "Building ${_target} cross binutils"
    mkdir -p "$srcdir"/binutils-${_target} && cd "${srcdir}/binutils-${_target}"
    "$srcdir"/binutils-${pkgver}/configure --prefix=/usr \
        --target=${_target} \
        --infodir=/usr/share/info/${_target} \
        --enable-lto --enable-plugins \
        --enable-deterministic-archives \
        --disable-multilib --disable-nls \
        --disable-werror
     make
  done
}

package() {
  for _target in ${_targets}; do
    msg "Installing ${_target} cross binutils"
    cd "$srcdir"/binutils-${_target}
    make DESTDIR="$pkgdir" install
  done
}
