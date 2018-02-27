# Maintainer: HRKo <ootaharuki99[at]gmail.com>
_skinname='material'
pkgname='fcitx-skin-material'
pkgver=0.3
pkgrel=1
pkgdesc='A Material Design-like skin for Fcitx.'
arch=('any')
url="https://github.com/ootaharuki99/fcitx-skin-material"
license=('Apache')
depends=('fcitx')
source=('https://github.com/ootaharuki99/fcitx-skin-material/archive/v0.3.tar.gz')
md5sums=('a531822d3b15ba007e906853be041d56')

package() {
    install -dm755 ${pkgdir}/usr/share/fcitx/skin/${_skinname}
    install -m644 ${srcdir}/fcitx-skin-material-0.3/material/* ${pkgdir}/usr/share/fcitx/skin/${_skinname}
}
