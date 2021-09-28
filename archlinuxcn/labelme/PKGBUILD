# Maintainer: Butui Hu <hot123tea123@gmail.com>

pkgname=labelme
pkgver=4.5.12
pkgrel=1
pkgdesc='Image Polygonal Annotation with Python (polygon, rectangle, circle, line, point and image-level flag annotation).'
arch=('any')
url='https://github.com/wkentaro/labelme'
license=('GPL')
depends=(
  python-imgviz
  python-matplotlib
  python-numpy
  python-pillow
  python-qtpy
  python-termcolor
  python-yaml
)
makedepends=(
  python-setuptools
)
optdepends=(
  "pyside2: Qt backend, at least install one Qt backend"
  "python-pyqt5: Qt backend"
)
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/wkentaro/labelme/archive/v${pkgver}.tar.gz")
sha512sums=('7f184c5cf644020c48dca91f067a2bcfaf99b45e9ffe7f804bf9933242c4a35e1d4876eef0a34e1b9e03adcdec397e1a038ec779f70e154376b585394b04ed02')

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
