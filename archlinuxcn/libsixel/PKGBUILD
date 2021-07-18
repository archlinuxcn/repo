# Maintainer: BrainDamage
pkgname="libsixel"
pkgrel=1
pkgver="v1.9.0"
pkgdesc="provides a codec for DEC SIXEL graphics, and some converter programs"
arch=("i686" "x86_64")
url="https://github.com/libsixel/libsixel"
license=("MIT")
depends=("libjpeg-turbo" "libpng" "python" "curl")
sha256sums=('f39a32a8a6e9f952941319fb421e10287cd2c954f2f69e416b0b20445c67496c')
source=("https://github.com/libsixel/libsixel/archive/${pkgver}.tar.gz")

build() {
	cd "${srcdir}/${pkgname}-${pkgver#v}"
	./configure --prefix=/usr --enable-python --enable-tests
	make
}

check() {
	cd "${srcdir}/${pkgname}-${pkgver#v}"
	make test
}

package() {
	cd "${srcdir}/${pkgname}-${pkgver#v}"
	make DESTDIR="${pkgdir}" install
	install -Dm 644 LICENSE "${pkgdir}/usr/share/licenses/libsixel/LICENSE"
}
