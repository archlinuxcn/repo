# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=timm
pkgname=python-timm
pkgver=1.0.10
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
sha512sums=('1387076be2cadb798852f5e1f436f858f8b820df86cd5a3c157ef805aaa6d22651f63d8e0c7a3c365e45deab9dbc65245a2785d29aac783780d34e1ce46e08ce')

build() {
  cd "${_pkgname}-${pkgver}"
  python -m build --wheel --no-isolation
}

package() {
  cd "${_pkgname}-${pkgver}"
  python -m installer --destdir="${pkgdir}" dist/*.whl
}
# vim:set ts=2 sw=2 et:
