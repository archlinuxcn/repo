# Maintainer: lilydjwg <lilydjwg@gmail.com>
_py_pkgname=motor # The pypi package name
pkgname=python-${_py_pkgname}
pkgver=0.1.2
pkgrel=1
pkgdesc="Non-blocking MongoDB driver for Tornado. Python 3 version."
arch=('any')
url="http://pypi.python.org/pypi/${_py_pkgname}"
license=('Apache')
depends=('python-tornado' 'python-pymongo' 'python-greenlet')
source=(http://pypi.python.org/packages/source/m/$_py_pkgname/$_py_pkgname-$pkgver.tar.gz)
md5sums=('f7477ac6c55046b2345bb91dce63fa83')

package() {
  cd "$srcdir/$_py_pkgname-$pkgver"
  python3 setup.py install --root="$pkgdir/" --optimize=1
}

# vim:set ts=2 sw=2 et:
