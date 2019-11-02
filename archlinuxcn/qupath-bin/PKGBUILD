# Maintainer: Butui Hu <hot123tea123@gmail.com>

pkgname=qupath-bin
_pkgname=QuPath
pkgver=0.2.0_m4
pkgrel=1
pkgdesc="An open, powerful, flexible, extensible software platform for whole slide image analysis."
arch=('x86_64')
url="https://qupath.github.io"
license=('GPL')
depends=(
  'freetype2'
  'glib2'
  'java-runtime'  
  'libjpeg-turbo'
  'libnet'
  'libtiff'
  'libxml2'
  'sqlite'
)
makedepends=('gendesk')
provides=(qupath=${pkgver})
conflicts=('qupath')
source=(
    "${pkgname}-${pkgver}.tar.xz::https://github.com/qupath/qupath/releases/download/v${pkgver//_/-}/${_pkgname}-${pkgver//_/-}-Linux.tar.xz"
)
sha512sums=('629d7bb2ef1d4ddf00e95905b2ffa42399eecf7f891f8c85053fd84972f77720f6fafe891120c021b3f6ddd52ae8b56d5568dca21ab958edf019c03a3c7fb130')

prepare() {
  msg2 "Creating desktop file"
  gendesk -f -n --pkgname ${_pkgname} \
    --pkgdesc "${pkgdesc}" \
    --categories "Graphics;MedicalSoftware;Science;" \
    --icon "${_pkgname}" \
    --exec "qupath"
}
package() {
  install -d "${pkgdir}/opt" "${pkgdir}/usr/bin" "${pkgdir}/usr/share/pixmaps"
  mv "${srcdir}/${_pkgname}-${pkgver//_/-}" "${pkgdir}/opt/${_pkgname}"
  mv "${pkgdir}/opt/${_pkgname}/bin/${_pkgname}-${pkgver//_/-}.png" "${pkgdir}/usr/share/pixmaps/${_pkgname}.png"
  ln -s /opt/${_pkgname}/bin/${_pkgname}-${pkgver//_/-} "${pkgdir}/usr/bin/qupath"
  install -Dm644 "${srcdir}/${_pkgname}.desktop" "${pkgdir}/usr/share/applications/${_pkgname}.desktop"
}
# vim:set ts=2 sw=2 et:

