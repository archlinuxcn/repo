# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=QuPath
pkgname=qupath
pkgver=0.4.2
pkgrel=1
pkgdesc='Bioimage analysis & digital pathology'
arch=('x86_64')
url="https://qupath.github.io"
license=('GPL')
makedepends=(
  'gendesk'
  'java-environment=11'
)
optdepends=(
  'ttf-droid: font for CJK characters'
)
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/qupath/qupath/archive/v${pkgver}.tar.gz")
sha512sums=('7b3f5c0fc4ae72005c66a0e9b9c4e9cc0bd99dfaab30f2dd7d0ded76a5de3b1041d3046468e541f9008f2bc4637f91a2b9af68bfe246b8cd8851c6a6120e5d19')

prepare() {
  echo "Creating desktop file"
  gendesk -f -n --pkgname ${pkgname} \
    --pkgdesc "${pkgdesc}" \
    --categories "Graphics;MedicalSoftware;Science;" \
    --icon "/opt/${pkgname}/lib/${_pkgname}.png" \
    --exec "${pkgname}"
}

build() {
  cd "${pkgname}-${pkgver}"
  ./gradlew clean jpackage
}

package() {
  install -d ${pkgdir}/opt
  cp -a ${srcdir}/${pkgname}-${pkgver}/build/dist/${_pkgname} ${pkgdir}/opt/${pkgname}
  install -d "${pkgdir}/usr/bin"
  ln -sf "/opt/${pkgname}/bin/${_pkgname}" "${pkgdir}/usr/bin/${pkgname}" 
  install -Dm644 "${srcdir}/${pkgname}.desktop" "${pkgdir}/usr/share/applications/${_pkgname}.desktop"
}
# vim:set ts=2 sw=2 et:

