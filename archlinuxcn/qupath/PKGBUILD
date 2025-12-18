# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=QuPath
pkgname=qupath
pkgver=0.6.0
pkgrel=2
pkgdesc='Bioimage analysis & digital pathology'
arch=('x86_64')
url='https://github.com/qupath/qupath'
license=('GPL-2.0-or-later')
depends=(
  freetype2
  gcc-libs
  glibc
  giflib
  harfbuzz
  lcms2
  libjpeg-turbo
  libpng
  zlib
)
makedepends=(
  'gendesk'
  'java-environment=17'
)
optdepends=(
  'ttf-droid: font for CJK characters'
)
options=(!strip)
source=(
  "${pkgname}-${pkgver}.tar.gz::https://github.com/qupath/qupath/archive/v${pkgver}.tar.gz"
  "0001-fix-maven-repo.patch"
)
sha512sums=('2a0ddd87ce307a3c554592c0fdd56fc31f418a30187eaed654e9128adbecf0aedc1a568a208a00f8963b0f68adc2cb2aeb3861f3356abd07b002e0a9183f24de'
            '178d2960668c246bc8d3c1cc7c13dad5f7b423e5928f19e45452511016cd89333fac44646554ce40aa12e7a50029164f4707f553e6e05770db2e440bb239828d')

prepare() {
  echo "Creating desktop file"
  gendesk -f -n --pkgname ${pkgname} \
    --pkgdesc "${pkgdesc}" \
    --categories "Graphics;MedicalSoftware;Science;" \
    --icon "/opt/${_pkgname}/lib/${_pkgname}.png" \
    --exec "${pkgname}"
  patch -p1 -d "${srcdir}/${pkgname}-${pkgver}" -i "${srcdir}/0001-fix-maven-repo.patch"
}

build() {
  cd "${pkgname}-${pkgver}"
  # build with gradle wrapper
  ./gradlew clean jpackage -Porg.gradle.java.home=/usr/lib/jvm/default
  # do not work with gradle 9
  # gradle clean jpackage -Porg.gradle.java.home=/usr/lib/jvm/default
}

package() {
  install -d ${pkgdir}/opt
  cp -a ${srcdir}/${pkgname}-${pkgver}/build/dist/${_pkgname} ${pkgdir}/opt/${_pkgname}
  install -d "${pkgdir}/usr/bin"
  ln -sf "/opt/${_pkgname}/bin/${_pkgname}" "${pkgdir}/usr/bin/${pkgname}"
  install -Dm644 "${srcdir}/${pkgname}.desktop" "${pkgdir}/usr/share/applications/${_pkgname}.desktop"
}
# vim:set ts=2 sw=2 et:
