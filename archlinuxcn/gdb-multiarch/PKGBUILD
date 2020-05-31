# Maintainer: Aviel Warschawski <mail@aviel.org>

pkgname=gdb-multiarch
pkgver=9.2
pkgrel=1
pkgdesc='The GNU Debugger for all gdb supported architectures (i386/arm/mips...)'
arch=(i686 x86_64)
url='http://www.gnu.org/software/gdb/'
license=(GPL3)
depends=(xz ncurses expat python guile2.0 gdb-common=$pkgver)
options=(!emptydirs)
source=(https://ftp.gnu.org/gnu/gdb/gdb-9.2.tar.xz{,.sig})
sha256sums=('360cd7ae79b776988e89d8f9a01c985d0b1fa21c767a4295e5f88cb49175c555'
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
    --with-guile=guile-2.0 \
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
