_pkgname=yamllint
pkgname=yamllint
pkgver=1.10.0
pkgrel=1
pkgdesc="A linter for YAML files."
arch=('any')
url="https://github.com/adrienverge/yamllint"
license=('GPLv3')
depends=('python' 'python-yaml' 'python-pathspec' 'python-setuptools')
source=('https://pypi.python.org/packages/47/b9/512bbd1b8ee92196548d56eba7ca1242f5eb14255fa44f772399abdb9bde/yamllint-1.10.0.tar.gz')
md5sums=('d81360927150d330c445e4cd1aec66c0')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
