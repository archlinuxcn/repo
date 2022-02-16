# Maintainer: Andrew Whatson <https://aur.archlinux.org/account/flatwhatson>
# Maintainer: ZenTauro <zentauro at riseup dot net>
# Contributor: Ruben De Smet <ruben dot de dot smet at glycos dot org>
# Contributor: Jashandeep Sohi <jashandeep.s.sohi@gmail.com>

pkgname=libgccjit
pkgver=11.2.0
pkgrel=2
pkgdesc='Just-In-Time Compilation using GCC.'
arch=(x86_64)
license=(GPL3)
url='https://gcc.gnu.org/wiki/JIT'
makedepends=(binutils libmpc)
checkdepends=(dejagnu)
depends=(glibc libmpc "gcc-libs=$pkgver")
options=(!emptydirs)
source=(https://sourceware.org/pub/gcc/releases/gcc-${pkgver}/gcc-${pkgver}.tar.xz{,.sig})
validpgpkeys=(F3691687D867B81B51CE07D9BBE43771487328A9  # bpiotrowski@archlinux.org
              86CFFCA918CF3AF47147588051E8B148A9999C34  # evangelos@foutrelis.com
              13975A70E63C361C73AE69EF6EEB81F8981C74C7  # richard.guenther@gmail.com
              D3A93CAD751C2AF4F8C7AD516C35B99309B5FA62) # Jakub Jelinek <jakub@redhat.com>
sha256sums=('d08edc536b54c372a1010ff6619dd274c0f1603aa49212ba20f7aa2cda36fa8b'
            'SKIP')

prepare() {
 cd "$srcdir/gcc-$pkgver"

 # Do not run fixincludes
 sed -i 's@\./fixinc\.sh@-c true@' gcc/Makefile.in

 # Arch Linux installs x86_64 libraries /lib
 sed -i '/m64=/s/lib64/lib/' gcc/config/i386/t-linux64

 # hack! - some configure tests for header files using "$CPP $CPPFLAGS"
 sed -i "/ac_cpp=/s/\$CPPFLAGS/\$CPPFLAGS -O2/" {libiberty,gcc}/configure
}

build() {
 mkdir -p "$srcdir/$pkgname-build"
 cd "$srcdir/$pkgname-build"

 CFLAGS=${CFLAGS/-Werror=format-security/}
 CXXFLAGS=${CXXFLAGS/-Werror=format-security/}

 "$srcdir/gcc-$pkgver/configure" --prefix=/usr \
     --libdir=/usr/lib \
     --libexecdir=/usr/lib \
     --mandir=/usr/share/man \
     --infodir=/usr/share/info \
     --with-bugurl=https://aur.archlinux.org/packages/libgccjit/ \
     --enable-languages=jit \
     --with-linker-hash-style=gnu \
     --with-system-zlib \
     --enable-__cxa_atexit \
     --enable-cet=auto \
     --enable-checking=release \
     --enable-clocale=gnu \
     --enable-default-pie \
     --enable-default-ssp \
     --enable-gnu-indirect-function \
     --enable-gnu-unique-object \
     --enable-install-libiberty \
     --enable-linker-build-id \
     --enable-lto \
     --enable-multilib \
     --enable-plugin \
     --enable-shared \
     --enable-host-shared \
     --enable-threads=posix \
     --disable-bootstrap \
     --disable-multilib \
     --disable-libssp \
     --disable-lto \
     --disable-libquadmath \
     --disable-liboffloadmic \
     --disable-libada \
     --disable-libsanitizer \
     --disable-libquadmath-support \
     --disable-libgomp \
     --disable-libvtv \
     --disable-libsanitizer \
     --disable-libstdcxx-pch \
     --disable-libunwind-exceptions \
     --disable-werror

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
