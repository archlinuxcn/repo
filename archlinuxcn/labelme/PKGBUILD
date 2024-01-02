# Maintainer: Butui Hu <hot123tea123@gmail.com>

pkgname=labelme
pkgver=5.4.0
pkgrel=1
pkgdesc='Image Polygonal Annotation with Python (polygon, rectangle, circle, line, point and image-level flag annotation).'
arch=('any')
url='https://github.com/wkentaro/labelme'
license=('GPL')
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
sha512sums=('b6b151044a7961f23d9549d8da7b7baf3e21ceabe5287ade984ef2a4c5428b5bdcc1ac584906ba1c1379547cc24bf290c50d517a24de6759c8ce43dff2843272')

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
