# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=mmaction2
pkgname=python-mmaction2
pkgver=1.1.0
pkgrel=1
pkgdesc="OpenMMLab's Next Generation Action Understanding Toolbox and Benchmark"
arch=('any')
url='https://github.com/open-mmlab/mmaction2'
license=('Apache')
depends=(
  python-matplotlib
  python-mmcv
  python-numpy
  python-opencv
  python-pillow
  python-pytorch
  python-torchvision
)
makedepends=(
  python-build
  python-installer
  python-setuptools
  python-wheel
)
optdepends=(
  python-av
  python-decord
  python-lmdb
  python-imgaug
  python-onnx
  python-onnxruntime
  python-timm
)
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/open-mmlab/mmaction2/archive/v${pkgver}.tar.gz")
sha512sums=('112d6dcfc3ec7f4e84672328e8060b3880335b2c8df86ae647b7a941523a58a3e0ca8e756e0e1c34fab0afcb9bc63cc3166e9bfb74b568899d83a6fe4fbb072b')

build() {
  cd "${_pkgname}-${pkgver}"
  python -m build --wheel --no-isolation
}

package() {
  cd "${_pkgname}-${pkgver}"
  python -m installer --destdir="${pkgdir}" dist/*.whl
  # delete unused .mim dir
  local site_packages=$(python -c "import site; print(site.getsitepackages()[0])")
  rm -rfv "${pkgdir}${site_packages}/mmaction/.mim"
}
# vim:set ts=2 sw=2 et:
