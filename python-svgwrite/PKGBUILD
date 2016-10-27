_pkgname=svgwrite
pkgname=python-svgwrite
pkgver=1.1.9
pkgrel=1
pkgdesc="A Python library to create SVG drawings."
arch=('any')
url="http://bitbucket.org/mozman/svgwrite"
license=('MIT')
depends=('python' 'python-pyparsing' 'python-setuptools')
source=('https://pypi.python.org/packages/c7/81/34d72c8dbfe72afdd05bb62f53f90b944b6eee36d7505f190e556903bf87/svgwrite-1.1.9.zip')
md5sums=('50c8d835c23cc4280539ff6717389b05')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"

  python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
