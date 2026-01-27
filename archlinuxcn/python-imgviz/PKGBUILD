# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=imgviz
pkgname=python-imgviz
pkgver=2.0.0a1
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
sha512sums=('5461a7d75fde600d8478324ca673ce741bb2cdd5acb0e94299c2fc053ab8a76ed03e3c4f180715db9f237bd7413964fbac0c7886e88dd6cb6291ef797e66cc88')

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
