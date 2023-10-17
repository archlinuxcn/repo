# Maintainer: Butui Hu <hot123tea123@gmail.com>

pkgname=labelme
pkgver=5.3.1
pkgrel=2
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
  python-setuptools
)
optdepends=(
  "pyside2: use PySide2"
  "pyside6: use PySide6, might not work due to API changes"
  "python-pyqt5: use PyQt5, recommend"
  "python-pyqt6: use PyQt6, might not work due to API changes"
)
install="${pkgname}.install"
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/wkentaro/labelme/archive/v${pkgver}.tar.gz")
sha512sums=('895b8b9cea60074c27c8e41133a370dfe126bb191b6e6f5300e9d5b744c00a1e6842305de7c0aa491b70ec0484dd5e20f0587a31dc4f140a3d4ca1894d154818')

build() {
  cd "${srcdir}/${pkgname}-${pkgver}"
  python setup.py build
}

package() {
  cd "${pkgname}-${pkgver}"
  python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
  install -Dm644 "labelme/icons/icon.png" "${pkgdir}/usr/share/pixmaps/labelme.png"
  install -Dm644 "labelme.desktop" -t "${pkgdir}/usr/share/applications"
}
# vim:set ts=2 sw=2 et:
