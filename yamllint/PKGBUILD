_pkgname=yamllint
pkgname=yamllint
pkgver=1.9.0
pkgrel=1
pkgdesc="A linter for YAML files."
arch=('any')
url="https://github.com/adrienverge/yamllint"
license=('GPLv3')
depends=('python' 'python-yaml' 'python-pathspec' 'python-setuptools')
source=('https://pypi.python.org/packages/d4/13/4c9ad3f39a4fc0e06eb849563a455b168acfee84b2d9077bac37fc97b642/yamllint-1.9.0.tar.gz')
md5sums=('ba7c766034f375456fd3055fd22d1a18')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
