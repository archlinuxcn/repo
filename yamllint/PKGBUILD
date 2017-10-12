_pkgname=yamllint
pkgname=yamllint
pkgver=1.8.2
pkgrel=1
pkgdesc="A linter for YAML files."
arch=('any')
url="https://github.com/adrienverge/yamllint"
license=('GPLv3')
depends=('python' 'python-yaml' 'python-pathspec' 'python-setuptools')
source=('https://pypi.python.org/packages/dc/e1/cce57d63761436130f334bda53f26d13054ec37e5611505bb6a8874a952b/yamllint-1.8.2.tar.gz')
md5sums=('337aec60a4ad31e77c049964f391ad9a')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
