# Maintainer: Doug Newgard <scimmia at archlinux dot info>

pkgname=pepper-flash
pkgdesc="Adobe's Pepper Flash plugin"
pkgver=26.0.0.131
pkgrel=1
arch=('i686' 'x86_64')
url='http://www.adobe.com/software/flash/about/'
license=('custom')
depends=('gcc-libs' 'glibc')
optdepends=('flashplugin: Settings utility')
conflicts=('chromium-pepper-flash')
source_i686=("flash_player_ppapi_linux_$pkgver.i386.tar.gz::https://fpdownload.adobe.com/get/flashplayer/pdc/$pkgver/flash_player_ppapi_linux.i386.tar.gz")
source_x86_64=("flash_player_ppapi_linux_$pkgver.x86_64.tar.gz::https://fpdownload.adobe.com/get/flashplayer/pdc/$pkgver/flash_player_ppapi_linux.x86_64.tar.gz")
sha256sums_i686=('25497127c725442ab327c6f5bd63b8c44696c9e1427ce7f249f89de86416142f')
sha256sums_x86_64=('de696e2bc2cc3025d0158b8d3d74908eb5740ba4cd33d3f2841f0146933b076c')

package() {
  install -Dm644 manifest.json libpepflashplayer.so -t "$pkgdir/usr/lib/PepperFlash/"
  install -Dm644 license.pdf -t "$pkgdir/usr/share/licenses/$pkgname/"
}
