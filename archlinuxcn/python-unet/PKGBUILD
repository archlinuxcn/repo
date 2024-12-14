# Maintainer: Butui Hu <hot123tea123@gmail.com>

pkgname=python-unet
_pkgname=unet
pkgver=0.8.1
pkgrel=1
pkgdesc='PyTorch Implementation of 2D and 3D U-Net'
arch=(any)
url='https://github.com/fepegar/unet'
license=(MIT)
depends=(
  python-pytorch
)
makedepends=(
  python-build
  python-hatchling
  python-installer
  python-setuptools
  python-wheel
)
checkdepends=(
  python-pytest
)

source=("${pkgname}-${pkgver}.tar.gz::https://github.com/fepegar/unet/archive/v${pkgver}.tar.gz")
sha512sums=('582761e5314af17ed5fc4a920df5a806107ca4be82d3cf43888665ff05e4cedf4c7dbde6d948ba7a5160a0453f1ad9795cfde7310ca3ea8c70e7b1902cc01c1e')

build() {
  cd "${_pkgname}-${pkgver}"
  python -m build --wheel --no-isolation
}

check() {
  cd "${_pkgname}-${pkgver}"
  pytest -v .
}

package() {
  cd "${_pkgname}-${pkgver}"
  python -m installer --destdir="${pkgdir}" dist/*.whl
  install -Dm644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
# vim:set ts=2 sw=2 et:
