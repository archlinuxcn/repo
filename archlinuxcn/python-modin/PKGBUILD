# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=modin
pkgname=python-modin
pkgver=0.28.1
pkgrel=1
pkgdesc='Speed up your Pandas workflows by changing a single line of code'
arch=('any')
url='https://github.com/modin-project/modin'
license=('Apache-2.0')
depends=(
  python-boto3
  python-botocore
  python-cloudpickle
  python-dask
  python-distributed
  python-fsspec
  python-numpy
  python-pandas
  python-psutil
  python-pytz
  python-rpyc
)
makedepends=(
  python-build
  python-installer
  python-setuptools
  python-wheel
)
source=("${_pkgname}-${pkgver}.tar.gz::https://github.com/modin-project/modin/archive/${pkgver}.tar.gz")
sha512sums=('627cfbaf3acb2d563ae2d43be4a6c6a04ccdb7b1ef34ec43590e5be2a69877efa6bfc2bfa54b68a60acd92f6f90b2547b9f85e3ce78224d90a85f5920dd825c6')

build() {
  cd "${_pkgname}-${pkgver}"
  python -m build --wheel --no-isolation
}

package() {
  cd "${_pkgname}-${pkgver}"
  python -m installer --destdir="${pkgdir}" dist/*.whl
}
# vim:set ts=2 sw=2 et:
