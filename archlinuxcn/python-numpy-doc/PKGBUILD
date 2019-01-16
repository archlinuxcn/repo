# Maintainer: Miguel de Val-Borro <miguel at archlinux dot net>
# Contributor: piggy1983
# Contributor: Patrice Peterson <runiq at archlinux dot us>

pkgname=python-numpy-doc
pkgver=1.15.1
pkgrel=1
pkgdesc="Documentation for NumPy"
makedepends=('unzip')
arch=('any')
url='http://docs.scipy.org'
license=('BSD')
source=("$pkgname-$pkgver.zip::http://docs.scipy.org/doc/numpy-${pkgver}/numpy-html-${pkgver}.zip")
noextract=("$pkgname-$pkgver.zip")
md5sums=('95b5d45d5c7ab7ba43fd1609baeddfc1')

package()
{
  install -d "$pkgdir/usr/share/doc/python-numpy/html"
  unzip -qd "$pkgdir/usr/share/doc/python-numpy/html" "$srcdir/$pkgname-$pkgver.zip"
  find "$pkgdir/usr/share/doc/python-numpy/html" -type d -exec chmod 755 \{\} \;
  find "$pkgdir/usr/share/doc/python-numpy/html" -type f -exec chmod 644 \{\} \;
}
