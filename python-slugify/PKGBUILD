# Maintainer: Thomas Jost <schnouki@schnouki.net>
# Contributor: Andrey Mikhaylenko <neithere at gmail dot com>
pkgname=(python-slugify python2-slugify)
pkgbase=python-slugify
pkgver=2.0.1
pkgrel=1
pkgdesc="A Python slugify application that handles unicode"
arch=(any)
url="https://github.com/un33k/python-slugify"
license=('BSD')
makedepends=("python-setuptools" "python2-setuptools")
source=(https://github.com/un33k/python-slugify/archive/${pkgver}.tar.gz)
md5sums=('4d4a370c4d2417bc7ed825ff734af444')
sha256sums=('a63e563d35cb6593e7411e18d9dbf90bd48866b45cb97c88c8cf0eaa14b0cca8')

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
