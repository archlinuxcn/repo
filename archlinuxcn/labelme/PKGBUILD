# Maintainer: Butui Hu <hot123tea123@gmail.com>

pkgname=labelme
pkgver=5.8.3
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
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/wkentaro/labelme/archive/v${pkgver}.tar.gz"
        "labelme.desktop::https://github.com/wkentaro/labelme/raw/refs/tags/v5.6.1/labelme.desktop"
)
sha512sums=('23e6bac8939fdf45ff844483e55e521369fc8a02211536d1539f5a50288cf4567bd0fed2b08bf56141a0f67113515d76861860c02f4fd1fe302b10e18f717812'
            '4dfe6a42ed28560e4cc557feead644d2623c0c4a364e2f244d40f670069ed9d64f89017d5425c8cf9db38b6c54bdbb414d863d772200ca8eb5061f56eb7555b1')

build() {
  cd "${srcdir}/${pkgname}-${pkgver}"
  SETUPTOOLS_SCM_PRETEND_VERSION=${pkgver} \
  python -m build --wheel --no-isolation
}

package() {
  cd "${pkgname}-${pkgver}"
  python -m installer --destdir="${pkgdir}" dist/*.whl
  install -Dm644 "labelme/icons/icon.png" "${pkgdir}/usr/share/pixmaps/labelme.png"
  install -Dm644 "${srcdir}/labelme.desktop" -t "${pkgdir}/usr/share/applications"
}
# vim:set ts=2 sw=2 et:
