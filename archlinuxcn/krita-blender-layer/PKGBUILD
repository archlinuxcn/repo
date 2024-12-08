# Maintainer: Roald Clark <roaldclark@gmail.com>

_name=BlenderLayer
_pkgname=blender_layer
pkgname=krita-blender-layer
pkgver=1.0.1
pkgrel=1
pkgdesc="A plugin that allows you to stream 3D View from Blender into Krita"
arch=('any')
url="https://github.com/Yuntokon/${_name}"
license=('GPL-3.0-or-later')
depends=(
    'krita'
    'python-pyqt5'
)
install="${pkgname}.install"
source=("${pkgname}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz")
sha256sums=('01c033f69cbf7aa295ea1802e12f3dbdf7960ac4cdabda65230143992f9b41a3')

package() {
    cd "${srcdir}/${_name}-${pkgver}"
    install -d -m 0755 "${pkgdir}/usr/share/krita/pykrita/"
    cp -r {"${_pkgname}","${_pkgname}.desktop"} "${pkgdir}/usr/share/krita/pykrita/"
    install -D -m 0644 "${_pkgname}/${_pkgname}.action" -t "${pkgdir}/usr/share/krita/actions/"
}
