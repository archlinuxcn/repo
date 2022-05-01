# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=mmsegmentation
pkgname=python-mmsegmentation
pkgver=0.24.1
pkgrel=1
pkgdesc='OpenMMLab Semantic Segmentation Toolbox and Benchmark'
arch=('any')
url='https://github.com/open-mmlab/mmsegmentation'
license=('Apache')
depends=(
  python-mmcv
  python-numpy
  python-prettytable
)
makedepends=(
  python-setuptools
)
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/open-mmlab/mmsegmentation/archive/v${pkgver}.tar.gz")
sha512sums=('e5235be9bca1b17e8bd7e597d42e37e34c276cfe5136af4cef1f6299ec71e1bdb4f41f156081aa50929f1b50bde6ca4a0127dc8065984f28632c9c9ea05bfdef')

get_pyver() {
  python -c 'import sys; print(str(sys.version_info[0]) + "." + str(sys.version_info[1]))'
}

build() {
  cd "${srcdir}/${_pkgname}-${pkgver}"
  python setup.py build
}

package() {
  cd "${_pkgname}-${pkgver}"
  python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
  # remove unneeded files
  rm -rf "${pkgdir}/usr/lib/python$(get_pyver)/site-packages/tests"
}
# vim:set ts=2 sw=2 et:
