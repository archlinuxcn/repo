# Maintainer: Adrian Perez de Castro <aperez@igalia.com>
pkgdesc='FUSE implementation of overlayfs'
pkgname=fuse-overlayfs
pkgver=0.7
pkgrel=1
arch=(x86_64)
url='https://github.com/containers/fuse-overlayfs'
license=(GPL3)
depends=(fuse3)
source=("${url}/archive/v${pkgver}.tar.gz")
sha512sums=('ccca7d081c71529537f644a477c034a15e142c371c89a1595a77c2f96b1bfb5aa996a4bf108a589eab02f012666fbfd2946bc196734ee6f0a08f0301def886bd')

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
