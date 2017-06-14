# Contributor: Daniel Kirchner <daniel AT ekpyron DOT org>

pkgname=mingw-w64-zlib
pkgver=1.2.11
pkgrel=1
pkgdesc="A compression/decompression Library (mingw-w64)"
arch=('any')
license=('custom:zlib')
depends=(mingw-w64-crt)
makedepends=(mingw-w64-gcc)
url="http://www.zlib.net/"
source=("http://zlib.net/zlib-${pkgver}.tar.gz")
options=(!strip !buildflags staticlibs)
md5sums=('1c9f62f0778697a09d36121ead88e08e')

_architectures="i686-w64-mingw32 x86_64-w64-mingw32"

build() {
  for _arch in ${_architectures}; do
    rm -rf "${srcdir}/build-${_arch}"
  	cp -r "${srcdir}/zlib-${pkgver}" "${srcdir}/build-${_arch}"
  	cd "${srcdir}/build-${_arch}"
  	sed -ie "s,dllwrap,${_arch}-dllwrap," win32/Makefile.gcc
  	
  	CFLAGS="-O2 -g -pipe -Wall -Wp,-D_FORTIFY_SOURCE=2 -fexceptions --param=ssp-buffer-size=4" \
    ./configure --prefix=/usr/${_arch} -shared -static
  	make -f win32/Makefile.gcc \
  	    CC=${_arch}-gcc \
    	AR=${_arch}-ar \
    	RC=${_arch}-windres \
    	STRIP=${_arch}-strip \
    	IMPLIB=libz.dll.a \
    	CFLAGS="-O2 -g -pipe -Wall -Wp,-D_FORTIFY_SOURCE=2 -fexceptions --param=ssp-buffer-size=4"
  done
}

package () {
  for _arch in ${_architectures}; do
    cd "${srcdir}/build-${_arch}"
    install -d "${pkgdir}/usr/${_arch}/"{bin,include,lib}
    install -m644 -t "${pkgdir}/usr/${_arch}/include" zlib.h zconf.h
    install -m644 -t "${pkgdir}/usr/${_arch}/lib" libz.a libz.dll.a
    install -m755 -t "${pkgdir}/usr/${_arch}/bin" zlib1.dll
    install -d "${pkgdir}/usr/${_arch}/lib/pkgconfig"
    
    sed "s,@prefix@,/usr/${_arch},;s,@exec_prefix@,\${prefix},;s,@libdir@,\${exec_prefix}/lib,;s,@sharedlibdir@,\${libdir},;s,@includedir@,\${prefix}/include,;s,@VERSION@,$pkgver," < zlib.pc.in > "${pkgdir}/usr/${_arch}/lib/pkgconfig/zlib.pc"
    
    ${_arch}-strip -x -g "${pkgdir}/usr/${_arch}/bin/"*.dll
    ${_arch}-strip -g "${pkgdir}/usr/${_arch}/lib/"*.a
  done
}
