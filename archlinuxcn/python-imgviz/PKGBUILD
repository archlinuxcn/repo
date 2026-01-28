# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=imgviz
pkgname=python-imgviz
pkgver=2.0.0
pkgrel=1
pkgdesc='Image Visualization Tools (object detection, semantic and instance segmentation)'
arch=('any')
url='https://github.com/wkentaro/imgviz'
license=('MIT')
depends=(
  python-matplotlib
  python-numpy
  python-pillow
  python-yaml
)
makedepends=(
  python-build
  python-hatch-fancy-pypi-readme
  python-hatch-vcs
  python-hatchling
  python-installer
  python-setuptools
  python-wheel
)
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/wkentaro/imgviz/archive/v${pkgver}.tar.gz")
sha512sums=('e79d5c72f0fb132462f924d492d582e5c134ac0b61b412a2901bd39b3481a3cce40261cad85406b15cbb42ff33b90e2e3dc78fa7067dacd7bad79880fd6f85a5')

build() {
  cd "${_pkgname}-${pkgver}"
  SETUPTOOLS_SCM_PRETEND_VERSION=${pkgver} \
  python -m build --wheel --no-isolation
}

package() {
  cd "${_pkgname}-${pkgver}"
  python -m installer --destdir="${pkgdir}" dist/*.whl
  install -Dm644 "LICENSE" -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
# vim:set ts=2 sw=2 et:
