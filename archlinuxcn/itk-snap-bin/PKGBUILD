# Maintainer: Butui Hu <hot123tea123@gmail.com>

pkgname=itk-snap-bin
_pkgname=itk-snap
_date=20241202
pkgver=4.2.2
pkgrel=3
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
    "${_pkgname}-${pkgver}.tar.gz::https://sourceforge.net/projects/itk-snap/files/itk-snap/${pkgver}/itksnap-${pkgver}-${_date}-Linux-x86_64.tar.gz"
    "${_pkgname}.png::https://github.com/pyushkevich/itksnap/raw/master/GUI/Qt/Resources/logo_square.png"
)
noextract=("${_pkgname}-${pkgver}.tar.gz")
sha512sums=('e9cace7d9235960a4a400ea86a3014c18a6ba2b23f24a58a5ded9e237d4f4669b07686f2f048f61398047d09a7144adc62a1dea9304415fccf4245b16ffa6877'
            '7d7866a4f28ee645cf4a454488d197a776475d2959d0f9d4d34cf534f34a73ffbb1b92430518f36948b4c25b736990693be07dd345600ed8292e526e2846fca1')

prepare() {
  echo "Creating desktop file"
  gendesk -f -n --pkgname ${_pkgname} \
    --pkgdesc "${pkgdesc}" \
    --categories "Education;Graphics;Science;DataVisualization;MedicalSoftware;Viewer" \
    --icon "${_pkgname}" \
    --exec "itksnap"
  # manually extract tarball due to their unpredicted name
  mkdir "${srcdir}/${_pkgname}"
  tar xvf "${srcdir}/${_pkgname}-${pkgver}.tar.gz" -C "${srcdir}/${_pkgname}" --strip-components 1
}
package() {
  # install -d "${pkgdir}/usr"
  cp -a "${srcdir}/${_pkgname}" "${pkgdir}/usr"
  install -Dm644 "${srcdir}/${_pkgname}.desktop" "${pkgdir}/usr/share/applications/${_pkgname}.desktop"
  install -Dm644 "${srcdir}/${_pkgname}.png" "${pkgdir}/usr/share/pixmaps/${_pkgname}.png"
}
# vim:set ts=2 sw=2 et:
