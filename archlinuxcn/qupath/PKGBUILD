# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=QuPath
pkgname=qupath
pkgver=0.2.3
pkgrel=2
pkgdesc='Bioimage analysis & digital pathology'
arch=('x86_64')
url="https://qupath.github.io"
license=('GPL')
makedepends=(
  'gendesk'
  'java-environment'
)
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/qupath/qupath/archive/v${pkgver}.tar.gz")
sha512sums=('176a21fca1ae62d632fa15b75f980bdd2c2375f9e0870760a1304638134649615e44438bc62ac462494782dfa5e27ada945bc6b8eabc0c0c87df79b2ea147bb7')

prepare() {
  echo "Creating desktop file"
  gendesk -f -n --pkgname ${pkgname} \
    --pkgdesc "${pkgdesc}" \
    --categories "Graphics;MedicalSoftware;Science;" \
    --icon "/opt/${pkgname}/lib/${_pkgname}-${pkgver}.png" \
    --exec "${pkgname}"
}

build() {
  cd "${pkgname}-${pkgver}"
  ./gradlew clean assemble createPackage
}

package() {
  install -d ${pkgdir}/opt
  cp -a ${srcdir}/${pkgname}-${pkgver}/build/dist/${_pkgname}-${pkgver} ${pkgdir}/opt/${pkgname}
  install -d "${pkgdir}/usr/bin"
  ln -sf "/opt/${pkgname}/bin/${_pkgname}-${pkgver}" "${pkgdir}/usr/bin/${pkgname}" 
  find "${pkgdir}/opt/${pkgname}/lib/app" -type f -name "*.cfg" -exec mv -v {} "${pkgdir}/opt/${pkgname}/lib/app/${_pkgname}-${pkgver}.cfg" \;
  install -Dm644 "${srcdir}/${pkgname}.desktop" "${pkgdir}/usr/share/applications/${_pkgname}.desktop"
}
# vim:set ts=2 sw=2 et:

