# Maintainer: Tommaso Sardelli <lacapannadelloziotom at gmail dot com>

pkgname=tmux-nord-theme
_pkgname=nord-tmux
pkgver=0.3.0
pkgrel=1
pkgdesc='An arctic, north-bluish clean and elegant tmux color theme.'
arch=('any')
url='https://www.nordtheme.com/ports/tmux'
install=$pkgname.install
license=('MIT')
depends=('tmux')
source=("$pkgname-$pkgver.tar.gz::https://github.com/arcticicestudio/nord-tmux/archive/v${pkgver}.tar.gz")
sha256sums=('5672240fe3251a3e7a4bd41f93a39407e7fbcb91a732744d8e056f893542a26c')

package() {
    cd "${_pkgname}-${pkgver}"
    install -d "${pkgdir}/usr/share/${_pkgname}"
    cp -r * "${pkgdir}/usr/share/${_pkgname}"
    install -Dm 644 LICENSE.md "${pkgdir}/usr/share/licenses/${_pkgname}/LICENSE"
}
