_pkgname=yamllint
pkgname=yamllint
pkgver=1.5.0
pkgrel=1
pkgdesc="A linter for YAML files."
arch=('any')
url="https://github.com/adrienverge/yamllint"
license=('GPLv3')
depends=('python' 'python-yaml' 'python-setuptools')
source=('https://pypi.python.org/packages/42/ff/1570c386f2940ac34d54ec74820da60f43cae55461919910fab2d539e8a7/yamllint-1.5.0.tar.gz')
md5sums=('e289023a5b95556e06faadcc066ebd89')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"

  python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
