_pkgname=yamllint
pkgname=yamllint
pkgver=1.12.1
pkgrel=2
pkgdesc="A linter for YAML files."
arch=('any')
url="https://github.com/adrienverge/yamllint"
license=('GPLv3')
depends=('python' 'python-yaml' 'python-pathspec' 'python-setuptools')
checkdepends=('python-nose')
source=('https://files.pythonhosted.org/packages/14/c2/fd8ac885130ca3d27f1bf5b6cec59aa7c93482680ac871258635c10d30d3/yamllint-1.12.1.tar.gz')
md5sums=('1028e4c8c5fb585186d9241530a7569f')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

check() {
  cd $pkgname-$pkgver
  python -m unittest discover tests
}

# vim:set sw=2 et:
