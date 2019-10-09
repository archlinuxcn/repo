# Maintainer: Adrian Perez de Castro <aperez@igalia.com>
pkgdesc='FUSE implementation of overlayfs'
pkgname=fuse-overlayfs
pkgver=0.6.4
pkgrel=1
arch=(x86_64)
url='https://github.com/containers/fuse-overlayfs'
license=(GPL3)
depends=(fuse3)
source=("${url}/archive/v${pkgver}.tar.gz")
sha512sums=('0b014bdcc7d90167f1a0f64f0ace1c3e028e423a5226ea01cbcf0de602fab2cf48aad3ce636aa003145026c2d096ae51261838dbf0e58ff47092627e97d19195')

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
