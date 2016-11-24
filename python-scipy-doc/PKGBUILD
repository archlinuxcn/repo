# Maintainer: Patrice Peterson <runiq at archlinux dot us>

pkgname=python-scipy-doc
pkgver=0.18.1
pkgrel=1
pkgdesc="Documentation for SciPy"
makedepends=('unzip')
arch=('any')
url='http://docs.scipy.org'
license=('BSD')
source=("$pkgname-$pkgver.zip::https://docs.scipy.org/doc/scipy/scipy-html-$pkgver.zip")
noextract=("$pkgname-$pkgver.zip")
sha256sums=('b6118abf9af19318b566521c1944d93f0dec57a7e533641348e5338f790e1279')

package()
{
  install -d "$pkgdir/usr/share/doc/python-scipy/html"
  unzip -qd "$pkgdir/usr/share/doc/python-scipy/html" "$srcdir/$pkgname-$pkgver.zip"
  find "$pkgdir/usr/share/doc/python-scipy/html" -type d -exec chmod 755 \{\} \;
  find "$pkgdir/usr/share/doc/python-scipy/html" -type f -exec chmod 644 \{\} \;
}
