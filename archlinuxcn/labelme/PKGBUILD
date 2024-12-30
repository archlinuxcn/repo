# Maintainer: Butui Hu <hot123tea123@gmail.com>

pkgname=labelme
pkgver=5.6.0
pkgrel=1
pkgdesc='Image Polygonal Annotation with Python (polygon, rectangle, circle, line, point and image-level flag annotation).'
arch=('any')
url='https://github.com/wkentaro/labelme'
license=('GPL-3.0-or-later')
depends=(
  gdown
  python-imgviz
  python-matplotlib
  python-natsort
  python-numpy
  python-onnxruntime
  python-pillow
  python-qtpy
  python-scikit-image
  python-termcolor
  python-yaml
)
makedepends=(
  python-build
  python-installer
  python-setuptools
  python-wheel
)
optdepends=(
  "pyside2: use PySide2"
  "pyside6: use PySide6, might not work due to API changes"
  "python-pyqt5: use PyQt5, recommend"
  "python-pyqt6: use PyQt6, might not work due to API changes"
)
install="${pkgname}.install"
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/wkentaro/labelme/archive/v${pkgver}.tar.gz")
sha512sums=('899ba0abc65704c68230bb13e28dc96788e5d088c24e6f23d4a38e29682bbe7d7b08e85cc22b113568ad0e49e50a62e36079c2a7996420aee11adb19a7356689')

build() {
  cd "${srcdir}/${pkgname}-${pkgver}"
  python -m build --wheel --no-isolation
}

package() {
  cd "${pkgname}-${pkgver}"
  python -m installer --destdir="${pkgdir}" dist/*.whl
  install -Dm644 "labelme/icons/icon.png" "${pkgdir}/usr/share/pixmaps/labelme.png"
  install -Dm644 "labelme.desktop" -t "${pkgdir}/usr/share/applications"
}
# vim:set ts=2 sw=2 et:
