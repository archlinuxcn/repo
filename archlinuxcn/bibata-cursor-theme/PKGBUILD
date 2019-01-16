pkgname=bibata-cursor-theme
pkgver=0.4.1
pkgrel=1
pkgdesc="Material Based Cursor Theme."
arch=('any')
url="https://github.com/KaizIqbal/Bibata_Cursor.git"
license=('GPL')
makedepends=('inkscape' 'xorg-xcursorgen' 'gtk-engine-murrine')
source=("https://github.com/KaizIqbal/Bibata_Cursor/archive/v${pkgver}.tar.gz")
sha256sums=('01d06515f6139d796820cb4ca121185ee65a8789bfdd88e0600bcd749e3eea3b')

build() {
	cd "$srcdir/Bibata_Cursor-${pkgver}"
	./build.sh
}

package() {
	mkdir -p "$pkgdir/usr/share/icons"
	mv "$srcdir/Bibata_Cursor-${pkgver}/Bibata_Ice" "$pkgdir/usr/share/icons/Bibata_Ice"
	mv "$srcdir/Bibata_Cursor-${pkgver}/Bibata_Oil" "$pkgdir/usr/share/icons/Bibata_Oil"
	mv "$srcdir/Bibata_Cursor-${pkgver}/Bibata_Amber" "$pkgdir/usr/share/icons/Bibata_Amber"
}
