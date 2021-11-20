# Maintainer: itsme <mymail@ishere.ru>

pkgname=swaylock-effects
pkgver=1.6.3
_pkgver=1.6-3
pkgrel=2
pkgdesc="A fancier screen locker for Wayland."
arch=('i686' 'x86_64')
url="https://github.com/mortie/$pkgname"
license=('MIT')
depends=('libxkbcommon' 'cairo' 'gdk-pixbuf2' 'pam')
makedepends=('git' 'meson' 'ninja' 'scdoc' 'wayland' 'wayland-protocols')
provides=('swaylock' 'swaylock-effects')
conflicts=('swaylock' 'swaylock-effects-git')
source=("https://github.com/mortie/$pkgname/archive/v$_pkgver.tar.gz")
sha256sums=('c7c4e420276aef9bd952b321b68e24c31f050859a226edb8fde15a5ccee1a9fe')

build() {
	cd "$pkgname-$_pkgver"
	meson build --prefix=/usr
	ninja -C build
}

package() {
	cd "$pkgname-$_pkgver"
	DESTDIR="$pkgdir" ninja -C build install
}
