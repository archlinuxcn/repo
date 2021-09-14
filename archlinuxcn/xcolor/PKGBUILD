# Maintainer: Samuel Laurén <samuel dot lauren at iki dot fi>
pkgname=xcolor
pkgver=0.5.1
pkgrel=2
pkgdesc="Lightweight color picker for X11"
arch=(x86_64)
url="https://github.com/Soft/xcolor"
license=("MIT")
depends=("libxcb" "libxcursor" "libx11")
makedepends=("rust" "cargo" "python")
source=("https://github.com/Soft/xcolor/archive/${pkgver}.tar.gz")
sha256sums=("cff417d0ccbece766c66a183413e167868fdbd98b8129516ff9021a4b11a5647")


build() {
	cd "$srcdir/xcolor-${pkgver}"
	cargo build --release
}

package() {
	cd "$srcdir/xcolor-${pkgver}"
	install -D -m755 target/release/xcolor "$pkgdir/usr/bin/xcolor"
	install -D -m644 man/xcolor.1 "$pkgdir/usr/share/man/man1/xcolor.1"
	install -D -m644 extra/xcolor.desktop "$pkgdir/usr/share/applications/xcolor.desktop"
	install -D -m644 extra/icons/xcolor-16.png "$pkgdir/usr/share/icons/hicolor/16x16/apps/xcolor.png"
	install -D -m644 extra/icons/xcolor-24.png "$pkgdir/usr/share/icons/hicolor/24x24/apps/xcolor.png"
	install -D -m644 extra/icons/xcolor-32.png "$pkgdir/usr/share/icons/hicolor/32x32/apps/xcolor.png"
	install -D -m644 extra/icons/xcolor-48.png "$pkgdir/usr/share/icons/hicolor/48x48/apps/xcolor.png"
	install -D -m644 extra/icons/xcolor-256.png "$pkgdir/usr/share/icons/hicolor/256x256/apps/xcolor.png"
	install -D -m644 extra/icons/xcolor-512.png "$pkgdir/usr/share/icons/hicolor/512x512/apps/xcolor.png"
	install -D -m644 LICENSE "$pkgdir/usr/share/licenses/xcolor/LICENSE"
}
