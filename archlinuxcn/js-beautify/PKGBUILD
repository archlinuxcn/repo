# Maintainer: Martin Rys <https://rys.rs/contact>

pkgname=js-beautify
pkgver=2.0.3
pkgrel=1
pkgdesc="CSS, HTML & JavaScript unobfuscator and beautifier"
arch=('any')
url="https://beautifier.io"
license=('MIT')
depends=('nodejs')
makedepends=('npm')
conflicts=('python-cssbeautifier' 'python-jsbeautifier')
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/beautifier/js-beautify/archive/v${pkgver}.tar.gz")
noextract=("${pkgname}-${pkgver}.tar.gz")
sha256sums=('87ae2c001eba3186d0737be6adfd277d19cd66b16b48b454707805b5259e9fc7')

package() {
	npm install -g --prefix "${pkgdir}/usr" "${pkgname}-${pkgver}.tar.gz"

	install -d "${pkgdir}/usr/share/licenses/${pkgname}"
	ln -s "/usr/lib/node_modules/${pkgname}/LICENSE" "${pkgdir}/usr/share/licenses/${pkgname}/"
}
