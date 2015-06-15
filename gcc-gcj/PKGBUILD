# Maintainer: Joey Dumont <joey.dumont@gmail.com>
# Contributor: Renan Manola <rmanola@gmail.com>
# Contributor: Stefan Husmann <stefan-husmann@t-online.de>
# Based on a modified version of the gcc PKGBUILD

pkgname=gcc-gcj
pkgver=5.1.0
_pkgver=5
_islver=0.14.1
_cloogver=0.18.3
pkgrel=1
pkgdesc="The GNU Compiler for Java"
arch=('i686' 'x86_64')
license=('GPL' 'LGPL')
url="http://gcc.gnu.org"
depends=('gtk2' 'libxtst' 'alsa-lib' 'libmpc>=0.8.1' 'classpath' 'gcc-gcj-ecj')
makedepends=('mpfr>=2.4.2' 'elfutils' 'jack' 'zip' 'gcc=5.1.0' 'libart-lgpl')
optdepends=('python2: for running /usr/bin/aot-compile'
  'java-environment: for runnig some jars')
options=('!libtool')
install=$pkgname.install
source=("ftp://gcc.gnu.org/pub/gcc/releases/gcc-${pkgver}/gcc-${pkgver}.tar.bz2"
        "http://isl.gforge.inria.fr/isl-${_islver}.tar.bz2"
	"http://www.bastoul.net/cloog/pages/download/cloog-${_cloogver}.tar.gz")
	
sha512sums=('30f6a94d3adb25bc51fcaddf32a6c41429f569eeb9ed64330445b1296f99998fbfa03277b375be4f7b2b80f519910ef88e4149db7cd9031e2c61a49f501bde94'
            '0d8e04e4a029a1c382357570d0e58b45cff0c89ef576084af3841dda112a1275575fb85f62e7c0ea6e89a4fccf90cae55cdd12c37b824ce5e8845ed6d31edb2d'
            '14fc2af0da62cd17b1a9f5a7a1704da6bfe5dc78639928637588203e61847795a652ff788c313c34b6e7dd85fb329678eb4f72e0e1c9c149be6619ebf046cff8')

prepare() {
  echo "You need at least 10GB of space to compile gcc-gcj,"
  echo "and it will take a lot of time (~ hours)."
  echo "It is better to compile it using makepkg directly."
  sleep 5
  cd "$srcdir"/gcc-${pkgver}

  # Link isl/cloog for in-tree builds
  ln -s ../isl-${_islver} isl
  ln -s ../cloog-${_cloogver} cloog
  
  # Do not install libiberty
  sed -i 's/install_to_$(INSTALL_DEST) //' libiberty/Makefile.in

  # Do not run fixincludes
  sed -i 's@\./fixinc\.sh@-c true@' gcc/Makefile.in
  
  # Arch Linux installs x86_64 libraries /lib
  [[ $CARCH == "x86_64" ]] && sed -i '/m64=/s/lib64/lib/' gcc/config/i386/t-linux64
  
  # Arch uses python version 3 as default python 
  sed -i '1s+python+python2+' libjava/contrib/aot-compile.in

  echo ${pkgver} > gcc/BASE-VER
  [ -d build ] || mkdir build
}

build() {

  cd $srcdir/gcc-$pkgver/build

  ../configure --prefix=/usr --enable-shared --enable-languages=java \
      --enable-threads=posix --mandir=/usr/share/man --infodir=/usr/share/info \
      --enable-__cxa_atexit  --disable-multilib --libdir=/usr/lib \
      --libexecdir=/usr/lib --enable-clocale=gnu --disable-libstdcxx-pch \
      --with-tune=generic --enable-java-awt=gtk --with-java-home="$JAVA_HOME" \
      --enable-libgcj-multifile --disable-plugin --with-system-zlib \
      --enable-cloog-backend=isl
  CPPFLAGS="$CPPFLAGS -O2"
  make 
}

package() {
  cd "$srcdir"/gcc-${pkgver}/build
  make -j1 DESTDIR=${pkgdir} install-target-libjava

  cd gcc
  make -j1 DESTDIR=${pkgdir} java.install-common java.install-man

  install -m755 jc1 ${pkgdir}/usr/lib/gcc/${CHOST}/${pkgver}/
  install -m755 jvgenmain ${pkgdir}/usr/lib/gcc/${CHOST}/${pkgver}/

  # Remove files which belong to the base gcc package
  rm -f ${pkgdir}/usr/bin/{c,g}++
  if [ "${CARCH}" = "x86_64" ]; then
    rm -f ${pkgdir}/usr/bin/x86_64-unknown-linux-gnu-{c,g}++
   else
    rm -f ${pkgdir}/usr/bin/i686-pc-linux-gnu-{c,g}++
  fi
  rm -f ${pkgdir}/usr/man/man1/g++.*
  # Rename two files to not conflict to classpath
  mv ${pkgdir}/usr/share/info/cp-tools.info ${pkgdir}/usr/share/info/cp-tools-gcj.info
  mv ${pkgdir}/usr/share/man/man1/gjdoc.1 ${pkgdir}/usr/share/man/man1/gjdoc.gcj.1
  cd $pkgdir
  [[ $CARCH == "x86_64" ]] && rm usr/lib/libgcc_s.so usr/lib/libgcc_s.so.1 \
    usr/lib/gcc/x86_64-unknown-linux-gnu/$pkgver/crtbegin.o \
    usr/lib/gcc/x86_64-unknown-linux-gnu/$pkgver/crtbeginS.o \
    usr/lib/gcc/x86_64-unknown-linux-gnu/$pkgver/crtbeginT.o \
    usr/lib/gcc/x86_64-unknown-linux-gnu/$pkgver/crtend.o \
    usr/lib/gcc/x86_64-unknown-linux-gnu/$pkgver/crtendS.o \
    usr/lib/gcc/x86_64-unknown-linux-gnu/$pkgver/crtfastmath.o \
    usr/lib/gcc/x86_64-unknown-linux-gnu/$pkgver/crtprec32.o \
    usr/lib/gcc/x86_64-unknown-linux-gnu/$pkgver/crtprec64.o \
    usr/lib/gcc/x86_64-unknown-linux-gnu/$pkgver/crtprec80.o \
    usr/lib/gcc/x86_64-unknown-linux-gnu/$pkgver/include/unwind.h \
    usr/lib/gcc/x86_64-unknown-linux-gnu/$pkgver/libgcc.a \
    usr/lib/gcc/x86_64-unknown-linux-gnu/$pkgver/libgcc_eh.a \
    usr/lib/gcc/x86_64-unknown-linux-gnu/$pkgver/libgcov.a 
  [[ $CARCH == "i686" ]] && rm usr/lib/libgcc_s.so usr/lib/libgcc_s.so.1 \
    usr/lib/gcc/i686-pc-linux-gnu/$pkgver/crtbegin.o \
    usr/lib/gcc/i686-pc-linux-gnu/$pkgver/crtbeginS.o \
    usr/lib/gcc/i686-pc-linux-gnu/$pkgver/crtbeginT.o \
    usr/lib/gcc/i686-pc-linux-gnu/$pkgver/crtend.o \
    usr/lib/gcc/i686-pc-linux-gnu/$pkgver/crtendS.o \
    usr/lib/gcc/i686-pc-linux-gnu/$pkgver/crtfastmath.o \
    usr/lib/gcc/i686-pc-linux-gnu/$pkgver/crtprec32.o \
    usr/lib/gcc/i686-pc-linux-gnu/$pkgver/crtprec64.o \
    usr/lib/gcc/i686-pc-linux-gnu/$pkgver/crtprec80.o \
    usr/lib/gcc/i686-pc-linux-gnu/$pkgver/include/unwind.h \
    usr/lib/gcc/i686-pc-linux-gnu/$pkgver/libgcc.a \
    usr/lib/gcc/i686-pc-linux-gnu/$pkgver/libgcc_eh.a \
    usr/lib/gcc/i686-pc-linux-gnu/$pkgver/libgcov.a 

  find ${pkgdir}/usr/lib -type f -name '*.so.*' -exec strip --strip-unneeded {} \;

  linkdir=`basename $pkgdir/usr/lib/gcj-${pkgver}*`
  ln -sf $linkdir ${pkgdir}/usr/lib/gcj-${pkgver%.?}
  ln -sf libgcj-${pkgver}.jar ${pkgdir}/usr/share/java/libgcj-${pkgver%.?}.jar
  ln -sf libgcj-${pkgver}.jar ${pkgdir}/usr/share/java/libgcj.jar
  ln -sf libgcj-tools-${pkgver}.jar ${pkgdir}/usr/share/java/libgcj-tools-${pkgver%.?}.jar
  ln -sf libgcj-tools-${pkgver}.jar ${pkgdir}/usr/share/java/libgcj-tools.jar
}
