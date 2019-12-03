# Maintainer: Adrian Perez de Castro <aperez@igalia.com>
pkgdesc='FUSE implementation of overlayfs'
pkgname=fuse-overlayfs
pkgver=0.7.2
pkgrel=1
arch=(x86_64)
url='https://github.com/containers/fuse-overlayfs'
license=(GPL3)
depends=(fuse3)
source=("${url}/archive/v${pkgver}.tar.gz")
sha512sums=('fe881a8c27419544aa57ea3b02f574ecdd15362792d3ba56efbe887bd45dcbcbccc35745b2cf5c2e92b1471dd51d6ecbba9278aa0af524c394f808ea97124441')

build ()
{
	cd "${pkgname}-${pkgver}"
	NOCONFIGURE=1 ./autogen.sh
	./configure --prefix=/usr \
		--sbindir=/usr/bin \
		--mandir=/usr/share/man
	make -j$(nproc)
}

package ()
{
	cd "${pkgname}-${pkgver}"
	make DESTDIR="${pkgdir}" install
}
