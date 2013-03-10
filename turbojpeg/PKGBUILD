# $Id$
# Maintainer: Allan McRae <allan@archlinux.org>
# Contributor: Simone Sclavi 'Ito' <darkhado@gmail.com>

pkgname=turbojpeg
pkgver=1.2.1
pkgrel=1
pkgdesc="turbojpeg library from libjpeg-turbo"
arch=('i686' 'x86_64')
url="http://www.libjpeg-turbo.org/About/TurboJPEG"
license=('GPL' 'custom')
depends=('glibc' 'libjpeg')
makedepends=('nasm')
options=('!libtool')
source=(http://sourceforge.net/projects/libjpeg-turbo/files/$pkgver/libjpeg-turbo-$pkgver.tar.gz)
sha1sums=('a4992e102c6d88146709e8e6ce5896d5d0b5a361')
 
build() {
  cd "$srcdir/libjpeg-turbo-$pkgver"
 
  ./configure --prefix=/usr --with-jpeg8 --mandir=/usr/share/man
  make
}
 
check() {
  cd "$srcdir/libjpeg-turbo-$pkgver"
 
  make test
}
 
package() {
  cd "$srcdir/libjpeg-turbo-$pkgver"
 
  make DESTDIR="$pkgdir/" install
 
  # only distribute libturbojpeg
  rm -rf "$pkgdir"/usr/share
  rm "$pkgdir"/usr/include/j*.h
  rm "$pkgdir"/usr/lib/libj*
  rm "$pkgdir"/usr/bin/{djpeg,rdjpgcom,wrjpgcom,jpegtran,cjpeg}
 
  install -dm755 "$pkgdir/usr/share/licenses/$pkgname/"
  ln -s ../../doc/libjpeg-turbo/README \
"$pkgdir/usr/share/licenses/$pkgname/README"
  ln -s ../../doc/libjpeg-turbo/README-turbo.txt \
"$pkgdir/usr/share/licenses/$pkgname/README-turbo.txt"
}

