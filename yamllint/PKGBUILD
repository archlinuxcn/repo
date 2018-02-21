_pkgname=yamllint
pkgname=yamllint
pkgver=1.11.0
pkgrel=1
pkgdesc="A linter for YAML files."
arch=('any')
url="https://github.com/adrienverge/yamllint"
license=('GPLv3')
depends=('python' 'python-yaml' 'python-pathspec' 'python-setuptools')
source=('https://pypi.python.org/packages/2b/94/0d1fcfe76e2d50bf0b9ab96b2fdd39fa78747757aee4d25829edd5a84664/yamllint-1.11.0.tar.gz')
md5sums=('2bff370e3cf685d47effe79353cc5e50')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
