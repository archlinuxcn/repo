# Maintainer: Butui Hu <hot123tea123@gmail.com>

pkgname=python-cityscapesscripts
_pkgname=cityscapesScripts
pkgver=2.1.4
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
sha512sums=('0783ff0bdf6938fb16275ee005a7cfaa0610cbb2b1724830811255b495ba79c47f53b57a6d44f36c06389f5aac67390d36994ddf05611c45095d6d50842f4b43'
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
