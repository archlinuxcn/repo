# Maintainer: Butui Hu <hot123tea123@gmail.com>

pkgname=labelme
pkgver=4.5.6
pkgrel=1
pkgdesc='https://github.com/wkentaro/labelme'
arch=('any')
url='https://github.com/open-mmlab/mmcv'
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
sha512sums=('614d13203a19c503a72750dfd911ea3295ef64058762894c9b56c4abd96a8da4240371075de592b86e1cd615b3ce0f4ea995ba60c44649c2e771feedf2c44e28')

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
