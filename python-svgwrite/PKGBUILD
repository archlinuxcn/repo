_pkgname=svgwrite
pkgname=python-svgwrite
pkgver=1.1.10
pkgrel=1
pkgdesc="A Python library to create SVG drawings."
arch=('any')
url="http://github.com/mozman/svgwrite.git"
license=('MIT')
depends=('python' 'python-pyparsing' 'python-setuptools')
source=('https://pypi.python.org/packages/30/7c/7b6c0a74de3b27e3c478b708f2631818bcb9f179c478eb0713f02a98b87f/svgwrite-1.1.10.zip')
md5sums=('9cefc08e9e756d578893a37940ca4f0f')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
