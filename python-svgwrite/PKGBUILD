_pkgname=svgwrite
pkgname=python-$_pkgname
pkgver=1.1.6
pkgrel=2
pkgdesc="A Python library to create SVG drawings."
arch=('any')
url="http://bitbucket.org/mozman/svgwrite"
license=('MIT')
depends=('python' 'python-pyparsing' 'python-setuptools')
source=('https://pypi.python.org/packages/source/s/svgwrite/svgwrite-1.1.6.zip')
md5sums=('d57797786f9816617636f06b5566c5f7')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"

  python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
