_pkgname=yamllint
pkgname=yamllint
pkgver=1.12.0
pkgrel=1
pkgdesc="A linter for YAML files."
arch=('any')
url="https://github.com/adrienverge/yamllint"
license=('GPLv3')
depends=('python' 'python-yaml' 'python-pathspec' 'python-setuptools')
source=('https://files.pythonhosted.org/packages/d5/9c/aae754b0391ba56540fc88c80e31db95575b96cce87d8c9918f8bcbcb05c/yamllint-1.12.0.tar.gz')
md5sums=('9cb197c3be3340ac73346d78341941a8')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
