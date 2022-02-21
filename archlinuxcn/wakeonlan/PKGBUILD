# Maintainer: Aaron Fischer <mail@aaron-fischer.net>
# Contributor: danyf90 <daniele.formichelli@gmail.com>
# Contributor: Hyperair <hyperair@gmail.com>

pkgname=wakeonlan
pkgver=0.42
pkgrel=1
pkgdesc="Utility for waking up computers using UDP Wake-on-Lan packets"
arch=('any')
url="https://github.com/jpoliv/wakeonlan/"
license=('GPL')
depends=('perl')
source=("https://github.com/jpoliv/wakeonlan/archive/v$pkgver.tar.gz")
sha512sums=('46ecc7106eefa0b993f0f59eb4e4a593fac7831dffee87c743a7bd757abf366258e99e1efc6742fb3992ee066cb4e280787d0bf3d2db7fb4c88be7c09452da81')
options=(docs)

build() {
  cd $srcdir/$pkgname-$pkgver
  perl Makefile.PL
  make
}

package() {
  cd $srcdir/$pkgname-$pkgver
  install -D -m0755 $pkgname $pkgdir/usr/bin/$pkgname
  install -D -m0644 blib/man1/$pkgname.1p $pkgdir/usr/share/man/man1p/$pkgname.1p
  find examples -exec install -D -m0644 '{}' $pkgdir/usr/share/doc/$pkgname/\{\} \;
}
