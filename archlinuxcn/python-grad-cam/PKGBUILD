# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=grad-cam
pkgname=python-grad-cam
pkgver=1.5.0
pkgrel=1
pkgdesc='Image Test Time Augmentation with PyTorch'
arch=('any')
url='https://github.com/jacobgil/pytorch-grad-cam/'
license=('MIT')
depends=(
  python-matplotlib
  python-numpy
  python-opencv
  python-pillow
  python-pytorch
  python-scikit-learn
  python-torchvision
  python-tqdm
  python-ttach
)
checkdepends=(
  python-pytest
  python-psutil
)
makedepends=(
  python-build
  python-installer
  python-setuptools
  python-wheel
)
source=("${_pkgname}-${pkgver}.tar.gz::https://files.pythonhosted.org/packages/source/${_pkgname::1}/${_pkgname}/${_pkgname}-${pkgver}.tar.gz")
sha512sums=('9946b74949ed70054816dc34bfa875783aaa822ed98b4ea00a1b2986a56202fea59268ac04a403995ea0d52e68a2700b66a5458ce84627785d19040ba9c332a3')

build() {
  cd "${_pkgname}-${pkgver}"
  python -m build --wheel --no-isolation
}

check() {
  cd "${_pkgname}-${pkgver}"
  # skip this test
  PYTHONPATH=${PWD}/build/lib pytest -v -k "not test_memory_usage_in_loop"
}

package() {
  cd "${_pkgname}-${pkgver}"
  python -m installer --destdir="${pkgdir}" dist/*.whl
  install -Dm644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
# vim:set ts=2 sw=2 et:
