# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=grad-cam
pkgname=python-grad-cam
pkgver=1.5.5
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
sha512sums=('ddeecf91c146895706eb627c4c804ea648585cc8a3a3d5f36ef4dca9db5f64dbd2f43ddf9a27253c7ec6194680f55d48bbed0e45f3cfc4b6614f548b140deb3f')

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
