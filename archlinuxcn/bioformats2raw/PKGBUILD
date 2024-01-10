# Maintainer: Butui Hu <hot123tea123@gmail.com>

pkgname=bioformats2raw
pkgver=0.8.0
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
sha512sums=('da619ca6035934afcc9dd3c6bc7216c408d60c3eb67975680fd1b0a8cd8dc7a4d9b7767214e29ba6c9017436a90ac353e96b3e870c02be88ab60a4c1246aa870')

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
