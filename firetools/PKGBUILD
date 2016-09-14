# Maintainer: ajs124 < aur AT ajs124 DOT de > 

pkgname=firetools
pkgver=0.9.40
pkgrel=1
pkgdesc="GUI tools for firejail"
arch=(i686 x86_64)
license=(GPL2)
url=https://l3net.wordpress.com/projects/firejail/#firetools
depends=('firejail' 'qt5-base' 'qt5-svg')
#source=(${pkgname}-${pkgver}.tar.gz::https://github.com/netblue30/${pkgname}/archive/$pkgver.tar.gz)
source=(http://sourceforge.net/projects/firejail/files/firetools/${pkgname}-${pkgver}.tar.bz2)
sha512sums=('ddecb608fb5a42b9fd564554679edfe4f1d18c8ab19f78275e00714d65a84c4a514d0f64eade7e459cd21cc0a9b7a127002e58205446a8cac889560eafc9e64a')

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
