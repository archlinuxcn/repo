# Maintainer: crab2313 <crab2313@gmail.com>

pkgname=rkdeveloptool
pkgver=69
pkgrel=1
pkgdesc='Development tool for Rockchip SOC'
arch=('x86_64' 'aarch64')
url='https://github.com/rockchip-linux/rkdeveloptool'
license=('GPL2')
makedepends=('git')
depends=('libusb')
source=('git+https://github.com/rockchip-linux/rkdeveloptool.git')
sha256sums=('SKIP')

pkgver() {
	cd "$srcdir/$pkgname"
	git rev-list --count HEAD
}

build() {
	cd "$srcdir/$pkgname"
	sed -i 's/-Werror/-Werror -Wno-format-truncation/' Makefile.am
	autoreconf -i
	./configure --prefix=/usr --disable-werror
	make
}

package() {
	cd "$srcdir/$pkgname"
    make DESTDIR=$pkgdir install
    install -Dm644 99-rk-rockusb.rules -t "$pkgdir/usr/lib/udev/rules.d/"
}

# vim: set sw=4 ts=4 noet:
