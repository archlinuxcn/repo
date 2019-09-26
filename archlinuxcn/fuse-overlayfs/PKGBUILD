# Maintainer: Adrian Perez de Castro <aperez@igalia.com>
pkgdesc='FUSE implementation of overlayfs'
pkgname=fuse-overlayfs
pkgver=0.6.3
pkgrel=1
arch=(x86_64)
url='https://github.com/containers/fuse-overlayfs'
license=(GPL3)
depends=(fuse3)
source=("${url}/archive/v${pkgver}.tar.gz")
sha512sums=('13c11b9d5deb52d4e607e01989b0f77e76f9b1dc458ddb94d032c8ef58837a470666c296e0f500fc4658802d09d3169c0881296dac937d2a6b53f818edbdb6f4')

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
