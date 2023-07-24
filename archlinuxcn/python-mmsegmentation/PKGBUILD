# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=mmsegmentation
pkgname=python-mmsegmentation
pkgver=1.1.1
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
sha512sums=('6179f319bc02aa4d2370456eecaef7ed40489af6ea490684812ec74f54da142dd638b44bfb5db0f78e8b469cbd82ef73ed3d0f6aed78552fdd965842d813fbe9')

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
