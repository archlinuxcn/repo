# Maintainer: Butui Hu <hot123tea123@gmail.com>

pkgname=labelme
pkgver=5.2.0.post4
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
sha512sums=('94f050da659c1470f2cdb64af9fa592fe24d07b650451580571a48252776e1c9f438d99fa1fdf93b9fd9e4f727daa0cea35369d99580b1f62328be1ec226d43d')

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
