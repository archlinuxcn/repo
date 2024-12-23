# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=mmsegmentation
pkgname=python-mmsegmentation
pkgver=1.2.2
pkgrel=5
epoch=1
pkgdesc='OpenMMLab Semantic Segmentation Toolbox and Benchmark'
arch=('any')
url='https://github.com/open-mmlab/mmsegmentation'
license=('Apache-2.0')
depends=(
  python-matplotlib
  python-mmengine
  python-mmpretrain
  python-mmcv
  python-numpy
  python-opencv
  python-pillow
  python-prettytable
  python-pytorch
  python-scipy
)
makedepends=(
  python-build
  python-installer
  python-setuptools
  python-wheel
)
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/open-mmlab/mmsegmentation/archive/v${pkgver}.tar.gz")
sha512sums=('5a026fbd90a0b2632340aee611b439f116a5875fb3b7f86fb1612a6deea5bfcdda9bbb58e053c825cbe8338470bb773e6b8839ea03e518aa117a80941b0266c0')

prepare() {
sed -i "s/version=get_version()/version='$pkgver'/" "${srcdir}/${_pkgname}-${pkgver}/setup.py"
}

build() {
  cd "${srcdir}/${_pkgname}-${pkgver}"
  python -m build --wheel --no-isolation
}

package() {
  local site_packages=$(python -c "import site; print(site.getsitepackages()[0])")
  cd "${_pkgname}-${pkgver}"
  python -m installer --destdir="${pkgdir}" dist/*.whl
  # remove unused tests dir
  rm -rfv "${pkgdir}${site_packages}/tests"
}
# vim:set ts=2 sw=2 et:
