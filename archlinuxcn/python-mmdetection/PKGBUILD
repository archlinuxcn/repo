# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=mmdetection
pkgname=python-mmdetection
pkgver=3.2.0
pkgrel=1
pkgdesc='OpenMMLab Detection Toolbox and Benchmark'
arch=('any')
url='https://github.com/open-mmlab/mmdetection'
license=('Apache')
depends=(
  python-mmcv
  python-numpy
  python-mmpycocotools
  python-pytorch
  python-terminaltables
  python-torchvision
)
makedepends=(
  numactl
  python-build
  python-installer
  python-setuptools
  python-wheel
)
optdepends=(
  python-albumentations
  python-cityscapesscripts
  python-imagecorruptions
  python-mmlvis
)
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/open-mmlab/mmdetection/archive/v${pkgver}.tar.gz")
sha512sums=('55da8d4b949f9c2379b9a98a0e1792734f276888bfb8a5eec3e3a2683ac2db4124e5304ea2778fe9e3b1c95eeccf4e3955c27e20b6585cbdcc67c4b8c02c5f11')

build() {
  cd "${_pkgname}-${pkgver}"
  python -m build --wheel --no-isolation
}

package() {
  cd "${_pkgname}-${pkgver}"
  python -m installer --destdir="${pkgdir}" dist/*.whl
  # delete unused .mim dir
  local site_packages=$(python -c "import site; print(site.getsitepackages()[0])")
  rm -rfv "${pkgdir}${site_packages}/mmdet/.mim"
}
# vim:set ts=2 sw=2 et:
