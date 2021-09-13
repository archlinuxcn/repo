# Maintainer: Fredy García <frealgagu at gmail dot com>
# Contributor: feuri <padfoot at exemail dot com dot au>
# Contributor: feuri <mail at feuri dot de>

pkgname=python-pysdl2
pkgver=0.9.9
pkgrel=1
pkgdesc="Python ctypes wrapper around SDL2"
arch=("any")
url="https://github.com/marcusva/${pkgname/python-py/py-}"
license=("custom:CC0")
depends=("python-setuptools" "sdl2")
optdepends=("sdl2_gfx" "sdl2_image" "sdl2_mixer" "sdl2_ttf")
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/marcusva/${pkgname/python-py/py-}/archive/refs/tags/${pkgver}.tar.gz")
sha256sums=("2b32a4c28369ea52ebb1051b85202e9fd30590fd1a187dde93381f021e005bc3")

package() {
  cd "${srcdir}/${pkgname/python-py/py-}-${pkgver}"
  python setup.py install --root="${pkgdir}"
  install -Dm644 "${srcdir}/${pkgname/python-py/py-}-${pkgver}/doc/copying.rst" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
