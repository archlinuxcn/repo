# Maintainer: Butui Hu <hot123tea123@gmail.com>

pkgname=itk-snap-bin
_pkgname=itk-snap
pkgver=3.8.0beta
_pkgver=3.8.0
pkgrel=1
pkgdesc="A software application used to segment structures in 3D medical images"
arch=('x86_64')
url="https://www.itksnap.org"
license=('GPL')
depends=('curl' 'glib2')
makedepends=('gendesk')
provides=('itk-snap')
conflicts=('itk-snap')
source=(
    "${pkgname}-${pkgver}.tar.gz::http://www.nitrc.org/frs/downloadlink.php/10980"
    "${_pkgname}.png::https://sourceforge.net/p/itk-snap/src/ci/master/tree/GUI/Qt/Resources/logo_square.png?format=raw"
)
sha512sums=(
    "2b9b5e5965961c837904dc1f409d87f1490b3daeada757aeab7eeaeb4109b88a37f73ec9c1a4f21adfec5724940b059f50663f39fae31adf713cf8f41f985007"
    "7d7866a4f28ee645cf4a454488d197a776475d2959d0f9d4d34cf534f34a73ffbb1b92430518f36948b4c25b736990693be07dd345600ed8292e526e2846fca1"
)

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
  mv "${srcdir}/itksnap-${_pkgver}-beta-20181028-Linux-gcc64/"* "${pkgdir}/usr"
  install -Dm644 "${srcdir}/${_pkgname}.desktop" "${pkgdir}/usr/share/applications/${_pkgname}.desktop"
  install -Dm644 "${srcdir}/${_pkgname}.png" "${pkgdir}/usr/share/pixmaps/${_pkgname}.png"
}
# vim:set ts=2 sw=2 et:

