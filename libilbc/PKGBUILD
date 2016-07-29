# Maintainer: Daniel Bermond < yahoo-com: danielbermond >

pkgname=libilbc
pkgver=2.0.2
pkgrel=1
pkgdesc="A friendly copy of the iLBC codec from the WebRTC project"
arch=('i686' 'x86_64')
url="https://github.com/TimothyGu/libilbc/"
license=('custom')
depends=('glibc')
provides=('libilbc' 'libilbc.so')
conflicts=('ilbc' 'libilbc-git')
source=("https://github.com/TimothyGu/libilbc/releases/download/v${pkgver}/${pkgname}-${pkgver}.tar.bz2")
sha256sums=('88e2dc14e1fccd7b7a0d7f84e96ac22a33c3c86820cee4b0a05e3dcc08c2b096')

build() {
	cd "$pkgname"-"$pkgver"
	
	./configure \
                --prefix=/usr \
                --enable-static=no \
                --enable-shared=yes
	make
}

package() {
	cd "$pkgname"-"$pkgver"
	make DESTDIR="$pkgdir/" install
	install -D -m644 COPYING "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
