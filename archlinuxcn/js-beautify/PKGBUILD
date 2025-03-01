# Maintainer: Martin Rys <https://rys.rs/contact> | Toss a coin on https://rys.rs/donate

pkgname=js-beautify
pkgver=1.15.4
pkgrel=1
pkgdesc="CSS, HTML & JavaScript unobfuscator and beautifier"
arch=('any')
url="https://beautifier.io"
license=('MIT')
depends=('nodejs')
makedepends=('npm')
conflicts=('python-cssbeautifier' 'python-jsbeautifier')
source=("https://registry.npmjs.org/js-beautify/-/${pkgname}-${pkgver}.tgz")
noextract=("${pkgname}-${pkgver}.tgz")
sha256sums=('5feefb437c9467e789d179fc4cbc4f942008c05222f6b573a4f03ee41e31d9a6')

package() {
	npm install -g --prefix "${pkgdir}/usr" "${pkgname}-${pkgver}.tgz"

	install -d "${pkgdir}/usr/share/licenses/${pkgname}"
	ln -s "/usr/lib/node_modules/${pkgname}/LICENSE" "${pkgdir}/usr/share/licenses/${pkgname}/"
}
