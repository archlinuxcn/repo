# Maintainer: Sergey Kanafyev <sergeykanafyev@gmail.com>

pkgname=swaylock-effects
pkgver=1.8.1
pkgrel=1
pkgdesc="A fancier screen locker for Wayland."
arch=('i686' 'x86_64' 'aarch64')
url="https://github.com/hboetes/$pkgname"
license=('MIT')
depends=('libxkbcommon' 'cairo' 'gdk-pixbuf2' 'pam')
makedepends=('git' 'meson' 'ninja' 'scdoc' 'wayland' 'wayland-protocols')
provides=('swaylock')
conflicts=('swaylock')
backup=('etc/pam.d/swaylock')
source=("$url/archive/v$pkgver.tar.gz")
sha256sums=('d125185d1533246faf4e96623160501fc0c9bb0fd90c29c497a4a2d79abb16cb')

build() {
	cd "$pkgname-$pkgver"
	meson build --prefix=/usr
	ninja -C build
}

package() {
	cd "$pkgname-$pkgver"
	DESTDIR="$pkgdir" ninja -C build install
}
