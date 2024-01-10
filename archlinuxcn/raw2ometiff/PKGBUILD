# Maintainer: Butui Hu <hot123tea123@gmail.com>

pkgname=raw2ometiff
pkgver=0.6.0
pkgrel=1
pkgdesc='Raw format to OME-TIFF converter'
arch=('any')
url='https://github.com/glencoesoftware/raw2ometiff'
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
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/glencoesoftware/raw2ometiff/archive/refs/tags/v${pkgver}.tar.gz")
sha512sums=('c90332bbdf6c79bbeebe3dc6cfa3b0a08613cc399f56d2a5f7f631922aa2421c77ddd51e34e12a2d841a663951dbccbdea0e1f00cf95feca3198b02533b64311')

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
