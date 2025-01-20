# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=timm
pkgname=python-timm
pkgver=1.0.14
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
sha512sums=('44de579ad286b59de8566e2a3a38c7741a4e2e30dd7cf3d1cf078b57f3fc0aceb66a950af2af0d6531da68b077d2cfe22d9d9ad5ac9ffe979e7cb57fea27325f')

build() {
  cd "${_pkgname}-${pkgver}"
  python -m build --wheel --no-isolation
}

package() {
  cd "${_pkgname}-${pkgver}"
  python -m installer --destdir="${pkgdir}" dist/*.whl
}
# vim:set ts=2 sw=2 et:
