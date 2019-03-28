# Maintainer: Thomas Jost <schnouki@schnouki.net>
# Contributor: Andrey Mikhaylenko <neithere at gmail dot com>
pkgname=(python-slugify python2-slugify)
pkgbase=python-slugify
pkgver=3.0.1
pkgrel=1
pkgdesc="A Python slugify application that handles unicode"
arch=(any)
url="https://github.com/un33k/python-slugify"
license=('BSD')
makedepends=("python-setuptools" "python2-setuptools")
source=(https://github.com/un33k/python-slugify/archive/${pkgver}.tar.gz)
md5sums=('7f873c723703729426e5f303d9eaa9b2')
sha256sums=('32b9c416ee5be1f8131352575df51e86862845799404fcce8dee269498402635')

package_python-slugify() {
  depends=("python" "python-text-unidecode")
  optdepends=("python-unidecode: Unidecode support")
  cd "$srcdir/$pkgbase-$pkgver"
  python setup.py install --root="$pkgdir" --optimize=1
}

package_python2-slugify() {
  depends=("python2" "python2-text-unidecode")
  optdepends=("python2-unidecode: Unidecode support")
  cd "$srcdir/$pkgbase-$pkgver"
  python2 setup.py install --root="$pkgdir" --optimize=1
  mv "$pkgdir/usr/bin/slugify" "$pkgdir/usr/bin/slugify2"
}
