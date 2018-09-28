# Maintainer: Patrice Peterson <runiq at archlinux dot us>
# Contributor: David McInnis < dave@dave3.xyz>

pkgname=python-scipy-doc
pkgver=1.1.0
pkgrel=1
pkgdesc="Documentation for SciPy"
makedepends=('unzip')
arch=('any')
url='http://docs.scipy.org'
license=('BSD')
source=("$pkgname-$pkgver.zip::https://docs.scipy.org/doc/scipy-$pkgver/scipy-html-$pkgver.zip")
noextract=("$pkgname-$pkgver.zip")
sha256sums=('01fb4c8b2a981f4595035232da6fc53687a8ce6d78cd0efab7f5a27333cbf02f')

package()
{
  install -d "$pkgdir/usr/share/doc/python-scipy/html"
  unzip -qd "$pkgdir/usr/share/doc/python-scipy/html" "$srcdir/$pkgname-$pkgver.zip"
  find "$pkgdir/usr/share/doc/python-scipy/html" -type d -exec chmod 755 \{\} \;
  find "$pkgdir/usr/share/doc/python-scipy/html" -type f -exec chmod 644 \{\} \;
}
