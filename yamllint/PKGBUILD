_pkgname=yamllint
pkgname=yamllint
pkgver=1.11.1
pkgrel=1
pkgdesc="A linter for YAML files."
arch=('any')
url="https://github.com/adrienverge/yamllint"
license=('GPLv3')
depends=('python' 'python-yaml' 'python-pathspec' 'python-setuptools')
source=('https://pypi.python.org/packages/70/24/c1db9026a3e4a5d6148344997e97000522833a2a9b9f4a5ba33fae55e45a/yamllint-1.11.1.tar.gz')
md5sums=('37b6878948cba9eb91defdd570793cae')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
