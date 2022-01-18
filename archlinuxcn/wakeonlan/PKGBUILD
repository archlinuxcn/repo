# Maintainer: Aaron Fischer <mail@aaron-fischer.net>
# Contributor: danyf90 <daniele.formichelli@gmail.com>
# Contributor: Hyperair <hyperair@gmail.com>

pkgname=wakeonlan
pkgver=0.41
pkgrel=5
pkgdesc="Utility for waking up computers using UDP Wake-on-Lan packets"
arch=('any')
url="https://github.com/jpoliv/wakeonlan/"
license=('GPL')
depends=('perl')
source=("https://github.com/jpoliv/wakeonlan/archive/wakeonlan-$pkgver.tar.gz")
md5sums=('80182e67cc1ce471463b18a16f5476c4')
options=(docs)

build() {
  cd $srcdir/$pkgname-$pkgname-$pkgver
  perl Makefile.PL
  make
}

package() {
  cd $srcdir/$pkgname-$pkgname-$pkgver
  install -D -m0755 $pkgname $pkgdir/usr/bin/$pkgname
  install -D -m0644 blib/man1/$pkgname.1p $pkgdir/usr/share/man/man1p/$pkgname.1p
  find examples -exec install -D -m0644 '{}' $pkgdir/usr/share/doc/$pkgname/\{\} \;
}
