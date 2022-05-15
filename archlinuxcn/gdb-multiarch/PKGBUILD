# Maintainer: Aviel Warschawski <mail@aviel.org>

pkgname=gdb-multiarch
pkgver=12.1
pkgrel=1
pkgdesc='The GNU Debugger for all gdb supported architectures (i386/arm/mips...)'
arch=(i686 x86_64)
url='http://www.gnu.org/software/gdb/'
license=(GPL3)
depends=(xz ncurses expat python guile gdb-common=$pkgver)
options=(!emptydirs)
source=(https://ftp.gnu.org/gnu/gdb/gdb-12.1.tar.xz{,.sig})
sha256sums=('0e1793bf8f2b54d53f46dea84ccfd446f48f81b297b28c4f7fc017b818d69fed'
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
    --with-guile=guile-2.2 \
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
