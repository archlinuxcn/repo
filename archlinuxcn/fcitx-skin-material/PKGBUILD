# Maintainer: HRKo <ootaharuki99[at]gmail.com>
_skinname='material'
pkgname='fcitx-skin-material'
pkgver=0.4
pkgrel=1
pkgdesc='A Material Design-like skin for Fcitx.'
arch=('any')
url="https://github.com/ootaharuki99/fcitx-skin-material"
license=('Apache')
depends=('fcitx')
source=("https://github.com/ootaharuki99/fcitx-skin-material/archive/v${pkgver}.tar.gz")
md5sums=('a10d2da69c04fb57f702d174395fe38c')

package() {
    install -dm755 ${pkgdir}/usr/share/fcitx/skin/${_skinname}
    install -m644 ${srcdir}/fcitx-skin-material-${pkgver}/material/* ${pkgdir}/usr/share/fcitx/skin/${_skinname}
}
