_pkgname=yamllint
pkgname=yamllint
pkgver=1.7.0
pkgrel=1
pkgdesc="A linter for YAML files."
arch=('any')
url="https://github.com/adrienverge/yamllint"
license=('GPLv3')
depends=('python' 'python-yaml' 'python-setuptools')
source=('https://pypi.python.org/packages/c7/e2/08ed3498040e11063d3330831113599a51a028c8e0a4e3bfe86ef730eaa5/yamllint-1.7.0.tar.gz')
md5sums=('1a6e41776a2440d18bd1df5004bd772c')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
