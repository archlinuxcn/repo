# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=mmsegmentation
pkgname=python-mmsegmentation
pkgver=1.2.0
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
sha512sums=('36ac82f43366f4cc456ed25b598bd6f20ce731d0d6677ecbec4e17a625ab9aac3abc3075da0f60883da471ac2db063f6f63460535552e0c884fd3aa84b1fb907')

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
