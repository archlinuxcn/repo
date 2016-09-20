_pkgname=yamllint
pkgname=yamllint
pkgver=1.4.0
pkgrel=1
pkgdesc="A linter for YAML files."
arch=('any')
url="https://github.com/adrienverge/yamllint"
license=('GPLv3')
depends=('python' 'python-yaml' 'python-setuptools')
source=('https://pypi.python.org/packages/e7/db/3234bddd65c62e630136bb91ae1ff3aa34aa9f7e93d7e93583591a34d3a7/yamllint-1.4.0.tar.gz')
md5sums=('e99d19a3ad16d46cf34a5de88ecd293c')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"

  python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
