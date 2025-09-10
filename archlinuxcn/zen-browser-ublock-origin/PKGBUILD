# Maintainer: Kimiblock Moe

pkgname=zen-browser-ublock-origin
pkgver=1.66.2
pkgrel=1
epoch=1
pkgdesc='Efficient blocker add-on for various browsers. Fast, potent, and lean. Symlink to the Firefox addon.'
arch=(any)
url=https://github.com/gorhill/uBlock
license=(GPL-3.0-or-later)
depends=(firefox-ublock-origin)
source=(https://github.com/gorhill/uBlock.git)
b2sums=('9de01e1495088c3051896479809e8499100d719a1fe7c7b7e62be0189b26297ff7fe2f47bcdd7bff954f020aa9c29484d5c9d11945a7ae7927aaf8fa936e05c6')

function package() {
	install -d \
		"${pkgdir}/usr/lib/zen-browser/browser/extensions"
	ln -sf \
		"/usr/lib/firefox/browser/extensions/uBlock0@raymondhill.net.xpi" \
		"${pkgdir}/usr/lib/zen-browser/browser/extensions/uBlock0@raymondhill.net.xpi"
}
