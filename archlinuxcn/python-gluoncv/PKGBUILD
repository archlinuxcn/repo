# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=gluon-cv
pkgname=python-gluoncv
pkgver=0.6.0
pkgrel=1
pkgdesc='A Deep Learning Toolkit for Computer Vision'
arch=('any')
url='https://gluon-cv.mxnet.io'
license=('Apache')
depends=(
  'mxnet'
  'python-matplotlib'
  'python-numpy'
  'python-scipy'
)
makedepends=(python-setuptools)
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/dmlc/gluon-cv/archive/v${pkgver}.tar.gz")
sha512sums=('7c18d92a088e9c15d16626178aeea5e17e4c673c21bcd006c8e7dc9006ffc1341c30c7dce0f09e19213beaf81b7a289bd00a50968c7f5831e3c45b345666ccd6')

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
