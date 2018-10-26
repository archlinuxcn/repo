# Maintainer: Thomas Jost <schnouki@schnouki.net>
# Contributor: Andrey Mikhaylenko <neithere at gmail dot com>
pkgname=(python-slugify python2-slugify)
pkgbase=python-slugify
pkgver=1.2.6
pkgrel=1
pkgdesc="A Python slugify application that handles unicode"
arch=(any)
url="https://github.com/un33k/python-slugify"
license=('BSD')
makedepends=("python-setuptools" "python2-setuptools")
source=(https://github.com/un33k/python-slugify/archive/${pkgver}.tar.gz)
md5sums=('0d2a4d8433a02fa730444bbb7a0caebb')
sha256sums=('a360fd694bf4b78dedb224324e6c3b05682ff1b0354a95b5f78ba1108f3388f8')

package_python-slugify() {
  depends=("python" "python-unidecode>=0.04.16")
  optdepends=("python-text-unidecode: text-unidecode support")
  cd "$srcdir/$pkgbase-$pkgver"
  python setup.py install --root="$pkgdir" --optimize=1
}

package_python2-slugify() {
  depends=("python2" "python2-unidecode>=0.04.16")
  optdepends=("python2-text-unidecode: text-unidecode support")
  cd "$srcdir/$pkgbase-$pkgver"
  python2 setup.py install --root="$pkgdir" --optimize=1
  mv "$pkgdir/usr/bin/slugify" "$pkgdir/usr/bin/slugify2"
}
