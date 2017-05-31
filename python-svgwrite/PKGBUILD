_pkgname=svgwrite
pkgname=python-svgwrite
pkgver=1.1.11
pkgrel=1
pkgdesc="A Python library to create SVG drawings."
arch=('any')
url="http://github.com/mozman/svgwrite.git"
license=('MIT')
depends=('python' 'python-pyparsing' 'python-setuptools')
source=('https://pypi.python.org/packages/69/a5/c5edc66eb5bd9259589b3a379c8aac4084a92cad48fc688b07c1108da272/svgwrite-1.1.11.zip')
md5sums=('106f937fdaafd05945631099d0db27f2')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
