# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=QuPath
pkgname=qupath
pkgver=0.7.0
pkgrel=1
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
sha512sums=('b12636444c64c44786f32d913471b993ec2a566fff678e46b4bd555025110ca6c0625c90321265fd94d2da05fefc895da280bcf523f7a30cc7284eb979a1f578'
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
