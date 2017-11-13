# Maintainer: Patrick Stewart <patstew@gmail.com>
# Contributor:  Bartlomiej Piotrowski <bpiotrowski@archlinux.org>
# Contributor: Allan McRae <allan@archlinux.org>

# toolchain build order: linux-api-headers->glibc->binutils->gcc->binutils->glibc
# NOTE: valgrind requires rebuilt with each major glibc version

pkgname=glibc-wsl
pkgver=2.26
pkgrel=4
pkgdesc='GNU C Library'
arch=(i686 x86_64)
url='http://www.gnu.org/software/libc'
license=(GPL LGPL)
groups=(base)
depends=('linux-api-headers>=4.10' tzdata filesystem)
makedepends=(git gd)
optdepends=('gd: for memusagestat')
provides=(glibc=${pkgver}-${pkgrel})
conflicts=(glibc)
backup=(etc/gai.conf
        etc/locale.gen
        etc/nscd.conf)
options=(!strip staticlibs)
install=glibc.install
_commit=58270c0049404ef2f878fdd45df55f17f0b8c1f7
source=(glibc::git+https://sourceware.org/git/glibc.git#commit=${_commit}
        locale.gen.txt
        locale-gen
        0001-Don-t-use-IFUNC-resolver-for-longjmp-or-system-in-li.patch
        0002-x86-Add-x86_64-to-x86-64-HWCAP-BZ-22093.patch
        0001-Revert-linux-spawni.c-simplify-error-reporting-to-pa.patch
        0001-Revert-Assume-prlimit64-is-available.patch)
md5sums=('SKIP'
         '07ac979b6ab5eeb778d55f041529d623'
         '476e9113489f93b348b21e144b6a8fcf'
         'cbc073315c00b03898b7fc614274d6b3'
         'bd9b13f3294b6357baa809e4416b9f44'
         'a987eab514bee92cc627453c777896e8'
         '5758d6e2a0ca3dbd6019063f895b64da')

# pkgver() {
#   cd glibc
#   git describe --tags | sed 's/^glibc-//;s/-/+/g'
# }

prepare() {
  mkdir -p glibc-build

  cd glibc
  patch -p1 -i "$srcdir/0001-Don-t-use-IFUNC-resolver-for-longjmp-or-system-in-li.patch"
  patch -p1 -i "$srcdir/0002-x86-Add-x86_64-to-x86-64-HWCAP-BZ-22093.patch"
  patch -p1 -i "$srcdir/0001-Revert-linux-spawni.c-simplify-error-reporting-to-pa.patch"
  patch -p1 -i "$srcdir/0001-Revert-Assume-prlimit64-is-available.patch"
}  

build() {
  cd glibc-build

  if [[ ${CARCH} = "i686" ]]; then
    # Hack to fix NPTL issues with Xen, only required on 32bit platforms
    export CFLAGS="$CFLAGS -mno-tls-direct-seg-refs"
  fi

  echo "slibdir=/usr/lib" >> configparms
  echo "rtlddir=/usr/lib" >> configparms
  echo "sbindir=/usr/bin" >> configparms
  echo "rootsbindir=/usr/bin" >> configparms

  # remove fortify for building libraries
  CPPFLAGS=${CPPFLAGS/-D_FORTIFY_SOURCE=2/}

  "$srcdir/glibc/configure" \
      --prefix=/usr \
      --libdir=/usr/lib \
      --libexecdir=/usr/lib \
      --with-headers=/usr/include \
      --with-bugurl=https://bugs.archlinux.org/ \
      --enable-add-ons \
      --enable-bind-now \
      --enable-lock-elision \
      --enable-multi-arch \
      --enable-obsolete-nsl \
      --enable-obsolete-rpc \
      --enable-stack-protector=strong \
      --enable-stackguard-randomization \
      --disable-profile \
      --disable-werror

  # build libraries with fortify disabled
  echo "build-programs=no" >> configparms
  make

  # re-enable fortify for programs
  sed -i "/build-programs=/s#no#yes#" configparms

  echo "CC += -D_FORTIFY_SOURCE=2" >> configparms
  echo "CXX += -D_FORTIFY_SOURCE=2" >> configparms
  make
}

check() {
  cd glibc-build

  # remove fortify in preparation to run test-suite
  sed -i '/FORTIFY/d' configparms

  # some failures are "expected"
  make check || true
}

package() {
  install -dm755 "$pkgdir/etc"
  touch "$pkgdir/etc/ld.so.conf"

  make -C glibc-build install_root="$pkgdir" install
  rm -f "$pkgdir"/etc/ld.so.{cache,conf}

  cd glibc

  install -dm755 "$pkgdir"/usr/lib/{locale,systemd/system,tmpfiles.d}
  install -m644 nscd/nscd.conf "$pkgdir/etc/nscd.conf"
  install -m644 nscd/nscd.service "$pkgdir/usr/lib/systemd/system"
  install -m644 nscd/nscd.tmpfiles "$pkgdir/usr/lib/tmpfiles.d/nscd.conf"
  install -dm755 "$pkgdir/var/db/nscd"

  install -m644 posix/gai.conf "$pkgdir"/etc/gai.conf

  install -m755 "$srcdir/locale-gen" "$pkgdir/usr/bin"

  # create /etc/locale.gen
  install -m644 "$srcdir/locale.gen.txt" "$pkgdir/etc/locale.gen"
  sed -e '1,3d' -e 's|/| |g' -e 's|\\| |g' -e 's|^|#|g' \
    "$srcdir/glibc/localedata/SUPPORTED" >> "$pkgdir/etc/locale.gen"

  # Do not strip the following files for improved debugging support
  # ("improved" as in not breaking gdb and valgrind...):
  #   ld-${pkgver}.so
  #   libc-${pkgver}.so
  #   libpthread-${pkgver}.so
  #   libthread_db-1.0.so

  cd "$pkgdir"
  strip $STRIP_BINARIES usr/bin/{gencat,getconf,getent,iconv,iconvconfig} \
                        usr/bin/{ldconfig,locale,localedef,nscd,makedb} \
                        usr/bin/{pcprofiledump,pldd,rpcgen,sln,sprof} \
                        usr/lib/getconf/*

  strip $STRIP_STATIC usr/lib/lib{anl,BrokenLocale,c{,_nonshared},crypt}.a \
                      usr/lib/lib{dl,g,ieee,mcheck,nsl,pthread{,_nonshared}}.a \
                      usr/lib/lib{resolv,rpcsvc,rt,util}.a

  strip $STRIP_SHARED usr/lib/lib{anl,BrokenLocale,cidn,crypt}-${pkgver}.so \
                      usr/lib/libnss_{compat,db,dns,files,hesiod,nis,nisplus}-*.so \
                      usr/lib/lib{dl,m,nsl,resolv,rt,util}-${pkgver}.so \
                      usr/lib/lib{memusage,pcprofile,SegFault}.so \
                      usr/lib/{audit,gconv}/*.so || true

  if [[ $CARCH = "x86_64" ]]; then
    strip $STRIP_STATIC usr/lib/lib{m-${pkgver},mvec{,_nonshared}}.a
    strip $STRIP_SHARED usr/lib/libmvec-*.so
  fi
  
  if [[ $CARCH = "i686" ]]; then
    strip $STRIP_BINARIES usr/bin/lddlibc4
    strip $STRIP_STATIC usr/lib/libm.a
  fi
}
