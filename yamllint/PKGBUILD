_pkgname=yamllint
pkgname=yamllint
pkgver=1.3.1
pkgrel=1
pkgdesc="A linter for YAML files."
arch=('any')
url="https://github.com/adrienverge/yamllint"
license=('GPLv3')
depends=('python' 'python-yaml' 'python-setuptools')
source=('https://pypi.python.org/packages/68/ff/5dcffbb2e1f3f05fbc9d087e624299f0a8a8125dd639bac7a7d9c26f8c10/yamllint-1.3.1.tar.gz')
md5sums=('acf5eb5f180e5340542f51a25dacd4e3')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"

  python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
