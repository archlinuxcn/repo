# Maintainer: Dian M Fay <dian.m.fay@gmail.com>
_name=cobs
pkgname=python-cobs
pkgver=1.2.1
pkgrel=1
pkgdesc="Python library for Consistent Overhead Byte Stuffing (COBS)"
arch=("any")
url="https://pypi.python.org/pypi/$_name"
license=("MIT")
depends=("python")
makedepends=("python-setuptools")
conflicts=("${pkgname}" "${pkgname}-git")
source=("https://files.pythonhosted.org/packages/source/${_name::1}/$_name/$_name-$pkgver.tar.gz")
sha256sums=('2af7f8791cde1ae7c6b936f5d0c35fe29feb10de25f79c15b0af0d6729783cc0')

build() {
  cd "${srcdir}/${_name}-${pkgver}"
  python setup.py build
}

package() {
  cd "${srcdir}/${_name}-${pkgver}"
  python setup.py install --root="${pkgdir}/" --optimize=1 || return 1
}
