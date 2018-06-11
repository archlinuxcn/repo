# Maintainer: Jingbei Li <i@jingbei.li>

pkgname=hdf5_18-cpp-fortran
_pkgname=hdf5
pkgver=1.8.21
pkgrel=1
arch=('i686' 'x86_64')
pkgdesc="General purpose library and file format for storing scientific data"
url="http://www.hdfgroup.org/HDF5/"
license=('custom')
depends=('zlib' 'sh' 'gcc-libs')
makedepends=('time' 'gcc-fortran')
provides=('hdf5_18')
conflicts=('hdf5_18')
source=("https://support.hdfgroup.org/ftp/HDF5/releases/${_pkgname}-1.8/${_pkgname}-${pkgver}/src/${_pkgname}-${pkgver}.tar.bz2")
sha1sums=('182b48c50b15b1271573b9536a0b0aa8800b7303')

build() {
	cd "$srcdir/${_pkgname}-${pkgver/_/-}"
	./configure --prefix=/usr --disable-static \
		--enable-hl \
		--enable-cxx \
		--enable-fortran \
		--enable-fortran2003 \
		--enable-linux-lfs \
		--enable-build-mode=production \
		--with-pic \
		--docdir=/usr/share/doc/hdf5_18/ \
		--with-pthread=/usr/lib \
		--disable-sharedlib-rpath \
		--libdir=/usr/lib/hdf5_18 \
		--includedir=/usr/include/hdf5_18
	make
}

package() {
	cd "$srcdir/${_pkgname}-${pkgver/_/-}"

	make -j1 DESTDIR="${pkgdir}" install

	rm -rf "${pkgdir}"/usr/share/hdf5_examples

	for file in "${pkgdir}"/usr/bin/*
	do
		mv "${file}" "${file}"_18
	done

	install -d m755 "${pkgdir}"/etc/ld.so.conf.d
	echo /usr/lib/hdf5_18 >> "${pkgdir}"/etc/ld.so.conf.d/hdf5_18.conf

	install -d -m755 "$pkgdir/usr/share/licenses/${pkgname}"
	install -m644 "$srcdir/${_pkgname}-${pkgver/_/-}/COPYING" \
		"$pkgdir/usr/share/licenses/${pkgname}/LICENSE"
}
