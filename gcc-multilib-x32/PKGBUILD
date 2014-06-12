# $Id: PKGBUILD 112777 2014-06-06 22:12:36Z heftig $
# Maintainer: Fantix King <fantix.king@gmail.com>
# Upstream Maintainer: Jan Alexander Steffens (heftig) <jan.steffens@gmail.com>
# Contributor: Allan McRae <allan@archlinux.org>

# toolchain build order: linux-api-headers->glibc->binutils->gcc->binutils->glibc
# NOTE: libtool requires rebuilt with each new gcc version

pkgname='gcc-multilib-x32'
true && pkgname=('gcc-multilib-x32' 'gcc-libs-multilib-x32' 'libx32-gcc-libs' 'gcc-fortran-multilib-x32' 'gcc-objc-multilib-x32' 'gcc-ada-multilib-x32' 'gcc-go-multilib-x32')
pkgver=4.9.0_4
_pkgver=4.9
pkgrel=1
_snapshot=4.9-20140604
pkgdesc="The GNU Compiler Collection for multilib with x32 ABI support"
arch=('x86_64')
license=('GPL' 'LGPL' 'FDL' 'custom')
url="http://gcc.gnu.org"
makedepends=('binutils>=2.24' 'libmpc' 'cloog' 'gcc-ada-multilib' 'doxygen'
             'lib32-glibc>=2.19' 'libx32-glibc>=2.19')
checkdepends=('dejagnu' 'inetutils')
options=('!emptydirs')
source=(#ftp://gcc.gnu.org/pub/gcc/releases/gcc-${pkgver%_*}/gcc-${pkgver%_*}.tar.bz2
        ftp://gcc.gnu.org/pub/gcc/snapshots/${_snapshot}/gcc-${_snapshot}.tar.bz2
        gcc-4.8-filename-output.patch)
md5sums=('57aa4ff81c56262dc89994853c4d0149'
         '40cb437805e2f7a006aa0d0c3098ab0f')

if [ -n "${_snapshot}" ]; then
  _basedir=gcc-${_snapshot}
else
  _basedir=gcc-${pkgver%_*}
fi

_libdir="usr/lib/gcc/$CHOST/${pkgver%_*}"

prepare() {
  if [ ! `zgrep CONFIG_X86_X32=y /proc/config.gz` ]; then
    error "Your current kernel doesn't support X32 ABI!"
    msg2 "You need to install a kernel with CONFIG_X86_X32=y"
    msg2 "linux-pf from AUR for example supports X32 ABI"
    exit 1
  fi

  cd ${srcdir}/${_basedir}

  # Do not run fixincludes
  sed -i 's@\./fixinc\.sh@-c true@' gcc/Makefile.in

  # Arch Linux installs x86_64 libraries /lib
  [[ $CARCH == "x86_64" ]] && sed -i '/m64=/s/lib64/lib/' gcc/config/i386/t-linux64

  echo ${pkgver%_*} > gcc/BASE-VER

  # hack! - some configure tests for header files using "$CPP $CPPFLAGS"
  sed -i "/ac_cpp=/s/\$CPPFLAGS/\$CPPFLAGS -O2/" {libiberty,gcc}/configure

  # http://gcc.gnu.org/bugzilla/show_bug.cgi?id=57653
  patch -p0 -i ${srcdir}/gcc-4.8-filename-output.patch

  mkdir ${srcdir}/gcc-build
}

build() {
  cd ${srcdir}/gcc-build

  # using -pipe causes spurious test-suite failures
  # http://gcc.gnu.org/bugzilla/show_bug.cgi?id=48565
  CFLAGS=${CFLAGS/-pipe/}
  CXXFLAGS=${CXXFLAGS/-pipe/}

  ${srcdir}/${_basedir}/configure --prefix=/usr \
      --libdir=/usr/lib --libexecdir=/usr/lib \
      --mandir=/usr/share/man --infodir=/usr/share/info \
      --with-bugurl=https://bugs.archlinux.org/ \
      --enable-languages=c,c++,ada,fortran,go,lto,objc,obj-c++ \
      --enable-shared --enable-threads=posix \
      --with-system-zlib --enable-__cxa_atexit \
      --disable-libunwind-exceptions --enable-clocale=gnu \
      --disable-libstdcxx-pch --disable-libssp \
      --enable-gnu-unique-object --enable-linker-build-id \
      --enable-cloog-backend=isl --disable-cloog-version-check \
      --enable-lto --enable-plugin --enable-install-libiberty \
      --with-linker-hash-style=gnu \
      --enable-multilib --disable-werror \
      --with-multilib-list=m32,m64,mx32 \
      --enable-checking=release
  make
  
  # make documentation
  make -C $CHOST/libstdc++-v3/doc doc-man-doxygen
}

check() {
  cd ${srcdir}/gcc-build

  # increase stack size to prevent test failures
  # http://gcc.gnu.org/bugzilla/show_bug.cgi?id=31827
  ulimit -s 32768

  # do not abort on error as some are "expected"
  make -k check || true
  ${srcdir}/${_basedir}/contrib/test_summary
}

package_libx32-gcc-libs()
{
  pkgdesc="Runtime libraries shipped by GCC (x32 ABI)"
  depends=('libx32-glibc>=2.19')
  options=('!emptydirs')

  cd ${srcdir}/gcc-build

  make -C $CHOST/x32/libgcc DESTDIR=${pkgdir} install-shared
  rm ${pkgdir}/${_libdir}/x32/libgcc_eh.a

  for lib in libatomic \
             libcilkrts \
             libgfortran \
             libgomp \
             libitm \
             libquadmath \
             libsanitizer/{a,l,ub}san \
             libstdc++-v3/src \
             libvtv; do
    make -C $CHOST/x32/$lib DESTDIR=${pkgdir} install-toolexeclibLTLIBRARIES
  done

  make -C $CHOST/x32/libobjc DESTDIR=${pkgdir} install-libs

  # remove stuff in gcc-libs-multilib-x32
  rm -r ${pkgdir}/usr/lib

  # Install Runtime Library Exception
  install -Dm644 ${srcdir}/${_basedir}/COPYING.RUNTIME \
    ${pkgdir}/usr/share/licenses/libx32-gcc-libs/RUNTIME.LIBRARY.EXCEPTION
}

package_gcc-libs-multilib-x32()
{
  pkgdesc="Runtime libraries shipped by GCC for multilib with x32 ABI support"
  depends=('glibc>=2.19' "lib32-gcc-libs=${pkgver//_/-}" "libx32-gcc-libs=$pkgver-$pkgrel")
  provides=("gcc-libs=${pkgver//_/-}" "gcc-libs-multilib=${pkgver//_/-}")
  conflicts=('gcc-libs')
  options=('!emptydirs')
  install=gcc-libs.install

  cd ${srcdir}/gcc-build
  
  make -C $CHOST/libgcc DESTDIR=${pkgdir} install-shared
  rm ${pkgdir}/${_libdir}/libgcc_eh.a
  
  for lib in libatomic \
             libcilkrts \
             libgfortran \
             libgomp \
             libitm \
             libquadmath \
             libsanitizer/{a,l,ub}san \
             libstdc++-v3/src \
             libvtv; do
    make -C $CHOST/$lib DESTDIR=${pkgdir} install-toolexeclibLTLIBRARIES
  done

  [[ $CARCH == "x86_64" ]] && \
    make -C $CHOST/libsanitizer/tsan DESTDIR=${pkgdir} install-toolexeclibLTLIBRARIES

  make -C $CHOST/libobjc DESTDIR=${pkgdir} install-libs
  
  make -C $CHOST/libstdc++-v3/po DESTDIR=${pkgdir} install

  for lib in libgomp \
             libitm \
             libquadmath; do
    make -C $CHOST/$lib DESTDIR=${pkgdir} install-info
  done

  # remove stuff in lib32-gcc-libs and libx32-gcc-libs
  rm -r ${pkgdir}/usr/lib{32,x32}

  # Install Runtime Library Exception
  install -Dm644 ${srcdir}/${_basedir}/COPYING.RUNTIME \
    ${pkgdir}/usr/share/licenses/gcc-libs-multilib-x32/RUNTIME.LIBRARY.EXCEPTION
}

package_gcc-multilib-x32()
{
  pkgdesc="The GNU Compiler Collection - C and C++ frontends for multilib with x32 ABI support"
  depends=("gcc-libs-multilib-x32=$pkgver-$pkgrel" 'binutils>=2.24' 'libmpc' 'cloog')
  groups=('x32-devel')
  options=('staticlibs')
  provides=("gcc=${pkgver//_/-}" "gcc-multilib=${pkgver//_/-}")
  conflicts=('gcc' 'gcc-x32-seed' 'gcc-multilib')
  install=gcc.install

  cd ${srcdir}/gcc-build

  make -C gcc DESTDIR=${pkgdir} install-driver install-cpp install-gcc-ar \
    c++.install-common install-headers install-plugin install-lto-wrapper

  install -m755 gcc/gcov $pkgdir/usr/bin/
  install -m755 -t $pkgdir/${_libdir}/ gcc/{cc1,cc1plus,collect2,lto1}

  make -C $CHOST/libgcc DESTDIR=${pkgdir} install
  make -C $CHOST/32/libgcc DESTDIR=${pkgdir} install
  make -C $CHOST/x32/libgcc DESTDIR=${pkgdir} install
  rm ${pkgdir}/usr/lib{,32,x32}/libgcc_s.so*
  
  make -C $CHOST/libstdc++-v3/src DESTDIR=${pkgdir} install
  make -C $CHOST/libstdc++-v3/include DESTDIR=${pkgdir} install
  make -C $CHOST/libstdc++-v3/libsupc++ DESTDIR=${pkgdir} install
  make -C $CHOST/libstdc++-v3/python DESTDIR=${pkgdir} install
  make -C $CHOST/32/libstdc++-v3/src DESTDIR=${pkgdir} install
  make -C $CHOST/32/libstdc++-v3/include DESTDIR=${pkgdir} install
  make -C $CHOST/32/libstdc++-v3/libsupc++ DESTDIR=${pkgdir} install
  make -C $CHOST/x32/libstdc++-v3/src DESTDIR=${pkgdir} install
  make -C $CHOST/x32/libstdc++-v3/include DESTDIR=${pkgdir} install
  make -C $CHOST/x32/libstdc++-v3/libsupc++ DESTDIR=${pkgdir} install

  install -d $pkgdir/usr/share/gdb/auto-load/usr/lib
  mv $pkgdir/usr/lib/libstdc++.so.6.*-gdb.py \
    $pkgdir/usr/share/gdb/auto-load/usr/lib/
  rm ${pkgdir}/usr/lib{,32,x32}/libstdc++.so*

  make DESTDIR=${pkgdir} install-fixincludes
  make -C gcc DESTDIR=${pkgdir} install-mkheaders
  make -C lto-plugin DESTDIR=${pkgdir} install

  make -C $CHOST/libcilkrts DESTDIR=${pkgdir} install-nodist_toolexeclibHEADERS \
    install-nodist_cilkincludeHEADERS
  make -C $CHOST/libgomp DESTDIR=${pkgdir} install-nodist_toolexeclibHEADERS \
    install-nodist_libsubincludeHEADERS
  make -C $CHOST/libitm DESTDIR=${pkgdir} install-nodist_toolexeclibHEADERS
  make -C $CHOST/libquadmath DESTDIR=${pkgdir} install-nodist_libsubincludeHEADERS
  make -C $CHOST/libsanitizer DESTDIR=${pkgdir} install-nodist_toolexeclibHEADERS
  make -C $CHOST/libsanitizer/asan DESTDIR=${pkgdir} install-nodist_toolexeclibHEADERS
  make -C $CHOST/32/libcilkrts DESTDIR=${pkgdir} install-nodist_toolexeclibHEADERS
  make -C $CHOST/32/libgomp DESTDIR=${pkgdir} install-nodist_toolexeclibHEADERS
  make -C $CHOST/32/libitm DESTDIR=${pkgdir} install-nodist_toolexeclibHEADERS
  make -C $CHOST/32/libsanitizer DESTDIR=${pkgdir} install-nodist_toolexeclibHEADERS
  make -C $CHOST/32/libsanitizer/asan DESTDIR=${pkgdir} install-nodist_toolexeclibHEADERS
  make -C $CHOST/x32/libcilkrts DESTDIR=${pkgdir} install-nodist_toolexeclibHEADERS
  make -C $CHOST/x32/libgomp DESTDIR=${pkgdir} install-nodist_toolexeclibHEADERS
  make -C $CHOST/x32/libitm DESTDIR=${pkgdir} install-nodist_toolexeclibHEADERS
  make -C $CHOST/x32/libsanitizer DESTDIR=${pkgdir} install-nodist_toolexeclibHEADERS
  make -C $CHOST/x32/libsanitizer/asan DESTDIR=${pkgdir} install-nodist_toolexeclibHEADERS

  make -C libiberty DESTDIR=${pkgdir} install
  # install PIC version of libiberty
  install -m644 ${srcdir}/gcc-build/libiberty/pic/libiberty.a ${pkgdir}/usr/lib


  make -C gcc DESTDIR=${pkgdir} install-man install-info
  rm ${pkgdir}/usr/share/man/man1/{gccgo,gfortran}.1
  rm ${pkgdir}/usr/share/info/{gccgo,gfortran,gnat-style,gnat_rm,gnat_ugn}.info

  make -C libcpp DESTDIR=${pkgdir} install
  make -C gcc DESTDIR=${pkgdir} install-po

  # many packages expect this symlink
  ln -s gcc ${pkgdir}/usr/bin/cc

  # POSIX conformance launcher scripts for c89 and c99
  cat > $pkgdir/usr/bin/c89 <<"EOF"
#!/bin/sh
fl="-std=c89"
for opt; do
  case "$opt" in
    -ansi|-std=c89|-std=iso9899:1990) fl="";;
    -std=*) echo "`basename $0` called with non ANSI/ISO C option $opt" >&2
	    exit 1;;
  esac
done
exec gcc $fl ${1+"$@"}
EOF

  cat > $pkgdir/usr/bin/c99 <<"EOF"
#!/bin/sh
fl="-std=c99"
for opt; do
  case "$opt" in
    -std=c99|-std=iso9899:1999) fl="";;
    -std=*) echo "`basename $0` called with non ISO C99 option $opt" >&2
	    exit 1;;
  esac
done
exec gcc $fl ${1+"$@"}
EOF

  chmod 755 $pkgdir/usr/bin/c{8,9}9

  # install the libstdc++ man pages
  make -C $CHOST/libstdc++-v3/doc DESTDIR=$pkgdir doc-install-man

  # Install Runtime Library Exception
  install -d ${pkgdir}/usr/share/licenses/gcc-multilib-x32/
  ln -s ../gcc-libs-multilib-x32/RUNTIME.LIBRARY.EXCEPTION ${pkgdir}/usr/share/licenses/gcc-multilib-x32/
}

package_gcc-fortran-multilib-x32()
{
  pkgdesc="Fortran front-end for GCC for multilib with x32 ABI support"
  depends=("gcc-multilib-x32=$pkgver-$pkgrel")
  provides=("gcc-fortran=${pkgver//_/-}" "gcc-fortran-multilib=${pkgver//_/-}")
  conflicts=('gcc-fortran')
  options=('staticlibs' '!emptydirs')
  install=gcc-fortran.install

  cd ${srcdir}/gcc-build
  make -C $CHOST/libgfortran DESTDIR=$pkgdir install-{{caf,my}execlibLTLIBRARIES,toolexeclibDATA}
  make -C $CHOST/32/libgfortran DESTDIR=$pkgdir install-{{caf,my}execlibLTLIBRARIES,toolexeclibDATA}
  make -C $CHOST/x32/libgfortran DESTDIR=$pkgdir install-{{caf,my}execlibLTLIBRARIES,toolexeclibDATA}
  make -C $CHOST/libgomp DESTDIR=$pkgdir install-nodist_fincludeHEADERS
  make -C gcc DESTDIR=$pkgdir fortran.install-{common,man,info}
  install -Dm755 gcc/f951 $pkgdir/${_libdir}/f951

  ln -s gfortran ${pkgdir}/usr/bin/f95

  # Install Runtime Library Exception
  install -d ${pkgdir}/usr/share/licenses/gcc-fortran-multilib-x32/
  ln -s ../gcc-libs-multilib-x32/RUNTIME.LIBRARY.EXCEPTION ${pkgdir}/usr/share/licenses/gcc-fortran-multilib-x32/
}

package_gcc-objc-multilib-x32()
{
  pkgdesc="Objective-C front-end for GCC for multilib with x32 ABI support"
  depends=("gcc-multilib-x32=$pkgver-$pkgrel")
  provides=("gcc-objc=${pkgver//_/-}" "gcc-objc-multilib=${pkgver//_/-}")
  conflicts=('gcc-objc')

  cd ${srcdir}/gcc-build
  make DESTDIR=$pkgdir -C $CHOST/libobjc install-headers
  install -dm755 $pkgdir/${_libdir}
  install -m755 gcc/cc1obj{,plus} $pkgdir/${_libdir}/

  # Install Runtime Library Exception
  install -d ${pkgdir}/usr/share/licenses/gcc-objc-multilib-x32/
  ln -s ../gcc-libs-multilib-x32/RUNTIME.LIBRARY.EXCEPTION ${pkgdir}/usr/share/licenses/gcc-objc-multilib-x32/
}

package_gcc-ada-multilib-x32()
{
  pkgdesc="Ada front-end for GCC (GNAT) for multilib with x32 ABI support"
  depends=("gcc-multilib-x32=$pkgver-$pkgrel")
  provides=("gcc-ada=${pkgver//_/-}" "gcc-ada-multilib=${pkgver//_/-}")
  conflicts=('gcc-ada')
  options=('staticlibs' '!emptydirs')
  install=gcc-ada.install

  cd ${srcdir}/gcc-build/gcc
  make DESTDIR=$pkgdir ada.install-{common,info}
  install -m755 gnat1 $pkgdir/${_libdir}

  cd ${srcdir}/gcc-build/$CHOST/32/libada
  make DESTDIR=${pkgdir} INSTALL="install" \
    INSTALL_DATA="install -m644" install-gnatlib

  cd ${srcdir}/gcc-build/$CHOST/x32/libada
  make DESTDIR=${pkgdir} INSTALL="install" \
    INSTALL_DATA="install -m644" install-gnatlib

  ln -s gcc ${pkgdir}/usr/bin/gnatgcc

  # insist on dynamic linking, but keep static libraries because gnatmake complains
  mv ${pkgdir}/${_libdir}/adalib/libgna{rl,t}-${_pkgver}.so ${pkgdir}/usr/lib
  ln -s libgnarl-${_pkgver}.so ${pkgdir}/usr/lib/libgnarl.so
  ln -s libgnat-${_pkgver}.so ${pkgdir}/usr/lib/libgnat.so
  rm ${pkgdir}/${_libdir}/adalib/libgna{rl,t}.so

  install -d ${pkgdir}/usr/lib32/
  mv ${pkgdir}/${_libdir}/32/adalib/libgna{rl,t}-${_pkgver}.so ${pkgdir}/usr/lib32
  ln -s libgnarl-${_pkgver}.so ${pkgdir}/usr/lib32/libgnarl.so
  ln -s libgnat-${_pkgver}.so ${pkgdir}/usr/lib32/libgnat.so
  rm ${pkgdir}/${_libdir}/32/adalib/libgna{rl,t}.so

  install -d ${pkgdir}/usr/libx32/
  mv ${pkgdir}/${_libdir}/x32/adalib/libgna{rl,t}-${_pkgver}.so ${pkgdir}/usr/libx32
  ln -s libgnarl-${_pkgver}.so ${pkgdir}/usr/libx32/libgnarl.so
  ln -s libgnat-${_pkgver}.so ${pkgdir}/usr/libx32/libgnat.so
  rm ${pkgdir}/${_libdir}/x32/adalib/libgna{rl,t}.so

  # Install Runtime Library Exception
  install -d ${pkgdir}/usr/share/licenses/gcc-ada-multilib-x32/
  ln -s ../gcc-libs-multilib-x32/RUNTIME.LIBRARY.EXCEPTION ${pkgdir}/usr/share/licenses/gcc-ada-multilib-x32/
}

package_gcc-go-multilib-x32()
{
  pkgdesc="Go front-end for GCC for multilib with x32 ABI support"
  depends=("gcc-multilib-x32=$pkgver-$pkgrel")
  provides=("gcc-go=${pkgver//_/-}" "gcc-go-multilib=${pkgver//_/-}")
  conflicts=('gcc-go')
  options=('staticlibs' '!emptydirs')
  install=gcc-go.install

  cd ${srcdir}/gcc-build
  make -C $CHOST/libgo DESTDIR=$pkgdir install-exec-am
  make -C $CHOST/32/libgo DESTDIR=$pkgdir install-exec-am
  make -C $CHOST/x32/libgo DESTDIR=$pkgdir install-exec-am
  make -C gcc DESTDIR=$pkgdir go.install-{common,man,info}
  install -Dm755 gcc/go1 $pkgdir/${_libdir}/go1

  rm $pkgdir/usr/lib{,32,x32}/libgo.a

  # Install Runtime Library Exception
  install -d ${pkgdir}/usr/share/licenses/gcc-go-multilib-x32/
  ln -s ../gcc-libs-multilib-x32/RUNTIME.LIBRARY.EXCEPTION ${pkgdir}/usr/share/licenses/gcc-go-multilib-x32/
}
