# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=modin
pkgname=python-modin
pkgver=0.22.3
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
sha512sums=('4c976f263f93fd1df6f1984556e16b6999c6943c1678e410d828aba5aaf31b39f3ac59f9b4bc414a99f71d5c3c4d468b181a759cecf25330ead7703b9b2bc5b6')

build() {
  cd "${_pkgname}-${pkgver}"
  python setup.py build
}

package() {
  cd "${_pkgname}-${pkgver}"
  python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
}
# vim:set ts=2 sw=2 et:
