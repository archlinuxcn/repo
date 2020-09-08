# Maintainer: ZenTauro <zentauro at riseup dot net>
# Maintainer: Ruben De Smet <ruben dot de dot smet at glycos dot org>
# Contributor: Jashandeep Sohi <jashandeep.s.sohi@gmail.com>

_gccmajor="10.2.0"
_gccver="10.2.0"
_gccsrc="gcc-${_gccver}"

pkgname='libgccjit'
pkgver="${_gccver}"
pkgrel=2
pkgdesc='Just-In-Time Compilation using GCC.'
url='https://gcc.gnu.org/wiki/JIT'
license=(
 'GPL3'
)
source=(
   "ftp://gcc.gnu.org/pub/gcc/releases/gcc-$_gccmajor/$_gccsrc.tar.xz"
)
sha512sums=('42ae38928bd2e8183af445da34220964eb690b675b1892bbeb7cd5bb62be499011ec9a93397dba5e2fb681afadfc6f2767d03b9035b44ba9be807187ae6dc65e')
#  "https://sources.archlinux.org/other/gcc/gcc-8.2.1-20180831.tar.xz"
arch=(
 'i686'
 'x86_64'
)
depends=(
 'glibc'
# 'isl>=0.14'
 'libmpc'
 'zlib'
 "gcc-libs=$pkgver"
)
makedepends=(
 'binutils'
 'gcc-ada'
 'libmpc>=0.8.1'
 'gmp>=4.3.2'
 'mpfr>=2.4.2'
# 'isl>=0.14'
)
checkdepends=(
 'dejagnu'
)
options=(
 '!emptydirs'
)

prepare() {
 cd "$srcdir/$_gccsrc"

 # Do not run fixincludes
 sed -i 's@\./fixinc\.sh@-c true@' gcc/Makefile.in
}

build() {
 install -d "$srcdir/$pkgname-build"
 cd "$srcdir/$pkgname-build"

 CPPFLAGS="$CPPFLAGS -O2"

 ../$_gccsrc/configure \
  --prefix="/usr" \
  --libexecdir="/usr/lib" \
  --with-system-zlib \
  --with-bugurl='https://github.com/jashandeep-sohi/libgccjit-pkg/issues' \
  --with-linker-hash-style=gnu \
  --enable-host-shared \
  --enable-shared \
  --enable-checking=release \
  --enable-languages=jit \
  --enable-linker-build-id \
  --enable-checking=release \
  --disable-multilib \
  --disable-bootstrap \
  --disable-libssp \
  --disable-lto \
  --disable-libquadmath \
  --disable-liboffloadmic \
  --disable-libada \
  --disable-libsanitizer \
  --disable-libquadmath-support \
  --disable-libgomp \
  --disable-libvtv \
  --disable-libsanitizer

 make
}

package() {
 cd "$srcdir/$pkgname-build/gcc"
 make DESTDIR="$pkgdir" jit.install-common jit.install-info
}

check() {
 cd "$srcdir/$pkgname-build/gcc"
 make check-jit RUNTESTFLAGS="-v -v -v"
}

post_install() {
 [[ -x usr/bin/install-info ]] || return 0
 install-info usr/share/info/libgccjit.info.gz usr/share/info/dir 2> /dev/null
}

# vim: tabstop=1 expandtab
