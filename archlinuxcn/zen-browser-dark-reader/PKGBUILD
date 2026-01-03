# Maintainer: Kimiblock Moe

pkgname=zen-browser-dark-reader
pkgver=4.9.118
pkgrel=1
pkgdesc='Inverts brightness of web pages and aims to reduce eyestrain while browsing the web. Symlink to the Firefox addon.'
arch=(any)
url=https://darkreader.org/
license=(MIT)
depends=(firefox-dark-reader)
source=(https://github.com/darkreader/darkreader.git)
b2sums=('cbcc4755e0530ddf5221e9da82c27c161f811bc94d02d412d2cf97e521485dd1be1ffb3f59c3d322c21bf047b036d5be548469e26feb64789318d214f23bf1f2')
makedepends=(git)

function package() {
	install -d \
		"${pkgdir}/usr/lib/zen-browser/browser/extensions"
	ln -sf \
		"/usr/lib/firefox/browser/extensions/addon@darkreader.org.xpi" \
		"${pkgdir}/usr/lib/zen-browser/browser/extensions/addon@darkreader.org.xpi"
}
