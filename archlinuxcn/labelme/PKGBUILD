# Maintainer: Butui Hu <hot123tea123@gmail.com>

pkgname=labelme
pkgver=5.3.0
pkgrel=1
pkgdesc='Image Polygonal Annotation with Python (polygon, rectangle, circle, line, point and image-level flag annotation).'
arch=('any')
url='https://github.com/wkentaro/labelme'
license=('GPL')
depends=(
  python-imgviz
  python-matplotlib
  python-natsort
  python-numpy
  python-pillow
  python-qtpy
  python-termcolor
  python-yaml
  pyside2
)
makedepends=(
  python-setuptools
)
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/wkentaro/labelme/archive/v${pkgver}.tar.gz")
sha512sums=('e4858c329128feeae4cf528a1411a7822385c5a1b6639e9ef533d507e0fa3b0a09e656ed3e4102ab53e7761deb0455f1edad766d54ee4888cf8ff43b2430207f')

build() {
  cd "${srcdir}/${pkgname}-${pkgver}"
  python setup.py build
}

package() {
  cd "${pkgname}-${pkgver}"
  python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
  install -Dm644 "labelme/icons/icon.png" "${pkgdir}/usr/share/pixmaps/labelme.png"
  install -Dm644 "labelme.desktop" -t "${pkgdir}/usr/share/applications"
  # make labelme use PySide2 by default, PyQt5 is not working
  # see also https://github.com/spyder-ide/qtpy/blob/master/qtpy/__init__.py
  sed -i "3i import PySide2" "${pkgdir}/usr/bin/labelme"
}
# vim:set ts=2 sw=2 et:
