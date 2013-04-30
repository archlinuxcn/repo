# $Id$
# Maintainer: Fantix King <fantix.king@gmail.com>
# Upstream Maintainer: Jan Alexander Steffens (heftig) <jan.steffens@gmail.com>
# Contributor: Jan de Groot <jgc@archlinux.org>
# Contributor: Allan McRae <allan@archlinux.org>

# toolchain build order: linux-api-headers->glibc->binutils->gcc->binutils->glibc
# NOTE: valgrind requires rebuilt with each major glibc version

_pkgbasename=glibc
pkgname=libx32-$_pkgbasename
pkgver=2.17_5
pkgrel=1
pkgdesc="GNU C Library for x32 ABI"
arch=('x86_64')
url="http://www.gnu.org/software/libc"
license=('GPL' 'LGPL')
makedepends=('gcc-multilib-x32>=4.7')
conflicts=('glibc-x32-seed')
provides=('glibc-x32-seed')
options=('!strip' '!emptydirs')
source=(http://ftp.gnu.org/gnu/libc/${_pkgbasename}-${pkgver%_*}.tar.xz{,.sig}
        glibc-2.17-sync-with-linux37.patch
        glibc-2.17-getaddrinfo-stack-overflow.patch
        glibc-2.17-regexp-matcher-overrun.patch
        libx32-glibc.conf)
md5sums=('87bf675c8ee523ebda4803e8e1cec638'
         'SKIP'
         'fb99380d94598cc76d793deebf630022'
         '56d5f2c09503a348281a20ae404b7de3'
         '200acc05961b084ee00dde919e64f82d'
         '34a4169d2bdc5a3eb83676a0831aae57')

build() {
  cd ${srcdir}/${_pkgbasename}-${pkgver%_*}

  # combination of upstream commits 318cd0b, b540704 and fc1abbe
  patch -p1 -i ${srcdir}/glibc-2.17-sync-with-linux37.patch

  # CVE-2013-1914 - upstream commit 1cef1b19
  patch -p1 -i ${srcdir}/glibc-2.17-getaddrinfo-stack-overflow.patch

  # CVE-2013-0242 - upstream commit a445af0b
  patch -p1 -i ${srcdir}/glibc-2.17-regexp-matcher-overrun.patch

  cd ${srcdir}
  mkdir glibc-build
  cd glibc-build

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

  # remove hardening options for building libraries
  CFLAGS=${CFLAGS/-fstack-protector/}
  CPPFLAGS=${CPPFLAGS/-D_FORTIFY_SOURCE=2/}

  ${srcdir}/${_pkgbasename}-${pkgver%_*}/configure --prefix=/usr \
      --libdir=/usr/libx32 --libexecdir=/usr/libx32 \
      --with-headers=/usr/include \
      --with-bugurl=https://bugs.archlinux.org/ \
      --enable-add-ons=nptl,libidn \
      --enable-obsolete-rpc \
      --enable-kernel=2.6.32 \
      --enable-bind-now --disable-profile \
      --enable-stackguard-randomization \
      --target=x86_64-x32-linux --build=x86_64-linux --host=x86_64-x32-linux \
      --enable-multi-arch x86_64-x32-linux

  # build libraries with hardening disabled
  echo "build-programs=no" >> configparms
  make
  
  # re-enable hardening for programs
  sed -i "/build-programs=/s#no#yes#" configparms
  echo "CC += -fstack-protector -D_FORTIFY_SOURCE=2" >> configparms
  echo "CXX += -fstack-protector -D_FORTIFY_SOURCE=2" >> configparms
  make

  # remove harding in preparation to run test-suite
  sed -i '2,4d' configparms
}

check() {
  # bug to file - the linker commands need to be reordered
  LDFLAGS=${LDFLAGS/--as-needed,/}

  cd ${srcdir}/glibc-build
  if [ -x "/opt/gcc-x32-seed/bin/gcc" ]; then
    make check || true
  else
    make check
  fi
}

package() {
  cd ${srcdir}/glibc-build
  make install_root=${pkgdir} install

  rm -rf ${pkgdir}/{etc,sbin,usr/{bin,sbin,share},var}

  # We need one x32 ABI specific header file
  find ${pkgdir}/usr/include -type f -not -name stubs-x32.h -delete

  # Do not strip the following files for improved debugging support
  # ("improved" as in not breaking gdb and valgrind...):
  #   ld-${pkgver}.so
  #   libc-${pkgver}.so
  #   libpthread-${pkgver}.so
  #   libthread_db-1.0.so

  cd $pkgdir
  strip $STRIP_BINARIES usr/libx32/getconf/*

  strip $STRIP_STATIC usr/libx32/*.a

  strip $STRIP_SHARED usr/libx32/{libanl,libBrokenLocale,libcidn,libcrypt}-*.so \
                      usr/libx32/libnss_{compat,db,dns,files,hesiod,nis,nisplus}-*.so \
                      usr/libx32/{libdl,libm,libnsl,libresolv,librt,libutil}-*.so \
                      usr/libx32/{libmemusage,libpcprofile,libSegFault}.so \
                      usr/libx32/{pt_chown,{audit,gconv}/*.so}

  # Dynamic linker
  mkdir ${pkgdir}/usr/lib
  ln -s ../libx32/ld-linux-x32.so.2 ${pkgdir}/usr/lib/

  # Add libx32 paths to the default library search path
  install -Dm644 "$srcdir/libx32-glibc.conf" "$pkgdir/etc/ld.so.conf.d/libx32-glibc.conf"

  # Symlink /usr/libx32/locale to /usr/lib/locale
  ln -s ../lib/locale "$pkgdir/usr/libx32/locale"

  # Fix issue that core/glibc didn't fix the path to /lib/ld-linux-x32.so.2
  ln -s /usr/lib ${pkgdir}/libx32
}
