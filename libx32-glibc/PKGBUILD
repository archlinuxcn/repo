# $Id: PKGBUILD 103537 2014-01-07 13:27:35Z heftig $
# Maintainer: Fantix King <fantix.king@gmail.com>
# Upstream Maintainer: Jan Alexander Steffens (heftig) <jan.steffens@gmail.com>
# Contributor: Jan de Groot <jgc@archlinux.org>
# Contributor: Allan McRae <allan@archlinux.org>

# toolchain build order: linux-api-headers->glibc->binutils->gcc->binutils->glibc
# NOTE: valgrind requires rebuilt with each major glibc version

_pkgbasename=glibc
pkgname=libx32-$_pkgbasename
pkgver=2.18_12
pkgrel=1
pkgdesc="GNU C Library for x32 ABI"
arch=('x86_64')
url="http://www.gnu.org/software/libc"
license=('GPL' 'LGPL')
makedepends=('gcc-multilib-x32>=4.7')
conflicts=('glibc-x32-seed')
provides=('glibc-x32-seed')
options=('!strip' '!emptydirs' 'staticlibs')
source=(http://ftp.gnu.org/gnu/libc/${_pkgbasename}-${pkgver%_*}.tar.xz{,.sig}
        glibc-2.18-make-4.patch
        glibc-2.18-readdir_r-CVE-2013-4237.patch
        glibc-2.18-malloc-corrupt-CVE-2013-4332.patch
        glibc-2.18-strcoll-CVE-2012-4412+4424.patch
        glibc-2.18-ptr-mangle-CVE-2013-4788.patch
        glibc-2.18-getaddrinfo-CVE-2013-4458.patch
        glibc-2.18-getaddrinfo-assertion.patch
        glibc-2.18-scanf-parse-0e-0.patch
        glibc-2.18-strstr-hackfix.patch
        glibc-2.18-xattr-compat-hack.patch
        libx32-glibc.conf)
md5sums=('88fbbceafee809e82efd52efa1e3c58f'
         'SKIP'
         'e1883c2d1b01ff73650db5f5bb5a5a52'
         '154da6bf5a5248f42a7bf5bf08e01a47'
         'b79561ab9dce900e9bbeaf0d49927c2b'
         'c7264b99d0f7e51922a4d3126182c40a'
         '9749ba386b08a8fe53e7ecede9bf2dfb'
         '71329fccb8eb583fb0d67b55f1e8df68'
         'd4d86add33f22125777e0ecff06bc9bb'
         '01d19fe9b2aea489cf5651530e0369f2'
         '4441f6dfe7d75ced1fa75e54dd21d36e'
         '7ca96c68a37f2a4ab91792bfa0160a24'
         '34a4169d2bdc5a3eb83676a0831aae57')

prepare() {
  cd ${srcdir}/${_pkgbasename}-${pkgver%_*}

  # compatibility with make-4.0 (submitted upstream)
  patch -p1 -i $srcdir/glibc-2.18-make-4.patch

  # upstream commit 91ce4085
  patch -p1 -i $srcdir/glibc-2.18-readdir_r-CVE-2013-4237.patch

  # upstream commits 1159a193, 55e17aad and b73ed247
  patch -p1 -i $srcdir/glibc-2.18-malloc-corrupt-CVE-2013-4332.patch

  # upstream commits 1326ba1a, 141f3a77 and 303e567a
  patch -p1 -i $srcdir/glibc-2.18-strcoll-CVE-2012-4412+4424.patch

  # upstream commits c61b4d41 and 0b1f8e35
  patch -p1 -i $srcdir/glibc-2.18-ptr-mangle-CVE-2013-4788.patch

  # upstream commit 7cbcdb36
  patch -p1 -i $srcdir/glibc-2.18-getaddrinfo-CVE-2013-4458.patch

  # upstream commit 894f3f10
  patch -p1 -i $srcdir/glibc-2.18-getaddrinfo-assertion.patch

  # upstream commit a4966c61
  patch -p1 -i $srcdir/glibc-2.18-scanf-parse-0e-0.patch

  # hack fix for strstr issues on x86
  patch -p1 -i $srcdir/glibc-2.18-strstr-hackfix.patch
  
  # hack fix for {linux,sys}/xattr.h incompatibility
  patch -p1 -i $srcdir/glibc-2.18-xattr-compat-hack.patch

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
  echo "sbindir=/usr/bin" >> configparms
  echo "rootsbindir=/usr/bin" >> configparms

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
      --enable-lock-elision \
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
  sed -i '4,6d' configparms
}

check() {
  # the linker commands need to be reordered - fixed in 2.19
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
