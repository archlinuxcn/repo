# Maintainer: Mikael Eriksson <mikael_eriksson@miffe.org>
# Resurected from svn, originaly by
# Maintainer: Allan McRae <allan@archlinux.org>
# Committer: Judd Vinet <jvinet@zeroflux.org>

pkgname=libjpeg6
pkgver=6b1
pkgrel=2
pkgdesc="Library of JPEG support functions"
arch=('i686' 'x86_64')
url="http://www.ijg.org/"
license=('custom')
depends=('glibc')
options=(!makeflags) # Chokes on -jX>1
source=("ftp://ftp.debian.org/debian/pool/main/libj/libjpeg6b/libjpeg6b_$pkgver.orig.tar.gz")
md5sums=('18a8acd0251aca7d4ffd1f62a362d7cc')

build() {
  cd $srcdir/jpeg-$pkgver
  ./configure --prefix=/usr --enable-shared --enable-static
  make
}

package() {
  cd $srcdir/jpeg-$pkgver
  make install DESTDIR=$pkgdir
  # Fix /usr/bin
  for fn in $pkgdir/usr/bin/*; do mv $fn ${fn}6; done
  # Fix /usr/lib
  rm $pkgdir/usr/lib/libjpeg.{a,so,la}
  # Fix /usr/share/man
  for fn in $pkgdir/usr/share/man/man1/*; do mv $fn ${fn%.1}6.1; done
  # Fix /usr/include
  install -dm755 $pkgdir/usr/include/libjpeg6
  mv $pkgdir/usr/include/*.h $pkgdir/usr/include/libjpeg6
  install -Dm644 README $pkgdir/usr/share/licenses/libjpeg6/README
}

# vim:set ts=2 sw=2 et:
