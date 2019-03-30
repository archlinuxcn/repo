# Maintainer: Patrice Peterson <runiq at archlinux dot us>
# Contributor: David McInnis <dave@dave3.xyz>

pkgname=python-scipy-doc
pkgver=1.2.1
pkgrel=1
pkgdesc="Documentation for SciPy"
makedepends=('unzip')
depends=('bash')
arch=('any')
url='http://docs.scipy.org'
license=('BSD')
source=("$pkgname-$pkgver.zip::https://docs.scipy.org/doc/scipy-$pkgver/scipy-html-$pkgver.zip")
noextract=("$pkgname-$pkgver.zip")
sha256sums=('1043f18171674d8b22732241421c6f56b19895fcd4753c4010468fabb34f4f86')

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
