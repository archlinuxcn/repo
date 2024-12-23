# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=mmdetection
pkgname=python-mmdetection
pkgver=3.3.0
pkgrel=5
pkgdesc='OpenMMLab Detection Toolbox and Benchmark'
arch=('any')
url='https://github.com/open-mmlab/mmdetection'
license=('Apache-2.0')
depends=(
  python-addict
  python-matplotlib
  python-mmengine
  python-opencv
  python-pillow
  python-mmcv
  python-numpy
  python-mmpycocotools
  python-pytorch
  python-scipy
  python-six
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
sha512sums=('801abc59d79784ae58b5763c91af051b66bf46d89ea3ef690d627c553868329aa1509a35b199173449163c81739aec28600ca72f1e5f7b5a26c55a52d34ee06f')

prepare() {
  sed -i "s/version=get_version()/version='$pkgver'/" "${srcdir}/${_pkgname}-${pkgver}/setup.py"
}

build() {
  cd "${_pkgname}-${pkgver}"
  python -m build --wheel --no-isolation
}

package() {
  cd "${_pkgname}-${pkgver}"
  python -m installer --destdir="${pkgdir}" dist/*.whl
}
# vim:set ts=2 sw=2 et:
