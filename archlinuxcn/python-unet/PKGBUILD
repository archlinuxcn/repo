# Maintainer: Butui Hu <hot123tea123@gmail.com>

pkgname=python-unet
_pkgname=unet
pkgver=0.7.7
pkgrel=1
pkgdesc='PyTorch Implementation of 2D and 3D U-Net'
arch=(any)
url='https://github.com/fepegar/unet'
license=(MIT)
depends=(
  python-pytorch
)
makedepends=(
  python-setuptools
)
checkdepends=(
  python-pytest
)

source=("${pkgname}-${pkgver}.tar.gz::https://github.com/fepegar/unet/archive/v${pkgver}.tar.gz")
sha512sums=('5d22d7c5131c86868e73af18e928f2a7cb0173d25511ac2d86207791df800e27085a231875f5c191c1c31cc5901b1c128beefc4177a3d9572cb82c809d546a3e')

build() {
  cd "${_pkgname}-${pkgver}"
  python setup.py build
}

check() {
  cd "${_pkgname}-${pkgver}"
  pytest -v .
}

package() {
  cd "${_pkgname}-${pkgver}"
  python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
  install -Dm644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
# vim:set ts=2 sw=2 et:
