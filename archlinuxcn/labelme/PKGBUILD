# Maintainer: Butui Hu <hot123tea123@gmail.com>

pkgname=labelme
pkgver=4.5.10
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
sha512sums=('d3ef4b9bab86be216ce00ef4ba3c9df54182b00b01054202a49666ac871d4ebf798c5c12aa147e9f950e77855bd3adfba2f662907fb8a8b75afe9ec9d93a6aba')

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
