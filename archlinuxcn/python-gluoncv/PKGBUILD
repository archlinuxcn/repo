# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=gluon-cv
pkgname=python-gluoncv
pkgver=0.9.0
pkgrel=1
pkgdesc='A Deep Learning Toolkit for Computer Vision'
arch=('any')
url='https://gluon-cv.mxnet.io'
license=('Apache')
depends=(
  'mxnet'
  'python-matplotlib'
  'python-numpy'
  'python-portalocker'
  'python-requests'
  'python-scipy'
  'python-tqdm'
)
makedepends=(python-setuptools)
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/dmlc/gluon-cv/archive/v${pkgver}.tar.gz")
sha512sums=('5e43c91b9e21a511de844fa96877087e01bbce9f90c29c2ffe11d90249f64ff474297baee507703b64c97ad81f2c803692fae9c8b1cf490d552a6f0317b0926c')

get_pyver() {
  python -c 'import sys; print(str(sys.version_info[0]) + "." + str(sys.version_info[1]))'
}

build() {
  cd ${_pkgname}-${pkgver}
  python setup.py build
}

package() {
  cd "${_pkgname}-${pkgver}"
  python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
  install -Dm644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
# vim:set ts=2 sw=2 et:
