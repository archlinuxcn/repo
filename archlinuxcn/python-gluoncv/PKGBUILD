# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=gluon-cv
pkgname=python-gluoncv
pkgver=0.7.0
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
sha512sums=('402feabc6e37b905a2331e1f2dc5df9b0b7c5bf54a657266ecf366b2b826e9a7cb42aaa4f877f45568eb1b32230ed321c6e46815452e4e17744baabe2d8c2686')

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
