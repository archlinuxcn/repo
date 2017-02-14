# Maintainer: Doug Newgard <scimmia at archlinux dot info>

pkgname=pepper-flash
pkgdesc="Adobe's Pepper Flash plugin"
pkgver=24.0.0.221
pkgrel=1
arch=('i686' 'x86_64')
url='http://www.adobe.com/software/flash/about/'
license=('custom')
depends=('gcc-libs' 'glibc')
optdepends=('freshplayerplugin: Firefox support'
            'flashplugin: Settings utility')
conflicts=('chromium-pepper-flash')
source_x86_64=("flash_player_ppapi_linux_$pkgver.x86_64.tar.gz::https://fpdownload.adobe.com/pub/flashplayer/pdc/$pkgver/flash_player_ppapi_linux.x86_64.tar.gz")
source_i686=("flash_player_ppapi_linux_$pkgver.i386.tar.gz::https://fpdownload.adobe.com/pub/flashplayer/pdc/$pkgver/flash_player_ppapi_linux.i386.tar.gz")
sha256sums_i686=('4f79523ee10b28e172b93c7e3083604916299f888ed7565bf192484dd410f58e')
sha256sums_x86_64=('e420f01500273478d95953829d0fdac7225957777f6d682466aadc368c59bfd7')

package() {
  install -Dm644 manifest.json libpepflashplayer.so -t "$pkgdir/usr/lib/PepperFlash/"
  install -Dm644 license.pdf -t "$pkgdir/usr/share/licenses/$pkgname/"
}
