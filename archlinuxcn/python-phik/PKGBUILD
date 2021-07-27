# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=PhiK
pkgname=python-phik
pkgver=0.12.0
pkgrel=2
pkgdesc='Phi_K correlation analyzer library'
arch=('x86_64')
url='https://github.com/kaveio/phik'
license=('Apache')
depends=(
  python-joblib
  python-matplotlib
  python-numpy
  python-pandas
  python-scipy
)
checkdepends=(
  jupyter-nbconvert
  python-jupyter_client
  python-pytest
  python-pytest-pylint
)
makedepends=(
  cmake
  pybind11
  python-setuptools
)
source=("${_pkgname}-${pkgver}.tar.gz::https://github.com/KaveIO/PhiK/archive/refs/tags/v${pkgver}.tar.gz")
sha512sums=('648d021e0803dbe48bee3658f685b41da9328382ec5f67a7accc6ae015c5002fb26d85947afabdb72a8590afc400d21a8301e58b8198aafb7e549eeee33f0d22')

get_pyver() {
  python -c 'import sys; print(str(sys.version_info[0]) + "." + str(sys.version_info[1]))'
}

build() {
  cd "${_pkgname}-${pkgver}"
  CMAKE_GENERATOR="Unix Makefiles" python setup.py build
}

check() {
  cd "${_pkgname}-${pkgver}"
  PYTHONPATH="${PWD}/build/lib.linux-${CARCH}-$(get_pyver)" pytest -v
}

package() {
  cd "${_pkgname}-${pkgver}"
  python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
}
# vim:set ts=2 sw=2 et:
