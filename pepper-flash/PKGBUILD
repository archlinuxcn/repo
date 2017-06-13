# Maintainer: Doug Newgard <scimmia at archlinux dot info>

pkgname=pepper-flash
pkgdesc="Adobe's Pepper Flash plugin"
pkgver=26.0.0.126
pkgrel=1
arch=('i686' 'x86_64')
url='http://www.adobe.com/software/flash/about/'
license=('custom')
depends=('gcc-libs' 'glibc')
optdepends=('flashplugin: Settings utility')
conflicts=('chromium-pepper-flash')
source_i686=("flash_player_ppapi_linux_$pkgver.i386.tar.gz::https://fpdownload.adobe.com/get/flashplayer/pdc/$pkgver/flash_player_ppapi_linux.i386.tar.gz")
source_x86_64=("flash_player_ppapi_linux_$pkgver.x86_64.tar.gz::https://fpdownload.adobe.com/get/flashplayer/pdc/$pkgver/flash_player_ppapi_linux.x86_64.tar.gz")
sha256sums_i686=('f2c7b698d2c5702860f10c847ea1319c942112cdbd892bdaf5a23edafb95c054')
sha256sums_x86_64=('fcb1938f8e7ed98e64c6e097b56f6efc6166db07b182f3981e0334aa148251d2')

package() {
  install -Dm644 manifest.json libpepflashplayer.so -t "$pkgdir/usr/lib/PepperFlash/"
  install -Dm644 license.pdf -t "$pkgdir/usr/share/licenses/$pkgname/"
}
