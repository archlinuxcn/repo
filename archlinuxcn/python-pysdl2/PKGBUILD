# Maintainer: Fredy García <frealgagu at gmail dot com>
# Contributor: feuri <padfoot at exemail dot com dot au>
# Contributor: feuri <mail at feuri dot de>

pkgname=python-pysdl2
pkgver=0.9.16
pkgrel=1
pkgdesc="Python ctypes wrapper around SDL2"
arch=("any")
url="https://github.com/marcusva/${pkgname/python-py/py-}"
license=("custom:CC0")
depends=("python-setuptools" "sdl2")
optdepends=("sdl2_gfx" "sdl2_image" "sdl2_mixer" "sdl2_ttf")
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/marcusva/${pkgname/python-py/py-}/archive/refs/tags/${pkgver}.tar.gz")
sha256sums=("0da6b0c041a6197059936f461cc004227e04de148a22f7d0295b2877be000254")

package() {
  cd "${srcdir}/${pkgname/python-py/py-}-${pkgver}"
  python setup.py install --root="${pkgdir}"
  install -Dm644 "${srcdir}/${pkgname/python-py/py-}-${pkgver}/doc/copying.rst" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
