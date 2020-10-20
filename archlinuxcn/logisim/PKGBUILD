# Maintainer: Marcel Korpel <marcel[dot]korpel[at]gmail>
# Contributor: Renan Birck <renan.ee.ufsm at gmail.com>
 
pkgname=logisim
_truepkgname=logisim-generic
pkgver=2.7.1
pkgrel=7
pkgdesc='An educational tool for designing and simulating digital logic circuits'
arch=('any')
url="http://www.cburch.com/logisim/"
license=('GPL2')
depends=('sh' 'java-runtime' 'gtk-update-icon-cache' 'desktop-file-utils' 'shared-mime-info')
install=${pkgname}.install
source=(http://downloads.sourceforge.net/sourceforge/circuit/${_truepkgname}-${pkgver}.jar
        ${pkgname}.xml
        ${pkgname}.desktop
        ${pkgname}.sh)
sha256sums=('362a78c12ad18c203fed868872c4a01cd9c12141379d92e892bbe2c37e627bc2'
            '9dd50eb99edeff5f74247ae9b050d56c1366818ea80fbdcc6c5e24bfabfec5c0'
            '4d5ae9f9d5f5789469f3580a81ee568ca426f324df3ba37d7e4c8d6b20dc638c'
            '56eaac407f6ae64289ab228269edb8b1a2bbe647e2baf5dfab7f481c9db8e680')

package() {
  cd "$srcdir"

  install -Dm644 ${_truepkgname}-${pkgver}.jar "${pkgdir}/usr/share/java/${pkgname}/${pkgname}.jar"
  install -Dm644 ${pkgname}.xml "${pkgdir}/usr/share/mime/packages/${pkgname}.xml"
  install -Dm644 ${pkgname}.desktop "${pkgdir}/usr/share/applications/${pkgname}.desktop"
  for SIZE in 16 20 24 48 64 128; do
    install -Dm644 resources/${pkgname}/img/${pkgname}-icon-${SIZE}.png \
      "${pkgdir}/usr/share/icons/hicolor/${SIZE}x${SIZE}/apps/${pkgname}.png"
  done
  install -Dm755 ${pkgname}.sh "${pkgdir}/usr/bin/${pkgname}"
}
