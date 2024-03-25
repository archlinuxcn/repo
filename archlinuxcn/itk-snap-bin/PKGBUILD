# Maintainer: Butui Hu <hot123tea123@gmail.com>

pkgname=itk-snap-bin
_pkgname=itk-snap
pkgver=4.0.2
_date=20230925
pkgrel=2
pkgdesc="A software application used to segment structures in 3D medical images"
arch=('x86_64')
url="https://www.itksnap.org"
license=('GPL-3.0-or-later')
depends=(
  gcc-libs
  glib2
  glibc
)
makedepends=(
  gendesk
)
provides=('itk-snap')
conflicts=('itk-snap')
source=(
    "${pkgname}-${pkgver}.tar.gz::https://sourceforge.net/projects/itk-snap/files/itk-snap/${pkgver}/itksnap-${pkgver}-Linux-gcc64.tar.gz"
    "${_pkgname}.png::https://github.com/pyushkevich/itksnap/raw/master/GUI/Qt/Resources/logo_square.png"
)
sha512sums=('241051e9a8f5142f8c0b9608d6c0184f61f22e9f39d799870febd6793b44bb76fccc222b6292287736b68437fa7a92d260a33662320e2a14a3acc76d67e30e46'
            '7d7866a4f28ee645cf4a454488d197a776475d2959d0f9d4d34cf534f34a73ffbb1b92430518f36948b4c25b736990693be07dd345600ed8292e526e2846fca1')

prepare() {
  echo "Creating desktop file"
  gendesk -f -n --pkgname ${_pkgname} \
    --pkgdesc "${pkgdesc}" \
    --categories "Education;Graphics;Science;DataVisualization;MedicalSoftware;Viewer" \
    --icon "${_pkgname}" \
    --exec "itksnap"
}
package() {
  install -d "${pkgdir}/usr"
  mv "${srcdir}/itksnap-${pkgver}-${_date}-Linux-gcc64/"* "${pkgdir}/usr"
  install -Dm644 "${srcdir}/${_pkgname}.desktop" "${pkgdir}/usr/share/applications/${_pkgname}.desktop"
  install -Dm644 "${srcdir}/${_pkgname}.png" "${pkgdir}/usr/share/pixmaps/${_pkgname}.png"
}
# vim:set ts=2 sw=2 et:

