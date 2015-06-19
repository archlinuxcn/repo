# Maintainer: Colin Keenan <colinnkeenan at gmail dot com>

pkgname=tchrome
pkgver=1.3
pkgrel=1
pkgdesc="Close Chrome browser including background, or launch a version of Google Chrome/Chromium"
arch=('any')
url="https://github.com/colinkeenan/tchrome"
license=('GPL')
install=${pkgname}.install

source=(https://raw.githubusercontent.com/colinkeenan/${pkgname}/v${pkgver}/${pkgname} 
        https://raw.githubusercontent.com/colinkeenan/${pkgname}/v${pkgver}/${pkgname}.conf 
	https://raw.githubusercontent.com/colinkeenan/${pkgname}/v${pkgver}/${pkgname}.desktop
	https://raw.githubusercontent.com/colinkeenan/${pkgname}/v${pkgver}/${pkgname}.svg)
md5sums=('45abeb3edac87aaa0980b48f01172937'
         '3bab05dbc5357bbe934942503a79c6a3'
         'bcd4d82fa14628eb47ffc6e8cb66c0cf'
         '5f1dfb475e6f52d7169795fa146de4e0')

package() {
  install -D -m644 ${pkgname}.conf "$pkgdir/etc/${pkgname}.conf"
  install -D -m644 ${pkgname}.desktop "$pkgdir/usr/share/applications/${pkgname}.desktop"
  install -D -m644 ${pkgname}.svg "$pkgdir/usr/share/icons/hicolor/scalable/apps/${pkgname}.svg"
  install -D -m755 ${pkgname} "$pkgdir/usr/bin/${pkgname}"
}
