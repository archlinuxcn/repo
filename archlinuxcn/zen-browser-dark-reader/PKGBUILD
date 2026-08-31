# Maintainer: Kimiblock Moe

pkgname=zen-browser-dark-reader
pkgver=4.9.129
pkgrel=1
pkgdesc='Inverts brightness of web pages and aims to reduce eyestrain while browsing the web. Symlink to the Firefox addon.'
arch=(any)
url=https://darkreader.org/
license=(MIT)
depends=(firefox-dark-reader)
source=(https://github.com/darkreader/darkreader.git)
b2sums=('e340883f66d2d5f462052f117db9f7084ee21565aa05f48e41eab9db6e6982b5b72f3053721f5ec9791f5fa171527b781f33a71a8173ac2ab90ff9fc42476732')
makedepends=(git)

function package() {
	install -d \
		"${pkgdir}/usr/lib/zen-browser/browser/extensions"
	ln -sf \
		"/usr/lib/firefox/browser/extensions/addon@darkreader.org.xpi" \
		"${pkgdir}/usr/lib/zen-browser/browser/extensions/addon@darkreader.org.xpi"
}
