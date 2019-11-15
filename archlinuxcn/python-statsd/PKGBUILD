_pkgname=statsd
pkgname=python-statsd
pkgver=3.3.0
pkgrel=2
pkgdesc="A simple statsd client."
arch=('any')
url="https://github.com/jsocol/pystatsd"
license=('MIT')
depends=('python' 'python-setuptools')
_name=${pkgname#python-}
source=("https://files.pythonhosted.org/packages/source/${_name::1}/${_name}/${_pkgname}-${pkgver}.tar.gz")
md5sums=('b397ccf880f37cf099e775907ebf7a46')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
