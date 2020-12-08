# Maintainer: Jiachen YANG <farseerfc@gmail.com>
_srcname=srcML
_antlr_ver=2.7.7
pkgname=srcml
pkgver=1.0.0
pkgrel=1
pkgdesc="commandline and library for srcML, an XML representation for source code"
arch=(x86_64)
url="https://www.srcml.org/"
license=('GPL')
depends=(libxml2 libxslt libarchive boost-libs curl openssl)
makedepends=(cmake boost man2html docbook2x 'java-environment' 'sh' 'antlr2')
optdepends=()
source=("$pkgname-$pkgver.tar.gz::http://131.123.42.38/lmcrs/v${pkgver}/${_srcname}-${pkgver}.tar.gz"
        "arch-build.patch"
        "https://www.antlr2.org/download/antlr-${_antlr_ver}.tar.gz"
        "gcc4.4.patch")
md5sums=('f910de40b1b7fa9a6928e7cd3d75cd2b'
         '8aaad26040808d2a0ac0793999521e9e'
         '01cc9a2a454dd33dcd8c856ec89af090'
         '8574c93f40e6477e83c29f9b07de49da')

prepare() {
        # copied from antlr2 package, rebuild with -fPIC
        cd "${srcdir}/antlr-${_antlr_ver}"
        patch -Np0 -i "${srcdir}"/gcc4.4.patch

	cd "${srcdir}/${_srcname}-${pkgver}"
        patch -Np1 -i ../arch-build.patch
}


build() {
        # copied from antlr2 package, rebuild with -fPIC
  	cd "${srcdir}/antlr-${_antlr_ver}"

  	./configure --prefix=/usr \
  	  --disable-examples \
  	  --disable-csharp
  	export LDFLAGS="$LDFLAGS -fPIC"
  	export CFLAGS="$CFLAGS -fPIC"
  	export CXXFLAGS="$CXXFLAGS -fPIC"
        make

	cd "${srcdir}/${_srcname}-${pkgver}"
	mkdir build
	cd build
        export _antlr_ver
	export ANTLR_LIBRARY="${srcdir}/antlr-${_antlr_ver}/lib/cpp/src/libantlr.a"
	cmake .. \
		-DCMAKE_INSTALL_PREFIX="/usr" \
                -DBUILD_LIBSRCML_STATIC=OFF \
                -DLINK_LIBSRCML_STATIC=OFF \
                -DANTLR_LIBRARY="${srcdir}/antlr-${_antlr_ver}/lib/cpp/src/libantlr.a" 
	make
}

package() {
	cd "$_srcname-${pkgver}"
	cd build
	make DESTDIR="$pkgdir/" install
}
