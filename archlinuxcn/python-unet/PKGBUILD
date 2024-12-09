# Maintainer: Butui Hu <hot123tea123@gmail.com>

pkgname=python-unet
_pkgname=unet
pkgver=0.8.0
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
sha512sums=('456dd4cb25e4b74f6154c5540f8cb25e997f2fffe9b18fde8dfa5e9d7d1fe956bbaa45d2b584550c9ddf5cbe1967f9f9b7a712a18aeb25841e54e7c311296719')

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
