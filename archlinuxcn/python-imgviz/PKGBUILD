# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=imgviz
pkgname=python-imgviz
pkgver=1.8.0
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
sha512sums=('1599d9daa9a530e2a692de1758c6f7bb8b7fe7b939dccc3ff48317c471a0103729334fd131c23c34656bc0bf720ca2e6fbf8dd783a6cd6ec0ece8acf28226829')

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
