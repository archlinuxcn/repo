# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=QuPath
pkgname=qupath
pkgver=0.4.0
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
sha512sums=('09ffa998a56898e7d483b582e7c9e0a047da63bd72bdc746395be9e513b676645096b0d4497c255a9236de7c7ac1ddc40705e52bd4cea56e95857f89e6a986fd')

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

