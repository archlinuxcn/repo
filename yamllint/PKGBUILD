_pkgname=yamllint
pkgname=yamllint
pkgver=1.3.0
pkgrel=1
pkgdesc="A linter for YAML files."
arch=('any')
url="https://github.com/adrienverge/yamllint"
license=('GPLv3')
depends=('python' 'python-yaml' 'python-setuptools')
source=('https://pypi.python.org/packages/2c/fa/8b6ea8a2998109e55f85b4da093a8b8ca7297e1819dbad155a932f56432b/yamllint-1.3.0.tar.gz')
md5sums=('9e1c71446907b65407d89a3ebe429af5')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"

  python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
