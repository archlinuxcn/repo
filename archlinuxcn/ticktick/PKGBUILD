# Maintainer: Agustin Cisneros <agustincc@tutanota.com>

pkgname=ticktick
pkgver=2.0.0
pkgrel=1
pkgdesc='Official desktop application for Linux'
arch=('x86_64' 'aarch64')
url='https://ticktick.com/about/download'
license=('custom')
conflicts=('ticktick-nativefier')
depends=('alsa-lib' 'gtk3' 'nss')
source=('ticktick.sh' 'LICENSE')
source_x86_64=("${pkgname}-${pkgver}-amd64.deb::https://d2atcrkye2ik4e.cloudfront.net/download/linux/linux_deb_x64/${pkgname}-${pkgver}-amd64.deb")
source_aarch64=("${pkgname}-${pkgver}-arm64.deb::https://d2atcrkye2ik4e.cloudfront.net/download/linux/linux_deb_arm64/${pkgname}-${pkgver}-arm64.deb")
sha256sums=('b060ec7e9919707fe70c0c65f1c307d65c1f4ad84b5640e7dbeb2dd06e246637'
            '2d866fcb749c30d931fa96cc1578869b3fa9fc61a5c5f30e0316ddb00abb5814')
sha256sums_x86_64=('2ce96561db5ef98fa96e35c8db3390af0a6d994a380a4e8ec98a045fab2e634f')
sha256sums_aarch64=('a01587c471dfc06d88e5192eafa8584ea826a1b833ad91d65d1d7028ee2c5d65')

package() {
  tar -xf data.tar.xz -C "${pkgdir}"

  # Replace default path to system symlink
  sed -i 's/^Exec=.*/Exec=ticktick --uri=%U/' "${pkgdir}/usr/share/applications/ticktick.desktop"

  # Copy launch script to allow custom flags
  install -Dm 755 ticktick.sh "${pkgdir}/usr/bin/ticktick"

  # Install license from https://ticktick.com/about/tos
  install -Dm644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"

  mv "${pkgdir}/opt/TickTick/LICENSE.electron.txt" \
     "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE.electron.txt"
  mv "${pkgdir}/opt/TickTick/LICENSES.chromium.html" \
     "${pkgdir}/usr/share/licenses/${pkgname}/LICENSES.chromium.html"
}
