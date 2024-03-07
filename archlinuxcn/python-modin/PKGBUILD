# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=modin
pkgname=python-modin
pkgver=0.28.0
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
sha512sums=('8d0a36035ccaeda216a4970fd97a73bfb217c3d44dae0e91350de8dbd34418442133c19cfc882149dd866dd4891d8f3a2f0b7a65ee21b75c7bb310e7b5314737')

build() {
  cd "${_pkgname}-${pkgver}"
  python setup.py build
}

package() {
  cd "${_pkgname}-${pkgver}"
  python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
}
# vim:set ts=2 sw=2 et:
