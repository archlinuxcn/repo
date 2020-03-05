# Maintainer: Adrian Perez de Castro <aperez@igalia.com>
pkgdesc='FUSE implementation of overlayfs'
pkgname=fuse-overlayfs
pkgver=0.7.7
pkgrel=1
arch=(x86_64)
url=https://github.com/containers/fuse-overlayfs
license=(GPL3)
depends=(fuse3)
source=("${pkgname}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz")
sha512sums=('e5e2625ec0d4c3a22f1c1b5029b60aae65c41414f754c7e4578367824befb1a30f2050ff5ceb64004d67fd639efef529b9e76827148791a8bed7627a41213dc1')

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
