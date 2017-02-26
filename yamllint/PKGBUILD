_pkgname=yamllint
pkgname=yamllint
pkgver=1.6.1
pkgrel=1
pkgdesc="A linter for YAML files."
arch=('any')
url="https://github.com/adrienverge/yamllint"
license=('GPLv3')
depends=('python' 'python-yaml' 'python-setuptools')
source=('https://pypi.python.org/packages/54/2a/6cffdc51b0c18818d4cee09dfb9048914e21a0a460e3494cad8e25d1955e/yamllint-1.6.1.tar.gz')
md5sums=('18ae98f917441291e103423e032aee6e')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
