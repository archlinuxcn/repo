# Maintainer: Butui Hu <hot123tea123@gmail.com>

pkgname=python-cityscapesscripts
_pkgname=cityscapesscripts
_name=cityscapesScripts
pkgver=2.2.4
pkgrel=1
pkgdesc='README and scripts for the Cityscapes Dataset'
arch=('any')
url='https://github.com/mcordts/cityscapesScripts'
license=('MIT')
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
"LICENSE::https://github.com/mcordts/cityscapesScripts/raw/master/LICENSE")
sha512sums=('99b39235fc1b3d0ae17831701bea09c51dfaa96fc013eef2853efde7342ad674c3c8d40e90fa391985b07508dba4c807a1d2e29a5a26d58ffa1bfe432e0daa0f'
            '1eb9cdac415130b9164ffb3051cd781d6215aedcad87d540914dde96e850dffbad51fb2aa544f961c68665b7343b2068b3ebe165d9fec9386a3c6279a205dd2d')

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
