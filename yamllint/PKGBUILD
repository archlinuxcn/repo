_pkgname=yamllint
pkgname=yamllint
pkgver=1.8.0
pkgrel=1
pkgdesc="A linter for YAML files."
arch=('any')
url="https://github.com/adrienverge/yamllint"
license=('GPLv3')
depends=('python' 'python-yaml' 'python-setuptools')
source=('https://pypi.python.org/packages/44/80/309b796d2c5e3829cde5c8b4514297687cb0bf33c680a89459c8415c93f0/yamllint-1.8.0.tar.gz')
md5sums=('0b3f3cac216d8fb2db020f1dcae737b0')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
