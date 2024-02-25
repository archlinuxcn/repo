# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=QuPath
pkgname=qupath
pkgver=0.5.0
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
  'gradle'
  'java-environment=17'
)
optdepends=(
  'ttf-droid: font for CJK characters'
)
options=(!strip)
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/qupath/qupath/archive/v${pkgver}.tar.gz")
sha512sums=('825c4fee2ef2b067958f6330457831173891ef06aded24676c5d527d0a890e72c03b4b8fbe2de83c4b927a6c07b548767b86fdca1c9cdfc1da8326a701dd821e')

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
  # you could also build it with gradle wrapper
  # ./gradlew clean jpackage
  gradle clean jpackage -Porg.gradle.java.home=/usr/lib/jvm/default
}

package() {
  install -d ${pkgdir}/opt
  cp -a ${srcdir}/${pkgname}-${pkgver}/build/dist/${_pkgname} ${pkgdir}/opt/${_pkgname}
  install -d "${pkgdir}/usr/bin"
  ln -sf "/opt/${_pkgname}/bin/${_pkgname}" "${pkgdir}/usr/bin/${pkgname}"
  install -Dm644 "${srcdir}/${pkgname}.desktop" "${pkgdir}/usr/share/applications/${_pkgname}.desktop"
}
# vim:set ts=2 sw=2 et:
