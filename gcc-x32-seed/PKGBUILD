# $Id: PKGBUILD 138060 2015-08-07 14:12:05Z heftig $
# Maintainer: Jan Alexander Steffens (heftig) <jan.steffens@gmail.com>
# Contributor: Allan McRae <allan@archlinux.org>
# x32 Maintainer: Fantix King <fantix.king@gmail.com>

# toolchain build order: linux-api-headers->glibc->binutils->gcc->binutils->glibc
# NOTE: libtool requires rebuilt with each new gcc version

pkgname='gcc-x32-seed'
pkgver=5.2.0
_pkgver=5
_islver=0.14.1
pkgrel=2.1
#_snapshot=5-20150623
pkgdesc="An incomplete GCC build for building Glibc with x32 ABI support"
arch=('x86_64')
license=('GPL' 'LGPL' 'FDL' 'custom')
url="http://gcc.gnu.org"
makedepends=('binutils>=2.25' 'libmpc' 'doxygen'
             'lib32-glibc>=2.22')
checkdepends=('dejagnu' 'inetutils')
depends=('binutils>=2.24' 'libmpc' 'glibc-x32-seed')
provides=("gcc-multilib-x32=${pkgver}-${pkgrel}")
options=('!emptydirs')
source=(ftp://gcc.gnu.org/pub/gcc/releases/gcc-${pkgver}/gcc-${pkgver}.tar.bz2
        #ftp://gcc.gnu.org/pub/gcc/snapshots/${_snapshot}/gcc-${_snapshot}.tar.bz2
        http://isl.gforge.inria.fr/isl-${_islver}.tar.bz2
        pr66035.patch
        https://sites.google.com/site/x32abi/documents/gcc-x32-seed.tar.bz2)
md5sums=('a51bcfeb3da7dd4c623e27207ed43467'
         '118d1a379abf7606a3334c98a8411c79'
         '5b980076cd5fcbc3aff6014f306282dd'
         '1672d3283e6827b8b8ff634f85ddf523')


if [ -n "${_snapshot}" ]; then
  _basedir=gcc-${_snapshot}
else
  _basedir=gcc-${pkgver}
fi

_libdir="opt/gcc-x32-seed/lib/gcc/$CHOST/${pkgver}"

prepare() {
  if [ ! `zgrep CONFIG_X86_X32=y /proc/config.gz` ]; then
    error "Your current kernel doesn't support X32 ABI!"
    msg2 "You need to install a kernel with CONFIG_X86_X32=y"
    msg2 "linux-pf from AUR for example supports X32 ABI"
    exit 1
  fi

  cd ${srcdir}/${_basedir}

  # link isl for in-tree build
  ln -s ../isl-${_islver} isl

  # Do not run fixincludes
  sed -i 's@\./fixinc\.sh@-c true@' gcc/Makefile.in

  # Arch Linux installs x86_64 libraries /lib
  [[ $CARCH == "x86_64" ]] && sed -i '/m64=/s/lib64/lib/' gcc/config/i386/t-linux64

  echo ${pkgver} > gcc/BASE-VER

  # hack! - some configure tests for header files using "$CPP $CPPFLAGS"
  sed -i "/ac_cpp=/s/\$CPPFLAGS/\$CPPFLAGS -O2/" {libiberty,gcc}/configure

  # https://gcc.gnu.org/bugzilla/show_bug.cgi?id=66035
  patch -p1 -i ${srcdir}/pr66035.patch

  mkdir ${srcdir}/gcc-build
}

build() {
  cd ${srcdir}/gcc-build

  # using -pipe causes spurious test-suite failures
  # http://gcc.gnu.org/bugzilla/show_bug.cgi?id=48565
  CFLAGS=${CFLAGS/-pipe/}
  CXXFLAGS=${CXXFLAGS/-pipe/}

  ${srcdir}/${_basedir}/configure --prefix=/opt/gcc-x32-seed \
      --libdir=/opt/gcc-x32-seed/lib --libexecdir=/opt/gcc-x32-seed/lib \
      --mandir=/opt/gcc-x32-seed/share/man --infodir=/opt/gcc-x32-seed/share/info \
      --with-bugurl=https://bugs.archlinux.org/ \
      --enable-languages=c,c++ \
      --enable-shared --enable-threads=posix --enable-libmpx \
      --with-system-zlib --with-isl --enable-__cxa_atexit \
      --disable-libunwind-exceptions --enable-clocale=gnu \
      --disable-libstdcxx-pch --disable-libssp \
      --enable-gnu-unique-object --enable-linker-build-id \
      --enable-lto --enable-plugin --enable-install-libiberty \
      --with-linker-hash-style=gnu --enable-gnu-indirect-function \
      --enable-multilib --disable-werror \
      --with-multilib-list=m32,m64,mx32 \
      --enable-checking=release \
      --with-default-libstdcxx-abi=gcc4-compatible

  make || true

  rmdir fixincludes || true
  ln -s build-*/fixincludes || true
}

package()
{
  options=('staticlibs')

  cd ${srcdir}/gcc-build

  make -C gcc DESTDIR=${pkgdir} install-driver install-cpp install-gcc-ar \
    c++.install-common install-headers install-plugin install-lto-wrapper

  install -m755 gcc/gcov $pkgdir/opt/gcc-x32-seed/bin/
  install -m755 -t $pkgdir/opt/gcc-x32-seed/bin/ gcc/gcov{,-tool}
  install -m755 -t $pkgdir/${_libdir}/ gcc/{cc1,cc1plus,collect2,lto1}

  make -C $CHOST/libgcc DESTDIR=${pkgdir} install || true
  make -C $CHOST/32/libgcc DESTDIR=${pkgdir} install
  make -C $CHOST/x32/libgcc DESTDIR=${pkgdir} install

  make DESTDIR=${pkgdir} install-fixincludes
  make -C gcc DESTDIR=${pkgdir} install-mkheaders

  make -C lto-plugin DESTDIR=${pkgdir} install
  install -dm755 ${pkgdir}/opt/gcc-x32-seed/lib/bfd-plugins/
  ln -s /opt/gcc-x32-seed/lib/gcc/$CHOST/${pkgver}/liblto_plugin.so \
    ${pkgdir}/opt/gcc-x32-seed/lib/bfd-plugins/

  make -C libiberty DESTDIR=${pkgdir} install
  # install PIC version of libiberty
  install -m644 ${srcdir}/gcc-build/libiberty/pic/libiberty.a ${pkgdir}/opt/gcc-x32-seed/lib


  make -C libcpp DESTDIR=${pkgdir} install

  # many packages expect this symlinks
  ln -s gcc ${pkgdir}/opt/gcc-x32-seed/bin/cc

  # POSIX conformance launcher scripts for c89 and c99
  cat > $pkgdir/opt/gcc-x32-seed/bin/c89 <<"EOF"
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

  cat > $pkgdir/opt/gcc-x32-seed/bin/c99 <<"EOF"
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

  chmod 755 $pkgdir/opt/gcc-x32-seed/bin/c{8,9}9

  # Fix a wrong symbol link
  rm ${pkgdir}/opt/gcc-x32-seed/libx32/libgcc_s.so
  ln -s ../lib/gcc/x86_64-unknown-linux-gnu/4.8.2/x32/libgcc_s.so.1 \
      ${pkgdir}/opt/gcc-x32-seed/libx32/libgcc_s.so

  # Install x32 seed
  install -dm755 ${pkgdir}/opt/gcc-x32-seed/lib/gcc/$CHOST/${pkgver%_*}/x32
  cp ${srcdir}/x32/* ${pkgdir}/opt/gcc-x32-seed/lib/gcc/$CHOST/${pkgver%_*}/x32
}

