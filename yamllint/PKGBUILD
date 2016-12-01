_pkgname=yamllint
pkgname=yamllint
pkgver=1.6.0
pkgrel=1
pkgdesc="A linter for YAML files."
arch=('any')
url="https://github.com/adrienverge/yamllint"
license=('GPLv3')
depends=('python' 'python-yaml' 'python-setuptools')
source=('https://pypi.python.org/packages/3b/42/4e1342701f3207239c86535b14f0f29e09126feea8bba228b3cb6bdac708/yamllint-1.6.0.tar.gz')
md5sums=('bb0f14c67cfb8d9c5eeb8732dc69bc76')

export LANG=en_US.UTF-8

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"

  python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
