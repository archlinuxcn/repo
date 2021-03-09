# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=gluon-cv
pkgname=python-gluoncv
pkgver=0.10.0
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
sha512sums=('68128d501e591d6e35c3468cb6e900f8447fb5e16752fe0a33a94fceb40bc301d9d0d57495efdd5b31151103568b5fa79cb27df5af43ada5cfe321b27a9ceef4')

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
