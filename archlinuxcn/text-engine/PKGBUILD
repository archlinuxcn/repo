# Maintainer: musiclover <musiclover382@protonmail.com>

pkgname=text-engine
pkgver=0.1.1
pkgrel=1
pkgdesc="A lightweight rich-text framework for GTK"
arch=('x86_64')
url="https://github.com/mjakeman/$pkgname"
license=('LGPL3')
depends=('gtk4' 'json-glib' 'libadwaita' 'libxml2')
makedepends=('meson')
source=($url/archive/v$pkgver.tar.gz)
sha256sums=('cf540d2c0150a46e8ec81c4532550357707c5d07b6116dc52e3869b1902f515f')

build() {
  arch-meson $pkgname-$pkgver build
  meson compile -C build
}

package() {
  meson install -C build --destdir "$pkgdir"
  install -Dm644 $pkgname-$pkgver/COPYING "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
