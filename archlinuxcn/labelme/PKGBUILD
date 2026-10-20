# Maintainer: Butui Hu <hot123tea123@gmail.com>

pkgname=labelme
pkgver=7.9.0
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
sha512sums=('75418d698e481bbd8be0444d89fe0f2a3eebb002809db21908388d113c9e8c3b8385ef012f986c70d185913b15de0de0a3ba5783dbcb2d442f9cca9e7e10f5d2'
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
