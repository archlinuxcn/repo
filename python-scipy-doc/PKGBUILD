# Maintainer: Patrice Peterson <runiq at archlinux dot us>

pkgname=python-scipy-doc
pkgver=0.16.0
pkgrel=1
pkgdesc="Documentation for SciPy"
makedepends=('unzip')
arch=('any')
url=('http://docs.scipy.org')
license=('BSD')
source=("$pkgname-$pkgver.zip::http://docs.scipy.org/doc/scipy/scipy-html-$pkgver.zip")
noextract=("$pkgname-$pkgver.zip")
sha256sums=('63a967b285723da58b4535b40bdbad616573aefa713da54e19a1cf45857713c0')

package()
{
  install -d "$pkgdir/usr/share/doc/python-scipy/html"
  unzip -qd "$pkgdir/usr/share/doc/python-scipy/html" "$srcdir/$pkgname-$pkgver.zip"
  find "$pkgdir/usr/share/doc/python-scipy/html" -type d -exec chmod 755 \{\} \;
  find "$pkgdir/usr/share/doc/python-scipy/html" -type f -exec chmod 644 \{\} \;
}
