# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=mmsegmentation
pkgname=python-mmsegmentation
pkgver=0.29.1
pkgrel=1
epoch=1
pkgdesc='OpenMMLab Semantic Segmentation Toolbox and Benchmark'
arch=('any')
url='https://github.com/open-mmlab/mmsegmentation'
license=('Apache')
depends=(
  python-matplotlib
  python-mmclassification
  python-mmcv
  python-numpy
  python-prettytable
)
makedepends=(
  python-setuptools
)
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/open-mmlab/mmsegmentation/archive/v${pkgver}.tar.gz")
sha512sums=('2f3c963cb219eaf6490c0dd356c11ad07ebb4c40461d556b88df98131c6c6579b608d80c7e482bdc79637d69abd3ed6b5ab39da16f323c6d09bf36fbebe92bbf')

build() {
  cd "${srcdir}/${_pkgname}-${pkgver}"
  python setup.py build
}

package() {
  local site_packages=$(python -c "import site; print(site.getsitepackages()[0])")
  cd "${_pkgname}-${pkgver}"
  python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
  # remove unneeded files
  rm -rf "${pkgdir}${site_packages}/tests"
}
# vim:set ts=2 sw=2 et:
