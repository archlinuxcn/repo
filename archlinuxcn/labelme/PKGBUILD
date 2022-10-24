# Maintainer: Butui Hu <hot123tea123@gmail.com>

pkgname=labelme
pkgver=5.0.4
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
sha512sums=('f406462838eba7036b5e45ce301a0f42a4c2498a6b748d12606314cc9bc26750e8c49664c8438db5195c856af097ea5bd23714d288945cc66bd819fdd794c3ff')

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
