_pkgname=aiomonitor
pkgname=python-aiomonitor
pkgver=0.4.0
pkgrel=1
pkgdesc="aiomonitor adds monitor and python REPL capabilities for asyncio application"
arch=('any')
url="https://github.com/aio-libs/aiomonitor"
license=('Apache')
depends=('python' 'python-aioconsole' 'python-terminaltables' 'python-setuptools')
_name=${pkgname#python-}
source=("https://files.pythonhosted.org/packages/source/${_name::1}/${_name}/${_name}-${pkgver}.tar.gz")
md5sums=('0e81e01a92646697fbc0124580d03649')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
