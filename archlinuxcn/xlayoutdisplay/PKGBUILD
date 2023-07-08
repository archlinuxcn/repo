# Maintainer: Alexander Courtis <alex@courtis.org>
pkgname=xlayoutdisplay
pkgver=1.4.0
pkgrel=2
pkgdesc="Detects and arranges linux display outputs, using XRandR for detection and xrandr for arrangement."
arch=('x86_64')
url="https://github.com/alex-courtis/xlayoutdisplay"
license=('Apache')
depends=('xorg-xrandr' 'xorg-xrdb' 'libxcursor' 'libprocps')
makedepends=('git' 'make' 'boost')
source=("https://github.com/alex-courtis/xlayoutdisplay/archive/v$pkgver.tar.gz")
sha256sums=('f369c6c47134079a0c2ef3c42775816a732b1ec52fe97c015f807bcf1a7d1775')
install=install

build() {
	cd "$pkgname-$pkgver"
	make xlayoutdisplay
}

package() {
	cd "$pkgname-$pkgver"
	make PREFIX="/usr" DESTDIR="$pkgdir/" install
	install -Dm644 README.md               -t "$pkgdir/usr/share/doc/$pkgname"
	install -Dm644 99-xlayoutdisplay.rules -t "$pkgdir/usr/share/doc/$pkgname"
	install -Dm644 LICENSE                 -t "$pkgdir/usr/share/licenses/$pkgname"
	install -Dm644 NOTICE                  -t "$pkgdir/usr/share/licenses/$pkgname"
}
