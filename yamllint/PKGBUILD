_pkgname=yamllint
pkgname=yamllint
pkgver=1.8.1
pkgrel=1
pkgdesc="A linter for YAML files."
arch=('any')
url="https://github.com/adrienverge/yamllint"
license=('GPLv3')
depends=('python' 'python-yaml' 'python-setuptools')
source=('https://pypi.python.org/packages/34/a1/f58f12a40f11cbffd7822e6389f4eeb65b76f2e08b4fcdea51b38ddd7059/yamllint-1.8.1.tar.gz')
md5sums=('ee7734f4eb2510709201c1a56ab1e42a')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
