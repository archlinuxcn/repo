# Maintainer: Colin Keenan <colinnkeenan at gmail dot com>

pkgname=clup
pkgver=1.1
pkgrel=3
pkgdesc="Clickable/configurable Update of Arch Linux"
arch=('any')
url="https://github.com/colinkeenan/clup"
license=('GPL')
install=${pkgname}.install

source=(https://raw.githubusercontent.com/colinkeenan/${pkgname}/v${pkgver}/${pkgname} 
        https://raw.githubusercontent.com/colinkeenan/${pkgname}/v${pkgver}/${pkgname}.conf 
	https://raw.githubusercontent.com/colinkeenan/${pkgname}/v${pkgver}/${pkgname}.desktop)
md5sums=('7450016149f28def649bf4fa22adef6c'
         'd5f3caab2d3068ecaf76e09a5ece98f2'
         '0abe59259a20e473417204c8f31543f9')

package() {
  install -D -m644 ${pkgname}.conf "$pkgdir/etc/${pkgname}.conf"
  install -D -m644 ${pkgname}.desktop "$pkgdir/usr/share/applications/${pkgname}.desktop"
  install -D -m755 ${pkgname} "$pkgdir/usr/bin/${pkgname}"
}
