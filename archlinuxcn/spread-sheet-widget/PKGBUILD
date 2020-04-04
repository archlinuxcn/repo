# Maintainer: Miguel Revilla <yo at miguelrevilla dot com>

pkgname=spread-sheet-widget
pkgver=0.3
pkgrel=2
pkgdesc="Library for Gtk+ which provides a widget for viewing and manipulating 2 dimensional tabular data"
arch=('i686' 'x86_64')
url="https://www.gnu.org/software/ssw/"
license=("GPL3")
depends=(gtk3)
makedepends=(python)
source=("https://alpha.gnu.org/gnu/ssw/${pkgname}-${pkgver}.tar.gz")
md5sums=('9bd94714a18229eb9e9a2b79dda30e1f')

prepare() {
	cd "${srcdir}/${pkgname}-${pkgver}"

	./configure --prefix=/usr
}

build() {
	cd "${srcdir}/${pkgname}-${pkgver}"

	make
}

package() {
	cd "${srcdir}/${pkgname}-${pkgver}"

	make DESTDIR="${pkgdir}" install
}

# End of file
