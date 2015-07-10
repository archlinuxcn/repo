# Contributor: lucck <lucck@ep.com.pl>
# Maintainer: aksr <aksr at t-com dot me>
_pkgname=linux-udf
pkgname=udftools
pkgver=1.0.0b3
pkgrel=8
pkgdesc="Linux UDF tools"
url="http://sourceforge.net/projects/linux-udf/"
license=(GPL)
depends=('ncurses' 'readline')
arch=('i686' 'x86_64')
source=("http://downloads.sourceforge.net/sourceforge/${_pkgname}/$pkgname-$pkgver.tar.gz"
        'udftools-1.0.0b3.patch.bz2'
        'gcc4-compile.patch.bz2'
        'udftools-limits.patch.bz2'
        'udftools-open_missing_mode.patch'
        'gcc5-compile-fix.patch')
options=(!libtool)
md5sums=('2f491ddd63f31040797236fe18db9e60'
         '5c760ad80d05ca19a88c6c4f503abc6f'
         '494ddf016b05c65c049406359b3238bf'
         '7f037d997f9e22eba2ecd07ffae4d203'
         'ff606c797dbfc04a07781b5cadf2cb6d'
         '629392c8268752855fe2dbd91295dcbf')
sha1sums=('f1ceaff8dad3ddd5fe55c0b8db804fe7ca3b4308'
          '3f267d2a1f8e737305adf92212570b9ea0ffe85f'
          '1f0e202f055e395380c281a1002d8e9e739904d0'
          '668045c45a429d24596a178a59ca079180297073'
          '84f78a7b1961d6da22ef3bd55d74a06e1ae24c2a'
          '47132788e01576449b503af9f28188d13d2ea7ac')
sha256sums=('c5079e878d4d8e03de0fd75bfecf485a299689b8289a5288f18b2e793e0904a0'
            'bcfd1bcae3085581f53b2b0ef2dcde807fcb9f17397b6a68157ad9e8c71db920'
            'd42bbaa8ad55ef831915540a4b4d74cecea373257b7ad5753a7bf66f2b7be5da'
            '5ec52adfa14a5eea53bfeb6b01bbf9338aa8d838f034235f0c8ac07ed4ddfcd6'
            '8e8df105ddc7b79b00352ab4fab9fb8be202e6764f0508e1799c49ff1e44a7e1'
            'a9f7e3561d14ccec55e15cb14c85e73f78b87829f10e162a9605e31f56282d41')

prepare() {
  cd "$srcdir/$pkgname-$pkgver"
  # pktsetup patch from LFS
  patch -p1 -i "$srcdir/udftools-1.0.0b3.patch"

  # this fixes gcc4 compilation, but don't blame me if it doesn't work
  patch -p1 -i "$srcdir/gcc4-compile.patch"
  patch -p1 -i "$srcdir/udftools-limits.patch"
  
  # https://bugs.gentoo.org/show_bug.cgi?id=232100
  patch -p0 -i "$srcdir/udftools-open_missing_mode.patch"

  # fix for gcc5 compilation
  patch -p0 -i "$srcdir/gcc5-compile-fix.patch"
}

build() {
  cd "$srcdir/$pkgname-$pkgver"
  ./configure --prefix=/usr --mandir=/usr/share/man
  make
}

package() {
  cd "$srcdir/$pkgname-$pkgver"
  make -C "$srcdir/$pkgname-$pkgver" DESTDIR="$pkgdir" install
}

