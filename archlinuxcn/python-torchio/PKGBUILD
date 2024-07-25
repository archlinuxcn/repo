# Maintainer: Butui Hu <hot123tea123@gmail.com>

pkgname=python-torchio
_pkgname=torchio
pkgver=0.19.9
pkgrel=1
pkgdesc='Tools for medical image processing in deep learning and PyTorch'
arch=('any')
url='https://github.com/fepegar/torchio'
license=('MIT')
depends=(
  python-click
  python-deprecated
  python-humanize
  python-matplotlib
  python-nibabel
  python-numpy
  python-pytorch
  python-scipy
  python-simpleitk
  python-torchvision
  python-tqdm
)
makedepends=(
  python-build
  python-installer
  python-setuptools
  python-wheel
)

source=("${pkgname}-${pkgver}.tar.gz::https://github.com/fepegar/torchio/archive/v${pkgver}.tar.gz")
sha512sums=('f486c0ce7547601cbeb3d32b3930c70b96a6928236ff88504ce758673d097aaa50d0a4f2897679bf4fb16f9783b934b83f1a1877c1444bf4f2035b4fbde511bb')

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
