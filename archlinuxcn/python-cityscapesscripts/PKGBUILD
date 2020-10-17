# Maintainer: Butui Hu <hot123tea123@gmail.com>

pkgname=python-cityscapesscripts
_pkgname=cityscapesScripts
pkgver=2.1.7
pkgrel=1
pkgdesc='README and scripts for the Cityscapes Dataset'
arch=('any')
url='https://github.com/mcordts/cityscapesScripts'
license=('custom')
depends=(
  python-appdirs
  python-matplotlib
  python-numpy
  python-pillow
  python-pyqt5
)
makedepends=(
  python-setuptools
)

source=("${_pkgname}-${pkgver}.tar.gz::https://files.pythonhosted.org/packages/source/${_pkgname::1}/${_pkgname}/${_pkgname}-${pkgver}.tar.gz"
"LICENSE::https://github.com/mcordts/cityscapesScripts/raw/master/license.txt")
sha512sums=('8f93d623a500b7c19a44158f64fb88e781db8c2d55756c6d7fe2fd61435bbaa9e57f5e2b288624db990b4e89c0e8c936e267effb5efc8b33d6344cbf1b1ca020'
            '2b8be7037da1a4609b610fad32f16bd047049270337cecf20d092a6716b01e9435ef5e44dc09ad63b267d30d4ff4011666c62b7055988181ff381af825d046e3')

build() {
  cd "${_pkgname}-${pkgver}"
  python setup.py build
}

package() {
  cd "${_pkgname}-${pkgver}"
  python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
  install -Dm644 "${srcdir}/LICENSE" -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
# vim:set ts=2 sw=2 et:
