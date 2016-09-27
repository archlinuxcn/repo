# Maintainer: Daniel YC Lin <dlin at gmail>
# Contributor: sssslang <xofyarg at gmail>
# Contributor: kumkee <kumkee at gmail>
pkgname=ccal
pkgver=2.5.3
pkgrel=2
pkgdesc="A console program which writes a calendar together with Chinese calendar to standard output."
arch=('i686' 'x86_64' sh4)
url="http://ccal.chinesebay.com/ccal/ccal.htm"
license=("GPL")
depends=('gcc-libs' 'bash')
makedepends=('gcc')
source=(http://ccal.chinesebay.com/ccal/$pkgname-$pkgver.tar.gz)

build() {
  cd $srcdir/$pkgname-$pkgver
  make
}
package() {
  cd $srcdir/$pkgname-$pkgver
  mkdir -p $pkgdir/{usr/bin,usr/share/man/man1}
  install -c ccal $pkgdir/usr/bin
  install -c ccalpdf $pkgdir/usr/bin
  install -c -m 0644 ccal.1 $pkgdir/usr/share/man/man1
  install -c -m 0644 ccalpdf.1 $pkgdir/usr/share/man/man1
}
sha1sums=('b44d73804ef3ba9129ae196887509f99b508401c')
