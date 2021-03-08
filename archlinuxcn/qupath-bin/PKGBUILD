# Maintainer: Butui Hu <hot123tea123@gmail.com>

pkgname=qupath-bin
_pkgname=QuPath
pkgver=0.2.3
pkgrel=2
pkgdesc="An open, powerful, flexible, extensible software platform for whole slide image analysis."
arch=('x86_64')
url="https://qupath.github.io"
license=('GPL3')
makedepends=('gendesk')
provides=(qupath=${pkgver})
conflicts=('qupath')
options=(!strip)
source=(
    "${pkgname}-${pkgver}.tar.xz::https://github.com/qupath/qupath/releases/download/v${pkgver//_/-}/${_pkgname}-${pkgver//_/-}-Linux.tar.xz"
)
sha512sums=('283b954a76e921e4c12d162af6d7687c512056700ce66b12dd692555a6af0595b0fc619fead173ff18df441f359c3c2a0260b6e2883f40e4851f3e0919aa5a73')

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
  find "${pkgdir}/opt/${_pkgname}" -type f -name "*.png" -exec cp -vf {} "${pkgdir}/usr/share/pixmaps/${_pkgname}.png" \;
  ln -s /opt/${_pkgname}/bin/${_pkgname}-${pkgver//_/-} "${pkgdir}/usr/bin/qupath"
  install -Dm644 "${srcdir}/${_pkgname}.desktop" "${pkgdir}/usr/share/applications/${_pkgname}.desktop"
}
# vim:set ts=2 sw=2 et:

