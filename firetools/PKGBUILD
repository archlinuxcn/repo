# Maintainer: ajs124 < aur AT ajs124 DOT de > 

pkgname=firetools
pkgver=0.9.46
pkgrel=1
pkgdesc="GUI tools for firejail"
arch=(i686 x86_64)
license=(GPL2)
url=https://l3net.wordpress.com/projects/firejail/#firetools
depends=('firejail' 'qt5-base' 'qt5-svg')
#source=(${pkgname}-${pkgver}.tar.gz::https://github.com/netblue30/${pkgname}/archive/$pkgver.tar.gz)
source=(http://sourceforge.net/projects/firejail/files/firetools/${pkgname}-${pkgver}.tar.xz)
sha512sums=('3f2dec44e7aba9350e8b60891f23e8e34892233b08643f4d30addc284306ec469b3ad2aa46b72a97244fd25f19cf22cd6b9547c9f83026948f83eeeb528850f6')

build() {
	cd "${srcdir}/${pkgname}-${pkgver}"
	# fix build
	export CFLAGS=${CFLAGS/-fsanitize=undefined/}
	./configure --prefix=/usr
	make
}

package() {
	cd "${srcdir}/${pkgname}-${pkgver}"
	make DESTDIR="${pkgdir}" install
}
