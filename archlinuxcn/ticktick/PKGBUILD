# Maintainer: Agustin Cisneros <agustincc@tutanota.com>

pkgname=ticktick
pkgver=1.0.80
pkgrel=2
pkgdesc='Official desktop application for Linux'
arch=('x86_64' 'aarch64')
url='https://ticktick.com/about/download'
license=('custom')
conflicts=('ticktick-nativefier')
depends=('alsa-lib' 'gtk3' 'nss')
source=('LICENSE')
source_x86_64=("${pkgname}-${pkgver}-amd64.deb::https://ticktick-download-linux.s3.amazonaws.com/download/linux/linux_deb_x64/${pkgname}-${pkgver}-amd64.deb")
source_aarch64=("${pkgname}-${pkgver}-arm64.deb::https://ticktick-download-linux.s3.amazonaws.com/download/linux/linux_deb_arm64/${pkgname}-${pkgver}-arm64.deb")
sha256sums=('2d866fcb749c30d931fa96cc1578869b3fa9fc61a5c5f30e0316ddb00abb5814')
sha256sums_x86_64=('10afbc3451229b681c163f6de80198746565c858fd62aecd68e89add72b2ddc7')
sha256sums_aarch64=('f1b30675fb745a33b56c70eb30941979513c46222bc084a8329cad2a1f9b760b')

package() {
  tar -xf data.tar.xz -C "${pkgdir}"

  # Install license from https://ticktick.com/about/tos
  install -Dm644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"

  mv "${pkgdir}/opt/TickTick/LICENSE.electron.txt" \
     "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE.electron.txt"
  mv "${pkgdir}/opt/TickTick/LICENSES.chromium.html" \
     "${pkgdir}/usr/share/licenses/${pkgname}/LICENSES.chromium.html"
}
