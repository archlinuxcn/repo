# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=timm
pkgname=python-timm
pkgver=1.0.3
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
  python-pdm
  python-setuptools
  python-wheel
)
source=("${_pkgname}-${pkgver}.tar.gz::https://files.pythonhosted.org/packages/source/${_pkgname::1}/${_pkgname}/${_pkgname}-$pkgver.tar.gz")
sha512sums=('46a902b513a9cbf4c642db479501f846aa5691cf28e8cefe655fa3efb1cc328dba73ff7bc3b7c07e0544254214d4c43a8f18e95fa2d199623a7a994c922903b2')

build() {
  cd "${_pkgname}-${pkgver}"
  python -m build --wheel --no-isolation
}

package() {
  cd "${_pkgname}-${pkgver}"
  python -m installer --destdir="${pkgdir}" dist/*.whl
}
# vim:set ts=2 sw=2 et:
