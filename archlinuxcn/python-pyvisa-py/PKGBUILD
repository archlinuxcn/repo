# Maintainer: Grey Christoforo <first name [at] last name [dot] net>

pkgname=python-pyvisa-py
pkgver=0.3.1
pkgrel=1
pkgdesc="A pure python backend for PyVISA"
arch=('any')
license=('MIT')
depends=('python' 'python-pyvisa')
conflicts=('python-pyvisa-py-git')

_gitproject='pyvisa-py'

source=(https://github.com/pyvisa/pyvisa-py/archive/${pkgver}.tar.gz)
md5sums=('56b8d305a33b3b0965554f6f66dcb6c8')
url="https://github.com/pyvisa/pyvisa-py"

package() {
  cd ${_gitproject}-${pkgver}
  python setup.py install --prefix=/usr --root="$pkgdir/" --optimize=1
}

# vim:set ts=2 sw=2 et:
