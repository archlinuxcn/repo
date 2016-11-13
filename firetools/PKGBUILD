# Maintainer: ajs124 < aur AT ajs124 DOT de > 

pkgname=firetools
pkgver=0.9.44
pkgrel=1
pkgdesc="GUI tools for firejail"
arch=(i686 x86_64)
license=(GPL2)
url=https://l3net.wordpress.com/projects/firejail/#firetools
depends=('firejail' 'qt5-base' 'qt5-svg')
#source=(${pkgname}-${pkgver}.tar.gz::https://github.com/netblue30/${pkgname}/archive/$pkgver.tar.gz)
source=(http://sourceforge.net/projects/firejail/files/firetools/${pkgname}-${pkgver}.tar.bz2)
sha512sums=('b920caa191f111949b1242c183fe9dbc584507ece8d5323f5e4202bc1dd18572085c7224c9d17ca54e7620dd918a851993a7d92043eb294d7323a730f9e197dc')

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
