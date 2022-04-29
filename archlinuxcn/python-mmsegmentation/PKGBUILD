# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=mmsegmentation
pkgname=python-mmsegmentation
pkgver=0.24.0
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
sha512sums=('486c285b33f41a753f7cd41cb6f7d00b3cc0d3e49d0bcc2d21a586994a22480c42b3549c5b84113f816a097f476c371b9f38070b0c87b360aafcd23e38260fee')

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
