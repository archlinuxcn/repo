# Maintainer: Kimiblock Moe

pkgname=zen-browser-ublock-origin
pkgver=1.69.0
pkgrel=1
epoch=1
pkgdesc='Efficient blocker add-on for various browsers. Fast, potent, and lean. Symlink to the Firefox addon.'
arch=(any)
url=https://github.com/gorhill/uBlock
license=(GPL-3.0-or-later)
depends=(firefox-ublock-origin)
source=(https://github.com/gorhill/uBlock.git)
b2sums=('23afefcccf7e39f0f7accf9bd5fbe6aa4d036b7aa2a248a1e12b46d41f627721e84e14e2602096aea2cd62f1f71d3b02dc768b1076f2a1f72d8837483e5827c3')

function package() {
	install -d \
		"${pkgdir}/usr/lib/zen-browser/browser/extensions"
	ln -sf \
		"/usr/lib/firefox/browser/extensions/uBlock0@raymondhill.net.xpi" \
		"${pkgdir}/usr/lib/zen-browser/browser/extensions/uBlock0@raymondhill.net.xpi"
}
