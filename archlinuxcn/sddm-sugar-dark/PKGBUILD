# Maintainer: peeweep <peeweep at 0x0 dot ee>

pkgname=sddm-sugar-dark
pkgver=1.2
pkgrel=1
pkgdesc="The sweetest dark theme around for SDDM, the Simple Desktop Display Manager."
arch=('any')
url="https://github.com/MarianArlt/sddm-sugar-dark"
license=('GPL3')
depends=('qt5-graphicaleffects' 'qt5-quickcontrols2' 'qt5-svg' 'sddm')
install=$pkgname.install
source=("${pkgname}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz")
md5sums=('9a486bfe3e2daeb230a73f9e09576715')

package() {
  mkdir -p "${pkgdir}/usr/share/sddm/themes"
  cp -r "${srcdir}/sddm-sugar-dark-${pkgver}" "${pkgdir}/usr/share/sddm/themes/sugar-dark/"
}
