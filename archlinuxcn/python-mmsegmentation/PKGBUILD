# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=mmsegmentation
pkgname=python-mmsegmentation
pkgver=1.1.2
pkgrel=1
epoch=1
pkgdesc='OpenMMLab Semantic Segmentation Toolbox and Benchmark'
arch=('any')
url='https://github.com/open-mmlab/mmsegmentation'
license=('Apache')
depends=(
  python-matplotlib
  python-mmpretrain
  python-mmcv
  python-numpy
  python-prettytable
)
makedepends=(
  python-build
  python-installer
  python-setuptools
  python-wheel
)
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/open-mmlab/mmsegmentation/archive/v${pkgver}.tar.gz")
sha512sums=('03a7a62eb516fed21071c40c3f662222b97b29d3961a0ae7f6ad2c51d50ee1152d161358809766a94aeba7857a8d6628a8b23064f41e99d3fa363a3ca54af099')

build() {
  cd "${srcdir}/${_pkgname}-${pkgver}"
  python -m build --wheel --no-isolation
}

package() {
  local site_packages=$(python -c "import site; print(site.getsitepackages()[0])")
  cd "${_pkgname}-${pkgver}"
  python -m installer --destdir="${pkgdir}" dist/*.whl
  # remove unused .mim and tests dir
  rm -rfv "${pkgdir}${site_packages}/mmseg/.mim"
  rm -rfv "${pkgdir}${site_packages}/tests"
}
# vim:set ts=2 sw=2 et:
