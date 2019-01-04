# Maintainer: Patrice Peterson <runiq at archlinux dot us>
# Contributor: David McInnis <dave@dave3.xyz>

pkgname=python-scipy-doc
pkgver=1.2.0
pkgrel=1
pkgdesc="Documentation for SciPy"
makedepends=('unzip')
depends=('bash')
arch=('any')
url='http://docs.scipy.org'
license=('BSD')
source=("$pkgname-$pkgver.zip::https://docs.scipy.org/doc/scipy-$pkgver/scipy-html-$pkgver.zip")
noextract=("$pkgname-$pkgver.zip")
sha256sums=('40e54c58f94a3228305c16f50c2689f51c03862336e772359ab56c5fdb0dcd74')

package()
{
  install -d "$pkgdir/usr/share/doc/python-scipy/html"
  unzip -qd "$pkgdir/usr/share/doc/python-scipy/html" "$srcdir/$pkgname-$pkgver.zip"
  find "$pkgdir/usr/share/doc/python-scipy/html" -type d -exec chmod 755 \{\} \;
  find "$pkgdir/usr/share/doc/python-scipy/html" -type f -exec chmod 644 \{\} \;
  mkdir -p -m 755 "$pkgdir/usr/share/licenses/python-scipy-doc";
  cp "$pkgdir/usr/share/doc/python-scipy/html/dev/licensing.html" \
     "$pkgdir/usr/share/licenses/python-scipy-doc/LICENSE.html";
}
