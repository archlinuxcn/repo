# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=albumentations
pkgname=python-albumentations
pkgver=1.4.15
pkgrel=1
pkgdesc='Fast image augmentation library and easy to use wrapper around other libraries'
arch=('any')
url='https://github.com/albumentations-team/albumentations'
license=('MIT')
depends=(
  python-albucore
  python-numpy
  python-opencv
  python-pydantic
  python-scikit-image
  python-scipy
  python-typing_extensions
  python-yaml
)
makedepends=(
  python-build
  python-installer
  python-setuptools
  python-wheel
)
optdepends=(
  "python-pytorch: for transforms from pytorch"
  "python-torchvision: for transforms from torchvision"
)
source=("${_pkgname}-${pkgver}.tar.gz::https://github.com/albumentations-team/albumentations/archive/${pkgver}.tar.gz")
sha512sums=('812dc6bffbd726f3d9de673a359bf45660d32196d13dcdf3b8333487a06153ebb484da641d17d31b122aed5f8cb2fb5d3662cbcc58b0a8c79abfe2ec0efc5edf')

build() {
  cd "${_pkgname}-${pkgver}"
  python -m build --wheel --no-isolation
}

package() {
  cd "${_pkgname}-${pkgver}"
  python -m installer --destdir="${pkgdir}" dist/*.whl
  install -Dm644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
# vim:set ts=2 sw=2 et:
