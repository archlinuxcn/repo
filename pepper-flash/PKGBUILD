# Maintainer: Doug Newgard <scimmia at archlinux dot info>

pkgname=pepper-flash
pkgdesc="Adobe's Pepper Flash plugin"
pkgver=23.0.0.162
pkgrel=1
arch=('i686' 'x86_64')
url='http://www.adobe.com/software/flash/about/'
license=('custom')
depends=('gcc-libs')
optdepends=('freshplayerplugin: Firefox support'
            'flashplugin: Settings utility')
conflicts=('chromium-pepper-flash')
provides=('chromium-pepper-flash')
source=("http://wwwimages.adobe.com/content/dam/acom/en/legal/licenses-terms/pdf/Flash_Player_${pkgver%%.*}_0.pdf")
source_x86_64=("flash_player_ppapi_linux_$pkgver.x86_64.tar.gz::https://fpdownload.adobe.com/pub/flashplayer/pdc/$pkgver/flash_player_ppapi_linux.x86_64.tar.gz")
source_i686=("flash_player_ppapi_linux_$pkgver.i386.tar.gz::https://fpdownload.adobe.com/pub/flashplayer/pdc/$pkgver/flash_player_ppapi_linux.i386.tar.gz")
sha256sums=('74d3a2dd91dbf31efd962f0cf83c09eed70fbf70726766f18089b2bf9c55e7bd')
sha256sums_i686=('d0d2788daff437e7f8d018bc3e10a190776d9bcbef556f6d343c12beee58ce34')
sha256sums_x86_64=('7467e5401d6cc6bb6f3c9034841aa834ff357d7500fbf2e0adf22d4979668bec')

package() {
  install -Dm644 manifest.json libpepflashplayer.so -t "$pkgdir/usr/lib/PepperFlash/"
  install -Dm644 Flash_Player_${pkgver%%.*}_0.pdf -t "$pkgdir/usr/share/licenses/$pkgname/"
}
