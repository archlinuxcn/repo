# Maintainer: Fredy García <frealgagu at gmail dot com>
# Contributor: feuri <padfoot at exemail dot com dot au>
# Contributor: feuri <mail at feuri dot de>

pkgname=python-pysdl2
pkgver=0.9.6
pkgrel=4
pkgdesc="Python ctypes wrapper around SDL2"
arch=("any")
url="https://github.com/marcusva/${pkgname/python-py/py-}"
license=("custom:CC0")
depends=("python" "sdl2")
optdepends=("sdl2_gfx" "sdl2_image" "sdl2_mixer" "sdl2_ttf")
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/marcusva/${pkgname/python-py/py-}/archive/rel_${pkgver//./_}.tar.gz")
sha256sums=("50e137cc6078d20d59c7a79883a684a02cbeaa583c9f43ac6bfbcca364236f97")

package() {
  cd "${pkgname/python-py/py-}-rel_${pkgver//./_}"
  python setup.py install --root="${pkgdir}"
  install -Dm644 "doc/copying.rst" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
