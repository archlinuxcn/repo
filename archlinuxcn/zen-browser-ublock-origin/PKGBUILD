# Maintainer: Kimiblock Moe

pkgname=zen-browser-ublock-origin
pkgver=1.67.0
pkgrel=1
epoch=1
pkgdesc='Efficient blocker add-on for various browsers. Fast, potent, and lean. Symlink to the Firefox addon.'
arch=(any)
url=https://github.com/gorhill/uBlock
license=(GPL-3.0-or-later)
depends=(firefox-ublock-origin)
source=(https://github.com/gorhill/uBlock.git)
b2sums=('5f60d966beb315fb1d5e9ae1a32e1b1437d15d92cdd3a2d9c55339f6112034fcf3407e403377feb4e71fc3b6ec8428ac22e4fe4f5e7c4f1a72d192b9894cb56d')

function package() {
	install -d \
		"${pkgdir}/usr/lib/zen-browser/browser/extensions"
	ln -sf \
		"/usr/lib/firefox/browser/extensions/uBlock0@raymondhill.net.xpi" \
		"${pkgdir}/usr/lib/zen-browser/browser/extensions/uBlock0@raymondhill.net.xpi"
}
