# Maintainer: Martin Rys <https://rys.rs/contact> | Toss a coin on https://rys.rs/donate

pkgname=js-beautify
pkgver=1.15.4
pkgrel=2
pkgdesc="CSS, HTML & JavaScript unobfuscator and beautifier"
arch=('any')
url="https://beautifier.io"
license=('MIT')
depends=('nodejs')
makedepends=('npm')
conflicts=('python-cssbeautifier' 'python-jsbeautifier')
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/beautifier/js-beautify/archive/v${pkgver}.tar.gz")
noextract=("${pkgname}-${pkgver}.tar.gz")
sha256sums=('54f1d231b2ddd5727d8add4b6486ec7799508227ca0185bc08bb9da908c55ac5')

package() {
	npm install -g --prefix "${pkgdir}/usr" "${pkgname}-${pkgver}.tar.gz"

	install -d "${pkgdir}/usr/share/licenses/${pkgname}"
	ln -s "/usr/lib/node_modules/${pkgname}/LICENSE" "${pkgdir}/usr/share/licenses/${pkgname}/"
}
