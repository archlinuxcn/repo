# $Id: PKGBUILD 143671 2015-10-11 15:34:05Z fyan $
# Contributor: Pierre Schmitz <pierre@archlinux.de>
# Contributor: François Charette <firmicus@gmx.net>
# x32 Maintainer: Fantix King <fantix.king@gmail.com>

pkgname=libx32-xz
_pkgbasename=xz
pkgver=5.2.2
pkgrel=1.1
pkgdesc='Library and command line tools for XZ and LZMA compressed files (x32 ABI)'
arch=('x86_64')
url='http://tukaani.org/xz/'
license=('GPL' 'LGPL' 'custom')
depends=('libx32-glibc' 'xz')
makedepends=('gcc-multilib-x32')
source=("http://tukaani.org/xz/${_pkgbasename}-${pkgver}.tar.gz"
        "http://tukaani.org/xz/${_pkgbasename}-${pkgver}.tar.gz.sig")
md5sums=('7cf6a8544a7dae8e8106fdf7addfa28c'
         'SKIP')
validpgpkeys=('3690C240CE51B4670D30AD1C38EE757D69184620')  # Lasse Collin

build() {
	cd ${srcdir}/xz-${pkgver}

	export CC="gcc -mx32"
	export PKG_CONFIG_PATH="/usr/libx32/pkgconfig"
	
	./configure --prefix=/usr \
		--libdir=/usr/libx32 \
		--disable-rpath \
		--enable-werror
	make
}

check() {
	cd ${srcdir}/xz-${pkgver}

	make check
}

package() {
	cd ${srcdir}/xz-${pkgver}
	
	make DESTDIR=${pkgdir} install

	rm -rf "${pkgdir}"/usr/{bin,include,share}
	install -d -m755 "${pkgdir}"/usr/share/licenses
	ln -s xz "$pkgdir/usr/share/licenses/libx32-xz"
}
