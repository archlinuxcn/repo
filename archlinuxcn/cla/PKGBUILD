# Maintainer: Colin Keenan <colinnkeenan at gmail dot com>

pkgname=cla
pkgver=1.0
pkgrel=3
pkgdesc="Close active window. If desktop is active, logout. For panel-launcher."
arch=('any')
url="https://github.com/colinkeenan/cla"
license=('GPL')
depends=('xdotool' 'wmctrl')
install=${pkgname}.install

source=("https://raw.githubusercontent.com/colinkeenan/${pkgname}/v${pkgver}/${pkgname}" 
        "https://raw.githubusercontent.com/colinkeenan/${pkgname}/v${pkgver}/${pkgname}.desktop")
md5sums=('4aff89eb4505840fd11c83404cf33717'
         'c0c289e6dac69a28a82add518b0252ac')

package() {
  install -D -m644 cla.desktop "$pkgdir/usr/share/applications/cla.desktop"
  install -D -m755 cla "$pkgdir/usr/bin/cla"
}
