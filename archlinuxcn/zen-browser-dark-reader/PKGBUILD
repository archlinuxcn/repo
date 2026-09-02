# Maintainer: Kimiblock Moe

pkgname=zen-browser-dark-reader
pkgver=4.9.130
pkgrel=1
pkgdesc='Inverts brightness of web pages and aims to reduce eyestrain while browsing the web. Symlink to the Firefox addon.'
arch=(any)
url=https://darkreader.org/
license=(MIT)
depends=(firefox-dark-reader)
source=(https://github.com/darkreader/darkreader.git)
b2sums=('17ff34e38631c4acad19bd361a68af874ad31d7e1b774c4e28d9c7c7902a582f37aeaa139aaf891a5314751fd1e2e226db6fef39ed9c547d2c1eadffcfbb4a1d')
makedepends=(git)

function package() {
	install -d \
		"${pkgdir}/usr/lib/zen-browser/browser/extensions"
	ln -sf \
		"/usr/lib/firefox/browser/extensions/addon@darkreader.org.xpi" \
		"${pkgdir}/usr/lib/zen-browser/browser/extensions/addon@darkreader.org.xpi"
}
