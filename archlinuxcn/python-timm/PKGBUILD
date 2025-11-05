# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=timm
pkgname=python-timm
pkgver=1.0.22
pkgrel=1
pkgdesc='PyTorch Image Models'
arch=('any')
url='https://pypi.org/project/timm/'
license=('Apache-2.0')
depends=(
  python-huggingface-hub
  python-numpy
  python-pillow
  python-pytorch
  python-safetensors
  python-scipy
  python-torchvision
  python-yaml
)
makedepends=(
  python-build
  python-installer
  python-pdm-backend
  python-wheel
)
source=("${_pkgname}-${pkgver}.tar.gz::https://files.pythonhosted.org/packages/source/${_pkgname::1}/${_pkgname}/${_pkgname}-$pkgver.tar.gz")
sha512sums=('c40d0a2b19cd92fd482575b34fa712da2f9c38393175c45f275e5b8bf0154c6f4ca4f83e8832f38260b822c52eae5f7d8be72bbdc9b1f830fd5720ad70e5cc12')

build() {
  cd "${_pkgname}-${pkgver}"
  python -m build --wheel --no-isolation
}

package() {
  cd "${_pkgname}-${pkgver}"
  python -m installer --destdir="${pkgdir}" dist/*.whl
}
# vim:set ts=2 sw=2 et:
