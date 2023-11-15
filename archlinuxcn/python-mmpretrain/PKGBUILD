# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=mmpretrain
pkgname=python-mmpretrain
pkgver=1.1.1
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
sha512sums=('0a43478e370c2b764299c584bdf54072b54d84f8c9af11ad579da7a66c3bccec85cc8a468d37ff318bac63f02494476ae75ac078ecb9e3aff851b35f630eff7b')

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
