# Maintainer: Adrian Perez de Castro <aperez@igalia.com>
pkgdesc='FUSE implementation of overlayfs'
pkgname=fuse-overlayfs
pkgver=0.7.5
pkgrel=1
arch=(x86_64)
url=https://github.com/containers/fuse-overlayfs
license=(GPL3)
depends=(fuse3)
source=("${pkgname}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz")
sha512sums=('7bc085484cbd92e8da924d30b18621ebdfc8ea524fa52a14484c472da37f92730d04e1205f14540f1f6a2dca79e44c82f6c65933f9d7c36414ec3c27452aebc3')

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
