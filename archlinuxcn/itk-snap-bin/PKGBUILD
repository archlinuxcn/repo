# Maintainer: Butui Hu <hot123tea123@gmail.com>

pkgname=itk-snap-bin
_pkgname=itk-snap
pkgver=3.8.0
_pkgver=3.8.0
pkgrel=1
pkgdesc="A software application used to segment structures in 3D medical images"
arch=('x86_64')
url="https://www.itksnap.org"
license=('GPL')
depends=('curl' 'glib2' 'libpng12')
makedepends=('gendesk')
provides=('itk-snap')
conflicts=('itk-snap')
source=(
    "${pkgname}-${pkgver}.tar.gz::https://sourceforge.net/projects/itk-snap/files/itk-snap/3.8.0/itksnap-3.8.0-20190612-Linux-x86_64.tar.gz"
    "${_pkgname}.png::https://sourceforge.net/p/itk-snap/src/ci/master/tree/GUI/Qt/Resources/logo_square.png?format=raw"
)
sha512sums=('c76247387f6e4c5fe0dfaee7147167429352994a6903e772e6e2cf6a3a91bce92d9d34b6a0905a929bfa206854650438503d2da58abeb4966503d42ce42ea79b'
            '7d7866a4f28ee645cf4a454488d197a776475d2959d0f9d4d34cf534f34a73ffbb1b92430518f36948b4c25b736990693be07dd345600ed8292e526e2846fca1')

prepare() {
  msg2 "Creating desktop file"
  gendesk -f -n --pkgname ${_pkgname} \
    --pkgdesc "${pkgdesc}" \
    --categories "Education;Graphics;Science;DataVisualization;MedicalSoftware;Viewer" \
    --icon "${_pkgname}" \
    --exec "itksnap"
}
package() {
  install -d "${pkgdir}/usr"
  mv "${srcdir}/itksnap-${_pkgver}-20190612-Linux-gcc64/"* "${pkgdir}/usr"
  install -Dm644 "${srcdir}/${_pkgname}.desktop" "${pkgdir}/usr/share/applications/${_pkgname}.desktop"
  install -Dm644 "${srcdir}/${_pkgname}.png" "${pkgdir}/usr/share/pixmaps/${_pkgname}.png"
}
# vim:set ts=2 sw=2 et:

