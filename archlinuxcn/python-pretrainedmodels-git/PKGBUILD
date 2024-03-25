# Maintainer: Butui Hu <hot123tea123@gmail.com>
pkgname=python-pretrainedmodels-git
pkgver=r154.8aae3d8
pkgrel=5
pkgdesc="Pretrained ConvNets for PyTorch"
arch=(any)
url="https://github.com/Cadene/pretrained-models.pytorch"
license=('BSD-3-Clause')
depends=(
  python-munch
  python-numpy
  python-pillow
  python-pytorch
  python-scipy
  python-six
  python-torchvision
  python-tqdm
)
makedepends=(
  git
  python-build
  python-installer
  python-setuptools
  python-wheel
)
provides=(python-pretrainedmodels)
conflicts=(python-pretrainedmodels)
source=("${pkgname}::git+https://github.com/Cadene/pretrained-models.pytorch.git")
md5sums=('SKIP')

pkgver() {
  cd "${pkgname}"
  printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
}

build() {
  cd "${pkgname}"
  python -m build --wheel --no-isolation
}

package() {
  cd "${pkgname}"
  python -m installer --destdir="${pkgdir}" dist/*.whl
  install -Dm644 LICENSE.txt -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
# vim:set ts=2 sw=2 et:
