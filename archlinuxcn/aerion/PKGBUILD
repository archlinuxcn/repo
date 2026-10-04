# Maintainer: Fermín Olaiz <fermin@olaiz.net>

pkgname=aerion
pkgver=0.3.5
pkgrel=1
pkgdesc="An Open Source Lightweight E-Mail Client"
arch=('x86_64')
url="https://aerion.3df.io"
license=('Apache-2.0')
depends=('at-spi2-core' 'cairo' 'gdk-pixbuf2' 'glib2' 'glibc' 'gtk3' 'harfbuzz' 'libsoup3' 'pango' 'webkit2gtk-4.1' 'zlib')
makedepends=('go' 'wails')
provides=('aerion')
source=("$pkgname-$pkgver.tar.gz::https://github.com/hkdb/$pkgname/archive/refs/tags/v$pkgver.tar.gz")
sha256sums=('24bcc1bcb667c35dafdc9d36ea1cf8f30b94aa6badb9ee28377ab79f31e874f8')

build() {
	cd "$srcdir/$pkgname-$pkgver"
	make build-linux
}

check() {
	cd "$srcdir/$pkgname-$pkgver"
	make test
}

package() {
	cd "$srcdir/$pkgname-$pkgver"
	install -Dm755 -t "$pkgdir/usr/bin/" build/bin/aerion
	install -Dm644 -t "$pkgdir/usr/share/licenses/$pkgname/" LICENSE
	install -Dm644 build/linux/aerion.desktop "$pkgdir/usr/share/applications/io.github.hkdb.Aerion.desktop"
	install -Dm644 build/linux/aerion.png "$pkgdir/usr/share/icons/hicolor/256x256/apps/io.github.hkdb.Aerion.png"
}
