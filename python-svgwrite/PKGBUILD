_pkgname=svgwrite
pkgname=python-svgwrite
pkgver=1.1.12
pkgrel=1
pkgdesc="A Python library to create SVG drawings."
arch=('any')
url="http://github.com/mozman/svgwrite.git"
license=('MIT')
depends=('python' 'python-pyparsing' 'python-setuptools')
source=('https://pypi.python.org/packages/a6/e1/8d592fc801e1dc2958fe0c84c733ed729d4020daa1826c58978f9d601bb4/svgwrite-1.1.12.zip')
md5sums=('05780a4a8ba33c16842faf37818d670e')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
