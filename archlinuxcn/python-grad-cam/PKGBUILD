# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=grad-cam
pkgname=python-grad-cam
pkgver=1.5.4
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
sha512sums=('30085624117855e2c1f66b0739970d39ab350d8c29489f74960634489a1b876f86158b352c346f56619ca00f140e27deab11251b78408d98cbe63c19b506f292')

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
