# Maintainer: Aviel Warschawski <mail@aviel.org>

pkgname=gdb-multiarch
pkgver=14.2
pkgrel=2
pkgdesc='The GNU Debugger for all gdb supported architectures (i386/arm/mips...)'
arch=(i686 x86_64)
url='http://www.gnu.org/software/gdb/'
license=(GPL3)
makedepends=(glibc gcc-libs texinfo python guile ncurses expat xz mpfr
             source-highlight boost readline)
depends=(glibc ncurses libncursesw.so gcc-libs expat xz mpfr source-highlight gdb-common=$pkgver
         readline libreadline.so guile python libelf)
options=(!emptydirs !lto)
source=(https://ftp.gnu.org/gnu/gdb/gdb-14.2.tar.xz{,.sig})
sha256sums=('2d4dd8061d8ded12b6c63f55e45344881e8226105f4d2a9b234040efa5ce7772'
            'SKIP')
validpgpkeys=('F40ADB902B24264AA42E50BF92EDB04BFF325CF3') # Joel Brobecker <brobecker@adacore.com>

prepare() {
  cd gdb-$pkgver
  sed -i "/ac_cpp=/s/\$CPPFLAGS/\$CPPFLAGS -O2/" libiberty/configure
}

build() {
  cd gdb-$pkgver

  mkdir -p build && cd build
  ../configure \
    --enable-targets=all \
    --prefix=/build \
    --enable-languages=all \
    --enable-multilib \
    --enable-interwork \
    --with-system-readline \
    --disable-nls \
    --with-python=/usr/bin/python \
    --with-system-gdbinit=/etc/gdb/gdbinit

  make
}

package() {
  cd gdb-$pkgver/build

  make DESTDIR="$pkgdir" install

  # Following files conflict with 'gdb' package
  mkdir -p "$pkgdir"/usr/bin
  mv "$pkgdir"/build/bin/gdb "$pkgdir"/usr/bin/gdb-multiarch
  rm -r "$pkgdir"/build
}
