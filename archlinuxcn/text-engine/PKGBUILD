# Maintainer: Mattia Borda <mattiagiovanni.borda@icloud.com>

pkgname=text-engine
pkgver=0.1.1
pkgrel=3
pkgdesc="A lightweight rich-text framework for GTK"
arch=('x86_64' 'aarch64')
url="https://github.com/mjakeman/$pkgname"
license=('LGPL3')
depends=('json-glib' 'libadwaita' 'libxml2')
makedepends=('meson')
source=($url/archive/v$pkgver.tar.gz)
sha256sums=('cf540d2c0150a46e8ec81c4532550357707c5d07b6116dc52e3869b1902f515f')

build() {
	arch-meson $pkgname-$pkgver build
	meson compile -C build
}

check() {
	meson test -C build
}

package() {
	DESTDIR="$pkgdir" meson install -C build
}
