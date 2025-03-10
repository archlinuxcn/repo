# Maintainer: Butui Hu <hot123tea123@gmail.com>

pkgname=labelme
pkgver=5.7.0
pkgrel=1
pkgdesc='Image Polygonal Annotation with Python (polygon, rectangle, circle, line, point and image-level flag annotation).'
arch=('any')
url='https://github.com/wkentaro/labelme'
license=('GPL-3.0-or-later')
depends=(
  gdown
  python-imgviz
  python-loguru
  python-matplotlib
  python-natsort
  python-numpy
  python-onnxruntime
  python-osam
  python-pillow
  python-pyqt5
  python-scikit-image
  python-yaml
)
makedepends=(
  python-build
  python-hatchling
  python-hatch-fancy-pypi-readme
  python-hatch-vcs
  python-installer
  python-wheel
)
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/wkentaro/labelme/archive/v${pkgver}.tar.gz")
sha512sums=('111874cd11988716b5535170e72a1282528b1a3be48453d403b8db73fb773e9e7c93ad14ef38dc7a2b5a0185d7c4a45c7585a3daff060e99ee4ec14e31278e24')

build() {
  cd "${srcdir}/${pkgname}-${pkgver}"
  SETUPTOOLS_SCM_PRETEND_VERSION=${pkgver} \
  python -m build --wheel --no-isolation
}

package() {
  cd "${pkgname}-${pkgver}"
  python -m installer --destdir="${pkgdir}" dist/*.whl
  install -Dm644 "labelme/icons/icon.png" "${pkgdir}/usr/share/pixmaps/labelme.png"
}
# vim:set ts=2 sw=2 et:
