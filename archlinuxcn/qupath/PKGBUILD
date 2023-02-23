# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=QuPath
pkgname=qupath
pkgver=0.4.3
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
sha512sums=('a96dfc7d10eebfe16599ca732233ab5790b745e818dea98b8da5ac3936dd35c1a7910cef2f21669173af892b7151a89a29eb5a3f66af9969ce4836c211944d25')

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

