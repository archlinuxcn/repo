# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=mars
pkgname=python-mars
pkgver=0.8.4
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
sha512sums=('e06ecaaf15d7e3809483940b2847b8610ae95da250e4e43df7375b74e5a8b7eac52865155db92b2a4c985e5e9105ab600a6512246ed05d46b5b2a9998e619729')

build() {
  cd "${_pkgname}-${pkgver}"
  python setup.py build
}

package() {
  cd "${_pkgname}-${pkgver}"
  python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
}
# vim:set ts=2 sw=2 et:
