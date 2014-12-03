# Contributor: piggy1983
# Maintainer: Patrice Peterson <runiq at archlinux dot us>

pkgname=python-numpy-doc
pkgver=1.9.1
pkgrel=1
pkgdesc="Documentation for NumPy"
makedepends=('unzip')
arch=('any')
url=('http://docs.scipy.org')
license=('BSD')
source=("$pkgname-$pkgver.zip::http://docs.scipy.org/doc/numpy/numpy-html-${pkgver}.zip")
noextract=("$pkgname-$pkgver.zip")
md5sums=('8ff2aec1a47e0043be04b77a071871fd')

package()
{
  install -d "$pkgdir/usr/share/doc/python-numpy/html"
  unzip -qd "$pkgdir/usr/share/doc/python-numpy/html" "$srcdir/$pkgname-$pkgver.zip"
  find "$pkgdir/usr/share/doc/python-numpy/html" -type d -exec chmod 755 \{\} \;
  find "$pkgdir/usr/share/doc/python-numpy/html" -type f -exec chmod 644 \{\} \;
}
