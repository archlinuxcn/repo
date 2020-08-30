# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=gluon-cv
pkgname=python-gluoncv
pkgver=0.8.0
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
sha512sums=('5d7bdd2750c333b4c12c6b88b31e5c4da3782ed8a0703bef0e51a42c06906666efdb51b99a815279371bd7bd9b9590464af55869014bbc9aa5c81cebe0b5a88e')

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
