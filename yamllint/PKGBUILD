_pkgname=yamllint
pkgname=yamllint
pkgver=1.3.2
pkgrel=1
pkgdesc="A linter for YAML files."
arch=('any')
url="https://github.com/adrienverge/yamllint"
license=('GPLv3')
depends=('python' 'python-yaml' 'python-setuptools')
source=('https://pypi.python.org/packages/e3/31/1df1511beeb53cea168af60e02e0871b2a4ef42bab3e3812ff948eb6902b/yamllint-1.3.2.tar.gz')
md5sums=('ee6e111cb7d6389a08f2fff8288e55c2')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"

  python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
