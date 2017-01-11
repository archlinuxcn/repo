# Maintainer: Doug Newgard <scimmia at archlinux dot info>

pkgname=pepper-flash
pkgdesc="Adobe's Pepper Flash plugin"
pkgver=24.0.0.194
pkgrel=1
arch=('i686' 'x86_64')
url='http://www.adobe.com/software/flash/about/'
license=('custom')
depends=('gcc-libs')
optdepends=('freshplayerplugin: Firefox support'
            'flashplugin: Settings utility')
conflicts=('chromium-pepper-flash')
provides=('chromium-pepper-flash')
source_x86_64=("flash_player_ppapi_linux_$pkgver.x86_64.tar.gz::https://fpdownload.adobe.com/pub/flashplayer/pdc/$pkgver/flash_player_ppapi_linux.x86_64.tar.gz")
source_i686=("flash_player_ppapi_linux_$pkgver.i386.tar.gz::https://fpdownload.adobe.com/pub/flashplayer/pdc/$pkgver/flash_player_ppapi_linux.i386.tar.gz")
sha256sums_i686=('e755bcffaa9967318b75d68fb8f8c83f6e53457e2a068a94eabb7a7ef69c05b8')
sha256sums_x86_64=('6fcd6df319690dc2bc14fc587107f6916e5e36dbf8aaa7aa55a2af6bec666aaa')

package() {
  install -Dm644 manifest.json libpepflashplayer.so -t "$pkgdir/usr/lib/PepperFlash/"
  install -Dm644 license.pdf -t "$pkgdir/usr/share/licenses/$pkgname/"
}
