# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=mars
pkgname=python-mars
pkgver=0.10.0
pkgrel=3
pkgdesc='A tensor-based unified framework for large-scale data computation which scales Numpy, pandas, Scikit-learn and Python functions'
arch=('x86_64')
url='https://github.com/mars-project/mars'
license=('Apache-2.0')
depends=(
  gcc-libs
  glibc
  python-arrow
  python-cloudpickle
  python-gevent
  python-jinja
  python-joblib
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
  python-build
  python-installer
  python-setuptools
  python-wheel
)
source=("${_pkgname}-${pkgver}.tar.gz::https://github.com/mars-project/mars/archive/v${pkgver}.tar.gz")
sha512sums=('3291e66610d5d1e1f126deb5e445eed48b856976a6c56ae20372bb328924587ce1f7681177a189929de762e1f81b9ac63537d1d49580085b103e3a96b4082266')

prepare() {
  # fix deps issue
  sed -i '/oldest-supported-numpy/d' "${_pkgname}-${pkgver}/pyproject.toml"
  sed -i '/setuptools/d' "${_pkgname}-${pkgver}/pyproject.toml"
}

build() {
  cd "${_pkgname}-${pkgver}"
  python -m build --wheel --no-isolation
}

package() {
  cd "${_pkgname}-${pkgver}"
  python -m installer --destdir="${pkgdir}" dist/*.whl
}
# vim:set ts=2 sw=2 et:
