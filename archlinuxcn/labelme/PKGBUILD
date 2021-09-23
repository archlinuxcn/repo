# Maintainer: Butui Hu <hot123tea123@gmail.com>

pkgname=labelme
pkgver=4.5.11
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
sha512sums=('e6845a227ecd13b7adf5352a8b9759377458985bb8e889971513e3d0872dfc0999c3abbac5c13c739428617a666683e87cdf4d47ef81e7a77a0a02a9f4d3f933')

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
