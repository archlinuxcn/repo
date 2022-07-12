# Maintainer: itsme <mymail@ishere.ru>

pkgname=swaylock-effects
pkgver=1.6.10
pkgrel=1
pkgdesc="A fancier screen locker for Wayland."
arch=('i686' 'x86_64')
url="https://github.com/jirutka/$pkgname"
license=('MIT')
depends=('libxkbcommon' 'cairo' 'gdk-pixbuf2' 'pam')
makedepends=('git' 'meson' 'ninja' 'scdoc' 'wayland' 'wayland-protocols')
provides=('swaylock' 'swaylock-effects')
conflicts=('swaylock' 'swaylock-effects-git')
source=("https://github.com/jirutka/$pkgname/archive/v$pkgver.tar.gz")
sha256sums=('0bfd0a73557ead32364175210397e73af172713ca9035bc73f60c26c7d4513bf')

build() {
	cd "$pkgname-$pkgver"
	meson build --prefix=/usr
	ninja -C build
}

package() {
	cd "$pkgname-$pkgver"
	DESTDIR="$pkgdir" ninja -C build install
}
