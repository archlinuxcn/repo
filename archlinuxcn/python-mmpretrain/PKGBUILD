# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=mmpretrain
pkgname=python-mmpretrain
pkgver=1.1.0
pkgrel=1
pkgdesc='OpenMMLab Pre-training Toolbox and Benchmark'
arch=('any')
url='https://github.com/open-mmlab/mmpretrain'
license=('Apache')
depends=(
  python-einops
  python-matplotlib
  python-mmcv
  python-model-index
  python-numpy
  python-rich
  python-pytorch
)
makedepends=(
  python-build
  python-installer
  python-setuptools
  python-wheel
)
optdepends=(
  python-albumentations
  python-scikit-learn
  python-grad-cam
  python-requests
)
provides=(
  python-mmclassification
)
replaces=(
  python-mmclassification
)
source=("${_pkgname}-${pkgver}.tar.gz::https://github.com/open-mmlab/mmpretrain/archive/refs/tags/v${pkgver}.tar.gz")
sha512sums=('95723f14d25169c62c704eeda2a9f3fd371cdd64f6678fe176df0ebd5d1586689339493bf4f18905c697f0014ac83fba3fb3fee67362e3b78af0d8932317a707')

build() {
  cd "${_pkgname}-${pkgver}"
  python -m build --wheel --no-isolation
}

package() {
  cd "${_pkgname}-${pkgver}"
  python -m installer --destdir="${pkgdir}" dist/*.whl
  # delete unused .mim dir
  local site_packages=$(python -c "import site; print(site.getsitepackages()[0])")
  rm -rfv "${pkgdir}${site_packages}/mmcls/.mim"
}
# vim:set ts=2 sw=2 et:
