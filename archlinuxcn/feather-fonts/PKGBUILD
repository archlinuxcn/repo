# Maintainer: Dct Mei <dctxmei@yandex.com>

pkgbase=feather-fonts
pkgname=('otf-feather'
         'ttf-feather')
pkgver=20200330
pkgrel=1
pkgdesc="A font design made for various vector designs"
arch=('any')
url="https://www.dafont.com/feather.font"
license=('custom')
groups=('feather-fonts')
source=("${pkgbase}-${pkgver}.zip::https://dl.dafont.com/dl/?f=feather")
sha256sums=('f58a337874e379e5e9bfcf1f9a30ce48b756bec432a3818a9c49ddfeaacc47a7')

package_otf-feather() {
    cd "${srcdir}"/
    install -Dm 644 'feather dafont.otf' "${pkgdir}"/usr/share/fonts/OTF/Feather.otf
}

package_ttf-feather() {
    cd "${srcdir}"/
    install -Dm 644 'feather dafont.otf' "${pkgdir}"/usr/share/fonts/TTF/Feather.ttf
}
