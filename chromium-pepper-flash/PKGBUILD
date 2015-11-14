# Maintainer: ava1ar <mail(at)ava1ar(dot)me>

pkgname=chromium-pepper-flash
pkgdesc="Google Chrome's Pepper Flash plugin for Chromium (stable version)"
_verbld=46.0.2490.86-1
pkgver=19.0.0.245
pkgrel=1
epoch=1
arch=('i686' 'x86_64')
url="http://www.google.com/chrome"
license=('custom:chrome')
conflicts=('chromium-pepper-flash-dev')
provides=('pepper-flash')
source=(${pkgname}-license.html::https://www.google.com/chrome/intl/en/eula_text.html)
source_i686=("https://dl.google.com/linux/chrome/rpm/stable/i386/google-chrome-stable-${_verbld}.i386.rpm")
source_x86_64=(https://dl.google.com/linux/chrome/rpm/stable/x86_64/google-chrome-stable-${_verbld}.x86_64.rpm)
sha256sums=('b35811bb330576631e64f7885c66720e0be4ca81afb04328b3a0f288a708e37f')
sha256sums_i686=('c18f4445c14081216492922e2b82151df442fbc4e7b4b2875084a5d140e1af13')
sha256sums_x86_64=('bf2d446b42520b00f9a3ec3763c8c3c33632db7c2385270dc4dfb3e5401371b8')

package() {
	# create required directories
	install -d "${pkgdir}"/usr/lib/PepperFlash
	# copy required files
	install -m644 "${srcdir}"/opt/google/chrome/PepperFlash/* "${pkgdir}"/usr/lib/PepperFlash
	# copy license
	install -Dm644 "${srcdir}"/${pkgname}-license.html "${pkgdir}"/usr/share/licenses/${pkgname}/license.html
}
