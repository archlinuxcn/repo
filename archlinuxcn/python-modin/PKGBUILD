# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=modin
pkgname=python-modin
pkgver=0.18.1
pkgrel=1
pkgdesc='Speed up your Pandas workflows by changing a single line of code'
arch=('any')
url='https://github.com/modin-project/modin'
license=(Apache)
depends=(
  python-boto3
  python-cloudpickle
  python-dask
  python-distributed
  python-numpy
  python-pandas
  python-rpyc
)
makedepends=(
  python-setuptools
)
source=("${_pkgname}-${pkgver}.tar.gz::https://github.com/modin-project/modin/archive/${pkgver}.tar.gz")
sha512sums=('4fcc2d1b08636b8cf5d32e928ac0177bf8ede7a5984554ebf860a548bb6ca23e71c6445bcfc265e7580dca56b8c3842d01006eca49d229ef4b5490d7486794d1')

build() {
  cd "${_pkgname}-${pkgver}"
  python setup.py build
}

package() {
  cd "${_pkgname}-${pkgver}"
  python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
}
# vim:set ts=2 sw=2 et:
