# Maintainer: Kimiblock Moe

pkgname=zen-browser-dark-reader
pkgver=4.9.124
pkgrel=1
pkgdesc='Inverts brightness of web pages and aims to reduce eyestrain while browsing the web. Symlink to the Firefox addon.'
arch=(any)
url=https://darkreader.org/
license=(MIT)
depends=(firefox-dark-reader)
source=(https://github.com/darkreader/darkreader.git)
b2sums=('738bae3467b6d4325618cf02cc9dd6027cf84be77b47a5d8278058a26e8339c11f5c6bc24f5a040bb64676a147f6f1ed0720561ffcff2806854112d3198cd9fa')
makedepends=(git)

function package() {
	install -d \
		"${pkgdir}/usr/lib/zen-browser/browser/extensions"
	ln -sf \
		"/usr/lib/firefox/browser/extensions/addon@darkreader.org.xpi" \
		"${pkgdir}/usr/lib/zen-browser/browser/extensions/addon@darkreader.org.xpi"
}
