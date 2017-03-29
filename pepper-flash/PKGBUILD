# Maintainer: Doug Newgard <scimmia at archlinux dot info>

pkgname=pepper-flash
pkgdesc="Adobe's Pepper Flash plugin"
pkgver=25.0.0.127
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
sha256sums_i686=('dfa0731c4c8f878b0777665ad1d5d45ae306b8ec3afc8a0d84c1321c4ab7e75b')
sha256sums_x86_64=('0d31c78f5e96488e548ce742d3acddf1fe05580a2a2bbc41032196a9f2c4c792')

package() {
  install -Dm644 manifest.json libpepflashplayer.so -t "$pkgdir/usr/lib/PepperFlash/"
  install -Dm644 license.pdf -t "$pkgdir/usr/share/licenses/$pkgname/"
}
