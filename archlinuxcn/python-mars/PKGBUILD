# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=mars
pkgname=python-mars
pkgver=0.7.3
pkgrel=1
pkgdesc='A tensor-based unified framework for large-scale data computation which scales Numpy, pandas, Scikit-learn and Python functions'
arch=('x86_64')
url='https://github.com/mars-project/mars'
license=(Apache)
depends=(
  python-arrow
  python-cloudpickle
  python-gevent
  python-jinja
  python-lz4
  python-numexpr
  python-numpy
  python-pandas
  python-protobuf
  python-psutil
  python-requests
  python-scikit-learn
  python-scipy
  python-sqlalchemy
)
makedepends=(
  cython
  python-setuptools
)
source=("${_pkgname}-${pkgver}.tar.gz::https://github.com/mars-project/mars/archive/v${pkgver}.tar.gz")
sha512sums=('d6d3af51bc8c86feb1e4144c5925af1c7264701625607a02a9397b6859a20512ec872afa70623cbcbc912da0103e51eaa5826d34541d79a0b9d2d46261ef9656')

build() {
  cd "${_pkgname}-${pkgver}"
  python setup.py build
}

package() {
  cd "${_pkgname}-${pkgver}"
  python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
}
# vim:set ts=2 sw=2 et:
