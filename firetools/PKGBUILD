# Maintainer: ajs124 < aur AT ajs124 DOT de > 

pkgname=firetools
pkgver=0.9.50
pkgrel=1
pkgdesc="GUI tools for firejail"
arch=(i686 x86_64)
license=(GPL2)
url=https://l3net.wordpress.com/projects/firejail/#firetools
depends=('firejail' 'qt5-base' 'qt5-svg')
#source=(${pkgname}-${pkgver}.tar.gz::https://github.com/netblue30/${pkgname}/archive/$pkgver.tar.gz)
source=(http://sourceforge.net/projects/firejail/files/firetools/${pkgname}-${pkgver}.tar.xz)
sha512sums=('5ed6dca2311350ceeaf520cb1d077c95978e6cbea7ee13f800b1085ed6ff5323a022d82a874f12b06ca22c221534dc61b2ac6e6b80cc05a669d4c704bc4bfbd1')

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
