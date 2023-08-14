# Maintainer: DDoSolitary <DDoSolitary@gmail.com>

pkgname=gtkwave-gtk3
pkgver=3.3.117
pkgrel=1
pkgdesc='A wave viewer which reads LXT, LXT2, VZT, GHW and VCD/EVCD files (gtk3 version)'
arch=(x86_64)
url=https://gtkwave.sourceforge.net
license=(GPL MIT)
depends=(
	bzip2 xz gtk3 desktop-file-utils dconf judy
	libbz2.so libgdk-3.so libgdk_pixbuf-2.0.so libgio-2.0.so libglib-2.0.so libgobject-2.0.so libgtk-3.so libpango-1.0.so libpangocairo-1.0.so
)
makedepends=(gperf)
conflicts=(gtkwave)
provides=(gtkwave)
source=(http://gtkwave.sourceforge.net/$pkgname-$pkgver.tar.gz)
sha256sums=('3cf1537586a911cbb0601af8fa18cf6da708c8a14a71f69ce3cb9118e8571db9')

prepare() {
	cd $pkgname-$pkgver
	sed -i '/define GLOBALS_H/a #include <X11\/X.h>' src/globals.h
}

build() {
	cd $pkgname-$pkgver
	./configure \
		--prefix=/usr \
		--disable-tcl \
		--disable-mime-update \
		--with-gsettings \
		--enable-judy \
		--enable-gtk3
	make
}

package() {
	cd $pkgname-$pkgver
	make DESTDIR="$pkgdir" install
	install -Dm644 LICENSE.TXT "$pkgdir/usr/share/licenses/$pkgname/LICENSE.TXT"
}

