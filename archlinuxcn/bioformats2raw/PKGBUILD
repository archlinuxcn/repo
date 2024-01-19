# Maintainer: Butui Hu <hot123tea123@gmail.com>

pkgname=bioformats2raw
pkgver=0.9.0
pkgrel=1
pkgdesc='Bio-Formats image file format to raw format converter'
arch=('any')
url='https://github.com/glencoesoftware/bioformats2raw'
license=('GPL')
depends=(
  bash
  blosc
  java-runtime
)
makedepends=(
  git
  gradle
  java-environment
)
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/glencoesoftware/bioformats2raw/archive/refs/tags/v${pkgver}.tar.gz")
sha512sums=('6262530af29a4c765e22038ecaa4a1cf0bdd97bd7c6a6f1580f052f0e1d7d14770a2fc4cccbc0f8c99b52c8b40929b94e59ffefeef94710bdaeab3163da3e37c')

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
