# Maintainer: Alexander Seiler <seileralex@gmail.com>
pkgname=sioyek
pkgver=2.0.0
pkgrel=1
pkgdesc="PDF viewer for research papers and technical books."
arch=('x86_64')
license=('GPL3')
url="https://github.com/ahrm/sioyek"
depends=(
	'gumbo-parser'
	'harfbuzz'
	'jbig2dec'
	'libmupdf'
	'openjpeg2'
	'qt5-3d'
	'qt5-base'
	'zlib')
source=("$pkgname-$pkgver.tar.gz::$url/archive/v$pkgver.tar.gz")
sha256sums=('92398b6da5e297c59f22cd3c6b562194846f28bc17bb4ae9432869aafeb5df17')

prepare() {
	cd "$pkgname-$pkgver"
	sed -i 's/-lmupdf-threads/-lfreetype -lgumbo -ljbig2dec -lopenjp2 -ljpeg/' pdf_viewer_build_config.pro
	sed -i '/#define LINUX_STANDARD_PATHS/s/\/\///' pdf_viewer/main.cpp
}

build() {
	cd "$pkgname-$pkgver"
	./build_linux.sh
}

package() {
	cd "$pkgname-$pkgver"
	install -D build/sioyek -t "$pkgdir/usr/bin/"
	install -Dm644 LICENSE -t "$pkgdir/usr/share/licenses/$pkgname/"
	install -Dm644 resources/sioyek-icon-linux.png -t "$pkgdir/usr/share/icons/"
	install -Dm644 resources/$pkgname.desktop -t "$pkgdir/usr/share/applications/"
	install -Dm644 build/shaders/* -t "$pkgdir/usr/share/$pkgname/shaders/"
	install -Dm644 -t "$pkgdir/etc/sioyek/" build/keys.config build/prefs.config
	install -Dm644 -t "$pkgdir/usr/share/man/man1" resources/sioyek.1
  install -Dm644 -t "$pkgdir/usr/share/sioyek" build/tutorial.pdf
}
