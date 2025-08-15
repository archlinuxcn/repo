# Maintainer: Butui Hu <hot123tea123@gmail.com>

pkgname=bioformats2raw
pkgver=0.10.1
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
sha512sums=('27f102471ebc07982e2783af0a0ecc87043b8b2309edd6ddab465c1d1a90e0d74464b453732db4b4aa603c362376f9814903229f5fe0ae75a972ebfd0f14ed90')

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
