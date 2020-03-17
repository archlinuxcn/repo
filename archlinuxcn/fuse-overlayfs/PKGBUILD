# Maintainer: Adrian Perez de Castro <aperez@igalia.com>
pkgdesc='FUSE implementation of overlayfs'
pkgname=fuse-overlayfs
pkgver=0.7.8
pkgrel=1
arch=(x86_64)
url=https://github.com/containers/fuse-overlayfs
license=(GPL3)
depends=(fuse3)
source=("${pkgname}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz")
sha512sums=('0eb3ca179ff88ad4ba783646e51aaab147ae5fdffbc48b2121a481ff3030d35d1f3e32b838e1f41a275c08d345ef397b86ff2e4a6768ead98a1bb1d56922f689')

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
