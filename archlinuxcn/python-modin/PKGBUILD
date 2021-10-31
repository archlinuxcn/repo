# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=modin
pkgname=python-modin
pkgver=0.11.2
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
sha512sums=('e6ccc8d203aeeb9888f698671619f26d193f3a50eb646b4555faa730a7062effdae2b3ab455ef2ad1514c91a87b089e66d94307fccbfec909230cfa331aaa478')

build() {
  cd "${_pkgname}-${pkgver}"
  python setup.py build
}

package() {
  cd "${_pkgname}-${pkgver}"
  python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
}
# vim:set ts=2 sw=2 et:
