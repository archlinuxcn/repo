# Maintainer: Butui Hu <hot123tea123@gmail.com>

pkgname=raw2ometiff
pkgver=0.7.1
pkgrel=1
pkgdesc='Raw format to OME-TIFF converter'
arch=('any')
url='https://github.com/glencoesoftware/raw2ometiff'
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
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/glencoesoftware/raw2ometiff/archive/refs/tags/v${pkgver}.tar.gz")
sha512sums=('52660edb6dca14b0931c92dbf4382e9c1debc88bd6d4c226b533008b9181ac68a76e64dc12f4b85fb198af4c42b323ffd1f9e47df61e429b420d94facefaa0d6')

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
