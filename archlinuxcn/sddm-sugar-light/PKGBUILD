# Maintainer: peeweep <peeweep at 0x0 dot ee>

pkgname=sddm-sugar-light
pkgver=1.0
pkgrel=1
pkgdesc="The sweetest theme around for SDDM, the Simple Desktop Display Manager."
arch=('any')
url="https://github.com/MarianArlt/sddm-sugar-light"
license=('GPL3')
depends=('sddm' 'qt5-base' 'qt5-quickcontrols2')
install=$pkgname.install
source=("${pkgname}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz")
md5sums=('d2d2cfb31d8010d2ab12755f6ebbf7b7')

package() {
  mkdir -p "${pkgdir}/usr/share/sddm/themes"
  cp -r "${srcdir}/sddm-sugar-light-${pkgver}" "${pkgdir}/usr/share/sddm/themes/sugar-light/"
}
