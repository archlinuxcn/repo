# Maintainer: Butui Hu <hot123tea123@gmail.com>

pkgname=labelme
pkgver=7.6.0
pkgrel=1
pkgdesc='Image Polygonal Annotation with Python (polygon, rectangle, circle, line, point and image-level flag annotation).'
arch=('any')
url='https://github.com/wkentaro/labelme'
license=('GPL-3.0-or-later')
depends=(
  gdown
  python-cmap
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
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/wkentaro/labelme/archive/v${pkgver}.tar.gz"
        "labelme.desktop::https://github.com/wkentaro/labelme/raw/refs/tags/v5.6.1/labelme.desktop"
)
sha512sums=('d62ea6d587792f393b6059fe79c4fc3616b0311bb2a8c203bec08d3141ab5d29d71c6df17676363029be753656fad05a2f48d8b301b45c0d53ad4a3ed28cb352'
            '4dfe6a42ed28560e4cc557feead644d2623c0c4a364e2f244d40f670069ed9d64f89017d5425c8cf9db38b6c54bdbb414d863d772200ca8eb5061f56eb7555b1')

build() {
  cd "${srcdir}/${pkgname}-${pkgver}"
  SETUPTOOLS_SCM_PRETEND_VERSION=${pkgver} \
  python -m build --wheel --no-isolation
}

package() {
  cd "${pkgname}-${pkgver}"
  python -m installer --destdir="${pkgdir}" dist/*.whl
  install -Dm644 "labelme/icons/icon-256.png" "${pkgdir}/usr/share/pixmaps/labelme.png"
  install -Dm644 "${srcdir}/labelme.desktop" -t "${pkgdir}/usr/share/applications"
}
# vim:set ts=2 sw=2 et:
