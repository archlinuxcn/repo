# Maintainer: Butui Hu <hot123tea123@gmail.com>

pkgname=python-nvidia-ml-py
_name=nvidia-ml-py
pkgver=12.535.108
pkgrel=1
pkgdesc='Python Bindings for the NVIDIA Management Library'
arch=('any')
url='https://pypi.org/project/nvidia-ml-py'
license=('BSD')
depends=(
  cuda
)
makedepends=(
  python-setuptools
)
source=(
  "${_name}-${pkgver}.tar.gz::https://files.pythonhosted.org/packages/source/${_name::1}/${_name}/${_name}-${pkgver}.tar.gz"
)
sha512sums=('42dbb947d4b6963d2f53b8102bf1705dd1e524f848c3911e186dee038ed075401b9f5a2bd8dc742095aa06713164be54669cb87eaefb819a97093d8b2e8ea81e')

build() {
  cd "${srcdir}/${_name}-${pkgver}"
  python setup.py build
}

package() {
  cd "${srcdir}/${_name}-${pkgver}"
  python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
}
# vim:set ts=2 sw=2 et:
