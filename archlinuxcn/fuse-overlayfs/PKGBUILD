# Maintainer: Adrian Perez de Castro <aperez@igalia.com>
pkgdesc='FUSE implementation of overlayfs'
pkgname=fuse-overlayfs
pkgver=0.7.6
pkgrel=1
arch=(x86_64)
url=https://github.com/containers/fuse-overlayfs
license=(GPL3)
depends=(fuse3)
source=("${pkgname}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz")
sha512sums=('097796c3911697793b6a8e2444dc9241c5308e0cbfd4263a768e69684ff856a2a0df44c1ec687b4a9872e41cc8d27697255d1d70517887437cc6424c973a826a')

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
