# Maintainer: Kimiblock Moe

pkgname=zen-browser-dark-reader
pkgver=4.9.110
pkgrel=1
pkgdesc='Inverts brightness of web pages and aims to reduce eyestrain while browsing the web. Symlink to the Firefox addon.'
arch=(any)
url=https://darkreader.org/
license=(MIT)
depends=(firefox-dark-reader)
source=(https://github.com/darkreader/darkreader.git)
b2sums=('34d3986cd694e8ce4199863d6fded97478a719f75d862957fdfd631784ee90cad8776d123c5dad492d337a642e733e5c0f589fe7f306a4a8a76189dae50c721b')
makedepends=(git)

function package() {
	install -d \
		"${pkgdir}/usr/lib/zen-browser/browser/extensions"
	ln -sf \
		"/usr/lib/firefox/browser/extensions/addon@darkreader.org.xpi" \
		"${pkgdir}/usr/lib/zen-browser/browser/extensions/addon@darkreader.org.xpi"
}
