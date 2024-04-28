# Maintainer: Butui Hu <hot123tea123@gmail.com>

pkgname=python-cityscapesscripts
_pkgname=cityscapesscripts
_name=cityscapesScripts
pkgver=2.2.3
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
sha512sums=('79cdf20da1da7f2acb4eec6498ff1f9d8c7d91cc2382a4c5d0363db7ad54cdec6d0623f18699a20af011f0676633bc52a4bf7a6eaa62b86aae69838ea15a609f'
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
