# Maintainer: Doug Newgard <scimmia at archlinux dot info>

pkgname=pepper-flash
pkgdesc="Adobe's Pepper Flash plugin"
pkgver=25.0.0.171
pkgrel=1
arch=('i686' 'x86_64')
url='http://www.adobe.com/software/flash/about/'
license=('custom')
depends=('gcc-libs' 'glibc')
optdepends=('flashplugin: Settings utility')
conflicts=('chromium-pepper-flash')
source_i686=("flash_player_ppapi_linux_$pkgver.i386.tar.gz::https://fpdownload.adobe.com/get/flashplayer/pdc/$pkgver/flash_player_ppapi_linux.i386.tar.gz")
source_x86_64=("flash_player_ppapi_linux_$pkgver.x86_64.tar.gz::https://fpdownload.adobe.com/get/flashplayer/pdc/$pkgver/flash_player_ppapi_linux.x86_64.tar.gz")
sha256sums_i686=('bd044776ed45b74dba78f6ec0608a857cfab21dccc0c9ace06a7e4b5af8ffd21')
sha256sums_x86_64=('b97e765d75eed61d4703f78af92655d93c80ed07260cdfb07aa6890c30a6dc5a')

package() {
  install -Dm644 manifest.json libpepflashplayer.so -t "$pkgdir/usr/lib/PepperFlash/"
  install -Dm644 license.pdf -t "$pkgdir/usr/share/licenses/$pkgname/"
}
