# Maintainer : George Eleftheriou <eleftg>
# Maintainer : XavierCLL <xavier dot corredor dot llano at gmail dot com>
# Contributor: Jingbei Li <petronny>
# Contributor: David Scholl <djscholl at gmail dot com>

pkgname=hdf4
pkgver=4.2.16
_pkgver=4.2.16-2
pkgrel=1
pkgdesc="General purpose library and file format for storing scientific data (version including the Java Native Interfaces - JNI)"
arch=('x86_64')
url="https://portal.hdfgroup.org/display/support/HDF+4.2.15"
license=('custom')
depends=('libaec' 'zlib' 'libjpeg-turbo' 'libtirpc')
makedepends=('java-environment')
conflicts=('hdf4-java')
provides=('hdf4-java')
replaces=('hdf4-java')
source=("https://support.hdfgroup.org/ftp/HDF/releases/HDF${_pkgver}/src/hdf-${_pkgver}.tar.bz2")
sha256sums=('c5c3234b5012258aef2e4432f649b31c21b26015afba1857ad83640c3f2b692c')

prepare() {
    mkdir -p build
    cd "hdf-${_pkgver}"
    autoreconf -i
}

build() {
    cd build

    "../hdf-${_pkgver}"/configure \
        CFLAGS="${CFLAGS} -fPIC" \
        CPPFLAGS="${CPPFLAGS} -I/usr/include/tirpc/" \
        LDFLAGS="${LDFLAGS} -ltirpc" \
        FFLAGS="${FFLAGS} -fPIC -ffixed-line-length-none" \
        LIBS="${LIBS} -ljpeg -laec -lsz" \
        JAVADOC='javadoc -Xdoclint:none' \
        --enable-shared \
        --disable-static \
        --disable-fortran \
        --disable-netcdf \
        --enable-java \
        --enable-production \
        --with-zlib \
        --with-szlib=/usr \
        --prefix=/opt/hdf4
    make
}

package() {
    cd build
    make -j1 DESTDIR="${pkgdir}" install
    install -dm 755 "${pkgdir}/usr/share/licenses/${pkgname}"
    install -Dm 644 "../hdf-${_pkgver}/COPYING" "${pkgdir}/usr/share/licenses/${pkgname}"
    install -dm 755 "${pkgdir}/etc/ld.so.conf.d"
    echo "/opt/${pkgname}/lib" > "${pkgdir}"/etc/ld.so.conf.d/${pkgname}.conf
}

