# Maintainer: HRKo <hrko[at]r-c.dev>
_skinname='material'
pkgname='fcitx-skin-material'
pkgver=0.5
pkgrel=1
pkgdesc='A Material Design-like skin for Fcitx.'
arch=('any')
url="https://github.com/hrko99/fcitx-skin-material"
license=('Apache')
depends=('fcitx')
source=("https://github.com/hrko99/fcitx-skin-material/archive/v${pkgver}.tar.gz")
md5sums=('d75a7dbb3c9a3a257b400c48b4cc91a7')

package() {
    install -dm755 ${pkgdir}/usr/share/fcitx/skin/${_skinname}
    install -m644 ${srcdir}/fcitx-skin-material-${pkgver}/material/* ${pkgdir}/usr/share/fcitx/skin/${_skinname}
}
