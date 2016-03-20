# Maintainer: Freonmonkey <freonmonkey at gmail dot com>
#
# The git version of hal-flash
#
# This project provides a stub libhal that uses UDisks and meets the needs
# for playing Flash DRM content without a full HAL installation and daemon.

pkgname=hal-flash-git
pkgver=0.3.1
pkgrel=1
pkgdesc="A libhal stub library forwarding to UDisks2 for flash to play DRM content"
arch=('i686' 'x86_64')
url="https://github.com/cshorler/hal-flash"
license=('GPL2') 
depends=('udisks2' 'dbus')
makedepends=('git')
provides=('hal=0.5.14')
conflicts=('hal')
source=("$pkgname"::'git+http://github.com/cshorler/hal-flash.git')
md5sums=('SKIP')

pkgver() {
	cd "$srcdir/$pkgname"
	# git describe --long | sed -E 's/([^-]*-g)/r\1/;s/-/./g'
	msg2 "Running configuration to determine package version..."
	autoreconf -i >/dev/null
	./configure --version | head -n1 | sed -E 's/.* configure (.+)/\1/'
}

prepare() {
	cd "$srcdir/$pkgname"

	./configure --prefix=/usr --enable-static=no
}

build() {
	cd "$srcdir/$pkgname"
	make
}

package() {
	# Install built files into the package
	cd "$srcdir/$pkgname"
	make PREFIX=/usr DESTDIR="${pkgdir}" install
	
	# Skip copying COPYING to LICENSE since it's just GPL2
} 

