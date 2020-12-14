# Maintainer: Miguel Revilla <yo at miguelrevilla dot com>

pkgname=spread-sheet-widget
pkgver=0.7
pkgrel=1
pkgdesc="Library for Gtk+ which provides a widget for viewing and manipulating 2 dimensional tabular data"
arch=('i686' 'x86_64')
url="https://www.gnu.org/software/ssw/"
license=("GPL3")
depends=(gtk3)
makedepends=(python)
source=("https://alpha.gnu.org/gnu/ssw/${pkgname}-${pkgver}.tar.gz")
md5sums=('2d26336029fc6656dabcc4fb97454fec')

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
