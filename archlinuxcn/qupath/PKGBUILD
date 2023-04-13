# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=QuPath
pkgname=qupath
pkgver=0.4.3
pkgrel=2
pkgdesc='Bioimage analysis & digital pathology'
arch=('x86_64')
url='https://github.com/qupath/qupath'
license=('GPL')
depends=(
  freetype2
  gcc-libs
  giflib
  harfbuzz
  lcms2
  libjpeg-turbo
  libpng
  libtiff
  libxml2
)
makedepends=(
  'gendesk'
  'java-environment=17'
)
optdepends=(
  'ttf-droid: font for CJK characters'
)
options=(!strip)
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/qupath/qupath/archive/v${pkgver}.tar.gz")
sha512sums=('a96dfc7d10eebfe16599ca732233ab5790b745e818dea98b8da5ac3936dd35c1a7910cef2f21669173af892b7151a89a29eb5a3f66af9969ce4836c211944d25')

prepare() {
  echo "Creating desktop file"
  gendesk -f -n --pkgname ${pkgname} \
    --pkgdesc "${pkgdesc}" \
    --categories "Graphics;MedicalSoftware;Science;" \
    --icon "/opt/${_pkgname}/lib/${_pkgname}.png" \
    --exec "${pkgname}"
}

build() {
  cd "${pkgname}-${pkgver}"
  ./gradlew clean jpackage
}

package() {
  install -d ${pkgdir}/opt
  cp -a ${srcdir}/${pkgname}-${pkgver}/build/dist/${_pkgname} ${pkgdir}/opt/${_pkgname}
  install -d "${pkgdir}/usr/bin"
  ln -sf "/opt/${_pkgname}/bin/${_pkgname}" "${pkgdir}/usr/bin/${pkgname}"
  install -Dm644 "${srcdir}/${pkgname}.desktop" "${pkgdir}/usr/share/applications/${_pkgname}.desktop"
  # create libtiff.so.5 softlink to /usr/lib/libtiff.so
  ln -sf "/usr/lib/libtiff.so" "${pkgdir}/opt/QuPath/lib/app/libtiff.so.5"
}
# vim:set ts=2 sw=2 et:
