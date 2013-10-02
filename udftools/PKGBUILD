pkgname=udftools
pkgver=1.0.0b3
pkgrel=7
pkgdesc="Linux UDF tools"
url="http://sourceforge.net/projects/linux-udf/"
license=(GPL)
depends=('ncurses' 'readline')
arch=('i686' 'x86_64')
source=("http://downloads.sourceforge.net/sourceforge/linux-udf/$pkgname-$pkgver.tar.gz"
        udftools-1.0.0b3.patch.bz2
        gcc4-compile.patch.bz2
        udftools-limits.patch.bz2
        udftools-open_missing_mode.patch
)

sha256sums=('c5079e878d4d8e03de0fd75bfecf485a299689b8289a5288f18b2e793e0904a0'
         'bcfd1bcae3085581f53b2b0ef2dcde807fcb9f17397b6a68157ad9e8c71db920'
         'd42bbaa8ad55ef831915540a4b4d74cecea373257b7ad5753a7bf66f2b7be5da'
         '5ec52adfa14a5eea53bfeb6b01bbf9338aa8d838f034235f0c8ac07ed4ddfcd6'
         '8e8df105ddc7b79b00352ab4fab9fb8be202e6764f0508e1799c49ff1e44a7e1')
options=(!libtool)

prepare() {
  cd "$srcdir/$pkgname-$pkgver"
  # pktsetup patch from LFS
  patch -p1 -i "$srcdir/udftools-1.0.0b3.patch"
  # this fixes gcc4 compilation, but don't blame me if it doesn't work
  patch -p1 -i "$srcdir/gcc4-compile.patch"
  patch -p1 -i "$srcdir/udftools-limits.patch"
  
  # https://bugs.gentoo.org/show_bug.cgi?id=232100
  patch -p0 -i "$srcdir/udftools-open_missing_mode.patch"
}

build() {
  cd "$srcdir/$pkgname-$pkgver"
  ./configure --prefix=/usr --mandir=/usr/share/man
  make
}

package() {
  make -C "$srcdir/$pkgname-$pkgver" DESTDIR="$pkgdir" install
}
