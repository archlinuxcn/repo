_pkgname=yamllint
pkgname=python-yamllint
pkgver=1.2.2
pkgrel=1
pkgdesc="A linter for YAML files."
arch=('any')
url="https://github.com/adrienverge/yamllint"
license=('GPLv3')
depends=('python' 'python-setuptools')
source=('https://pypi.python.org/packages/f8/93/e218512496adad4edf8d02a3a00ac7d8fdb82867f4027bfd163ae93748d4/yamllint-1.2.2.tar.gz')
md5sums=('7f36f4929c971795b6a2b5b85998ca40')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"

  python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
