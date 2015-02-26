# $Id: PKGBUILD 127583 2015-02-12 00:16:48Z heftig $
# Maintainer: Jan Alexander Steffens (heftig) <jan.steffens@gmail.com>
# Contributor: Jan de Groot <jgc@archlinux.org>
# Contributor: Allan McRae <allan@archlinux.org>
# x32 Maintainer: Fantix King <fantix.king@gmail.com>

# toolchain build order: linux-api-headers->glibc->binutils->gcc->binutils->glibc

_pkgbasename=glibc
pkgname=libx32-$_pkgbasename
pkgver=2.21
pkgrel=2.1
pkgdesc="GNU C Library (x32 ABI)"
arch=('x86_64')
url="http://www.gnu.org/software/libc"
license=('GPL' 'LGPL')
groups=()
depends=()
makedepends=('gcc-multilib-x32>=4.9')
backup=()
conflicts=('glibc-x32-seed')
provides=('glibc-x32-seed')


options=('!strip' 'staticlibs' '!emptydirs')

source=(http://ftp.gnu.org/gnu/libc/${_pkgbasename}-${pkgver}.tar.xz{,.sig}
        glibc-2.21-roundup.patch
        libx32-glibc.conf)
md5sums=('9cb398828e8f84f57d1f7d5588cf40cd'
         'SKIP'
         'bf9d96b11c76b113606aae102da63d9d'
         '34a4169d2bdc5a3eb83676a0831aae57')
validpgpkeys=('F37CDAB708E65EA183FD1AF625EF0A436C2A4AFF')  # Carlos O'Donell

prepare() {
  cd ${srcdir}/glibc-${pkgver}

  # glibc-2.21..75adf430
  patch -p1 -i $srcdir/glibc-2.21-roundup.patch

  mkdir ${srcdir}/glibc-build
}

build() {
  cd ${srcdir}/glibc-build

  #if [[ ${CARCH} = "i686" ]]; then
    # Hack to fix NPTL issues with Xen, only required on 32bit platforms
    # TODO: make separate glibc-xen package for i686
    #export CFLAGS="${CFLAGS} -mno-tls-direct-seg-refs"
  #fi

  if [ -x "/opt/gcc-x32-seed/bin/gcc" ]; then
    echo "Using gcc-x32-seed"
    gcc_home=`ls -d /opt/gcc-x32-seed/lib/gcc/x86_64-unknown-linux-gnu/*/`
    export CC="/opt/gcc-x32-seed/bin/gcc -mx32 -B"${gcc_home}
    export CXX="/opt/gcc-x32-seed/bin/g++ -mx32 -B"${gcc_home}
  else
    echo "Using gcc-multilib-x32"
    export CC="gcc -mx32"
    export CXX="g++ -mx32"
  fi
  echo "slibdir=/usr/libx32" >> configparms
  echo "rtlddir=/usr/libx32" >> configparms
  echo "sbindir=/usr/bin" >> configparms
  echo "rootsbindir=/usr/bin" >> configparms

  # remove hardening options for building libraries
  CFLAGS=${CFLAGS/-fstack-protector-strong/}
  CPPFLAGS=${CPPFLAGS/-D_FORTIFY_SOURCE=2/}

  ${srcdir}/${_pkgbasename}-${pkgver}/configure --prefix=/usr \
      --libdir=/usr/libx32 --libexecdir=/usr/libx32 \
      --with-headers=/usr/include \
      --with-bugurl=https://bugs.archlinux.org/ \
      --enable-add-ons \
      --enable-obsolete-rpc \
      --enable-kernel=2.6.32 \
      --enable-bind-now --disable-profile \
      --enable-stackguard-randomization \
      --enable-lock-elision \
      --enable-multi-arch \
      --disable-werror \
      x86_64-unknown-linux-gnux32
      #--target=x86_64-x32-linux --build=x86_64-linux --host=x86_64-x32-linux \

  # build libraries with hardening disabled
  echo "build-programs=no" >> configparms
  make

  # re-enable hardening for programs
  sed -i "/build-programs=/s#no#yes#" configparms
  echo "CC += -fstack-protector-strong -D_FORTIFY_SOURCE=2" >> configparms
  echo "CXX += -fstack-protector-strong -D_FORTIFY_SOURCE=2" >> configparms
  make

  # remove harding in preparation to run test-suite
  sed -i '5,7d' configparms
}

check() {
  # the linker commands need to be reordered - fixed in 2.19
  LDFLAGS=${LDFLAGS/--as-needed,/}

  cd ${srcdir}/glibc-build

  if [ -x "/opt/gcc-x32-seed/bin/gcc" ]; then
    make check || true
  else
    # tst-cleanupx4 failure on i686 is "expected"
    make check || true
  fi
}

package() {
  cd ${srcdir}/glibc-build
  make install_root=${pkgdir} install

  rm -rf ${pkgdir}/{etc,sbin,usr/{bin,sbin,share},var}

  # We need one x32 ABI specific header file
  find ${pkgdir}/usr/include -type f -not -name stubs-x32.h -delete


  # Dynamic linker
  mkdir ${pkgdir}/usr/lib
  ln -s ../libx32/ld-linux-x32.so.2 ${pkgdir}/usr/lib/

  # Add libx32 paths to the default library search path
  install -Dm644 "$srcdir/libx32-glibc.conf" "$pkgdir/etc/ld.so.conf.d/libx32-glibc.conf"

  # Symlink /usr/libx32/locale to /usr/lib/locale
  ln -s ../lib/locale "$pkgdir/usr/libx32/locale"

  # remove the static libraries that have a shared counterpart
  # libc, libdl, libm and libpthread are required for toolchain testsuites
  # in addition libcrypt appears widely required
  rm $pkgdir/usr/libx32/lib{anl,BrokenLocale,nsl,resolv,rt,util}.a

  # Do not strip the following files for improved debugging support
  # ("improved" as in not breaking gdb and valgrind...):
  #   ld-${pkgver}.so
  #   libc-${pkgver}.so
  #   libpthread-${pkgver}.so
  #   libthread_db-1.0.so

  cd $pkgdir
  strip $STRIP_BINARIES \
                        \
                        \
                        usr/libx32/getconf/*


  strip $STRIP_STATIC usr/libx32/*.a

  strip $STRIP_SHARED usr/libx32/{libanl,libBrokenLocale,libcidn,libcrypt}-*.so \
                      usr/libx32/libnss_{compat,db,dns,files,hesiod,nis,nisplus}-*.so \
                      usr/libx32/{libdl,libm,libnsl,libresolv,librt,libutil}-*.so \
                      usr/libx32/{libmemusage,libpcprofile,libSegFault}.so \
                      usr/libx32/{audit,gconv}/*.so

  # Fix issue that core/glibc didn't fix the path to /lib/ld-linux-x32.so.2
  ln -s /usr/lib ${pkgdir}/libx32
}
