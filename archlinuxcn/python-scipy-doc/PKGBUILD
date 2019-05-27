# Maintainer: Patrice Peterson <runiq at archlinux dot us>
# Contributor: David McInnis <dave@dave3.xyz>

pkgname=python-scipy-doc
pkgver=1.3.0
pkgrel=1
pkgdesc="Documentation for SciPy"
makedepends=('unzip')
depends=('bash')
arch=('any')
url='http://docs.scipy.org'
license=('BSD')
source=("$pkgname-$pkgver.zip::https://docs.scipy.org/doc/scipy-$pkgver/scipy-html-$pkgver.zip"
        "LICENSE.txt")
noextract=("$pkgname-$pkgver.zip")
sha256sums=('25578792ebb135694d4c50f6dfa9611c4e5d779e505b7b051f9e5203c797ba88'
            'f26cc805d4cd0b234c6296164c03e8fd442f8f63be8f3ffdfa1e7a5e65c40d78')

package()
{
  install -d "$pkgdir/usr/share/doc/python-scipy/html"
  unzip -qd "$pkgdir/usr/share/doc/python-scipy/html" "$srcdir/$pkgname-$pkgver.zip"
  find "$pkgdir/usr/share/doc/python-scipy/html" -type d -exec chmod 755 \{\} \;
  find "$pkgdir/usr/share/doc/python-scipy/html" -type f -exec chmod 644 \{\} \;
  mkdir -p -m 755 "$pkgdir/usr/share/licenses/python-scipy-doc";
  cp "LICENSE.txt" \
     "$pkgdir/usr/share/licenses/python-scipy-doc/LICENSE.txt";
}
