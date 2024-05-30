# Maintainer: Butui Hu <hot123tea123@gmail.com>

pkgname=bioformats2raw
pkgver=0.9.3
pkgrel=1
pkgdesc='Bio-Formats image file format to raw format converter'
arch=('any')
url='https://github.com/glencoesoftware/bioformats2raw'
license=('GPL-2.0-or-later')
depends=(
  bash
  blosc
  java-runtime=17
)
makedepends=(
  git
  gradle
  java-environment=17
)
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/glencoesoftware/bioformats2raw/archive/refs/tags/v${pkgver}.tar.gz")
sha512sums=('0e6d8319dfae1905cb11a373a741c87e6ed4c132b3f435a251bcbad00b04ae1f9a2d7ca71352d6b757b1c23c6d24f38d82b5484f3c3e7314700ada692c488b30')

package() {
  cd "${pkgname}-${pkgver}"
  gradle --gradle-user-home=/tmp clean installDist -Porg.gradle.java.home=/usr/lib/jvm/default
  install -dm755 ${pkgdir}/opt ${pkgdir}/usr/bin
  cp -a "build/install/${pkgname}-${pkgver}" "${pkgdir}/opt/${pkgname}"
  ln -sf "/opt/${pkgname}/bin/${pkgname}-${pkgver}" "${pkgdir}/opt/${pkgname}/bin/${pkgname}"
  ln -sf "/opt/${pkgname}/bin/${pkgname}" "${pkgdir}/usr/bin/${pkgname}"
  rm -vf "${pkgdir}/opt/${pkgname}/bin/${pkgname}-${pkgver}.bat"
}
# vim:set ts=2 sw=2 et:
