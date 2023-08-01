# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=mmpretrain
pkgname=python-mmpretrain
pkgver=1.0.1
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
sha512sums=('5f38db78f12af25ddfd893e9b16919df48d6ce67edb46e2cdd4b3ec0904e027c15aa6c5679b53fe699db34f27342ae63ddef3bba200be84b614d29a67334d584')

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
