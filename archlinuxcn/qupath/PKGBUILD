# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=QuPath
pkgname=qupath
pkgver=0.4.1
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
sha512sums=('3887f55f95e6d010a8969d82fe0deda0a25943553769549bf2d1e4bfd4de89236137d2da278c05b669dcee3114973c606350d5b5e756b343c433ffb95ab8f363')

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

