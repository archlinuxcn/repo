# Maintainer: BrainDamage
pkgname="libsixel"
pkgrel=3
pkgver="v1.8.6"
pkgdesc="provides a codec for DEC SIXEL graphics, and some converter programs"
arch=("i686" "x86_64")
url="https://saitoha.github.io/libsixel/"
license=("MIT")
depends=("libjpeg-turbo" "libpng" "python" "curl")
sha256sums=('37611d60c7dbcee701346967336dbf135fdd5041024d5f650d52fae14c731ab9')
source=("https://github.com/saitoha/libsixel/archive/${pkgver}.tar.gz")

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
