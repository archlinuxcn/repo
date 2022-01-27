# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=modin
pkgname=python-modin
pkgver=0.13.0
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
sha512sums=('b4cf4306c45d2413d8ec7f7d215f2ac4cdcd328c25d2ab8879d697b493ea6b5f9887aaf0391d04b669a35a7fb720f2952d00d83d01ba9ef5c3b6cd851ff3cf86')

build() {
  cd "${_pkgname}-${pkgver}"
  python setup.py build
}

package() {
  cd "${_pkgname}-${pkgver}"
  python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
}
# vim:set ts=2 sw=2 et:
