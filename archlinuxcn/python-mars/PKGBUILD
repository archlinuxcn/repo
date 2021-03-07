# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=mars
pkgname=python-mars
pkgver=0.6.6
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
sha512sums=('733134fe045210726eb34bc4d585c074c29f74b980946f88e0eb8869a78509e87c9d72a17792f755e4af4ee6e1c6acee9ee0a7a0ed07bc4393a96a269c7f8a08')

build() {
  cd "${_pkgname}-${pkgver}"
  python setup.py build
}

package() {
  cd "${_pkgname}-${pkgver}"
  python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
}
# vim:set ts=2 sw=2 et:
