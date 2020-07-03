# Maintainer: Ralph Plawetzki <ralph@purejava.org>

pkgname=acpitool
pkgver=0.5.1
pkgrel=6
pkgdesc="ACPI client - replacement for apm tool"
url="http://sourceforge.net/projects/acpitool/"
arch=('i686' 'x86_64')
license=('GPL')
depends=('gcc-libs')
source=(http://downloads.sourceforge.net/sourceforge/acpitool/acpitool-$pkgver.tar.bz2
	linux-3.0.patch
	sysfs-battery.patch
  0001-Use-dynamic-structures-instead-of-predefined-ones.patch)
md5sums=('9e4ec55201be0be71ffbc56d38b42b57'
         'eb149edb32be6cdf20a7d16beb3e9f70'
         '969fc4929cc215756db27168646c2b7a'
         'e5baf736eac5b030355533782660c92b')

build() {
  cd "$srcdir/$pkgname-$pkgver"
  patch -p1 <$srcdir/linux-3.0.patch
  patch -p1 <$srcdir/sysfs-battery.patch
  patch -p1 <$srcdir/0001-Use-dynamic-structures-instead-of-predefined-ones.patch
  ./configure --prefix=/usr
  make
}

package() {
  cd "$srcdir/$pkgname-$pkgver"
  make prefix="$pkgdir/usr" install
}
