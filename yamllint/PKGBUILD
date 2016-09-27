_pkgname=yamllint
pkgname=yamllint
pkgver=1.4.1
pkgrel=1
pkgdesc="A linter for YAML files."
arch=('any')
url="https://github.com/adrienverge/yamllint"
license=('GPLv3')
depends=('python' 'python-yaml' 'python-setuptools')
source=('https://pypi.python.org/packages/ef/c7/4f82f35ac5faa761851929ed33efe218ca3a3170328730446ced6df5b6a2/yamllint-1.4.1.tar.gz')
md5sums=('8627296504845d776d3615087a051312')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"

  python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
