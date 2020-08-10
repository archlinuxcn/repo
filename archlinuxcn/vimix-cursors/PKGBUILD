# Maintainer: Mark Wagie <mark dot wagie at tutanota dot com>
pkgname=vimix-cursors
_pkgname=Vimix-cursors
pkgver=2020.02.24
_pkgver=2020-02-24
pkgrel=4
pkgdesc="An X Cursor theme inspired by Material design and based on capitaine-cursors"
arch=('any')
url="https://github.com/vinceliuice/Vimix-cursors"
license=('GPL3')
makedepends=('inkscape' 'python-cairosvg' 'xorg-xcursorgen')
source=("$pkgname-$pkgver.tar.gz::$url/archive/$_pkgver.tar.gz")
options=('!strip')
sha256sums=('69298d02264b5b15239c340f8fa899f91574c0eac49ad5745e8e588315423618')

prepare() {
	cd "$_pkgname-$_pkgver"

	# Remove prebuilt assets
	rm -rf {dist,dist-white}

	# Fix for inkscape 1.0
	sed -i 's|inkscape -z -e|inkscape -o|g' build.sh
}

build() {
	cd "$_pkgname-$_pkgver"
	./build.sh
}

package() {
	cd "$_pkgname-$_pkgver"
	install -d "$pkgdir"/usr/share/icons/{"$pkgname","$pkgname"-white}
	cp -dr --no-preserve=ownership dist/* "$pkgdir/usr/share/icons/$pkgname"
	cp -dr --no-preserve=ownership dist-white/* "$pkgdir/usr/share/icons/$pkgname-white"
}
