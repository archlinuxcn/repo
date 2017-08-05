# Maintainer: Patrice Peterson <runiq at archlinux dot us>
# Contributor: David McInnis < dave@dave3.xyz>

pkgname=python-scipy-doc
pkgver=0.19.1
pkgrel=1
pkgdesc="Documentation for SciPy"
makedepends=('unzip')
arch=('any')
url='http://docs.scipy.org'
license=('BSD')
source=("$pkgname-$pkgver.zip::https://docs.scipy.org/doc/scipy/scipy-html-$pkgver.zip")
noextract=("$pkgname-$pkgver.zip")
sha256sums=('e123b40d3d550ed55df0f8fbe808ff28f6e4343c3773c553afff508819e800ba')

package()
{
  install -d "$pkgdir/usr/share/doc/python-scipy/html"
  unzip -qd "$pkgdir/usr/share/doc/python-scipy/html" "$srcdir/$pkgname-$pkgver.zip"
  find "$pkgdir/usr/share/doc/python-scipy/html" -type d -exec chmod 755 \{\} \;
  find "$pkgdir/usr/share/doc/python-scipy/html" -type f -exec chmod 644 \{\} \;
}
