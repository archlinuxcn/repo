# Maintainer:  Gabriel Souza Franco <Z2FicmllbGZyYW5jb3NvdXphQGdtYWlsLmNvbQ==>
# Contributor: Florian Pritz
# Contributor: Christian Hesse <mail@eworm.de>
# Contributor: Thomas Dziedzic < gostrc at gmail >
# Contributor: mickele
# Contributor: marcus fritzsch <fritschy@googlemail.com>

pkgbase=coin
pkgname=(coin coin-docs)
pkgver=3.1.3
pkgrel=18
pkgdesc='A high-level 3D graphics toolkit on top of OpenGL'
url='https://bitbucket.org/Coin3D/coin'
license=('GPL')
arch=('i686' 'x86_64')
depends=('libgl' 'libsm')
makedepends=('doxygen')
optdepends=('openal: sound/dynamic linking support'
            'fontconfig: dynamic linking support'
            'zlib: dynamic linking support'
            'freetype2: dynamic linking support'
            'js: dynamic linking support'
            'simage: image format support')
source=("https://bitbucket.org/Coin3D/coin/downloads/Coin-${pkgver}.tar.gz"
        'fixed-wrong-assignment.patch'
        'gcc6-crash-fix.patch'
        'remove-expat.patch')
sha256sums=('583478c581317862aa03a19f14c527c3888478a06284b9a46a0155fa5886d417'
            'f71a13da97f6000ce66a63ae780a67226bcd906f9abf289436ea6e218d77fae0'
            '23326a4790f7a9c9654bd114baec400386a350bf49450c72c17a369056287c53'
            'ab939e75dd5e9be87781ab6c9f4c69c9a85c6d6c6c554249fbd3f4e646b4a7de')

prepare() {
	cd Coin-${pkgver}

	# fix prefix in coin-config
	sed -i '/^prefix/c prefix="/usr/"' bin/coin-config

	# fix compilation
	sed -i '/^#include "fonts\/freetype.h"$/i #include <cstdlib>\n#include <cmath>' src/fonts/freetype.cpp

	# fix http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=667139
	sed -i '/^#include <Inventor\/C\/basic.h>$/i #include <Inventor/C/errors/debugerror.h>' include/Inventor/SbBasic.h

	# fixes char to pointer assignment
	patch -i "$srcdir/fixed-wrong-assignment.patch" -p1

	# fix crash at startup
	patch -i "$srcdir/gcc6-crash-fix.patch" -p1

	# remove bundled expat
	rm -rf src/xml/expat
	patch -i "$srcdir/remove-expat.patch" -p1
}

build() {
	cd Coin-${pkgver}

	./configure \
		--prefix=/usr \
		--mandir=/usr/share/man \
		--enable-optimization \
		--enable-3ds-import \
		--enable-javascript-api \
		--enable-threadsafe \
		--enable-exceptions \
		--enable-man \
		--enable-html \
		--with-mesa \
		--disable-debug \
		--enable-shared \
		--disable-maintainer-mode \
		--disable-dependency-tracking \
		--enable-system-expat

	make
}

package_coin() {
	optdepends+=('coin-docs: Coin documentation')

	cd Coin-${pkgver}

	make DESTDIR="${pkgdir}" HTMLDIRS= install

	# final adjustments
	for _FILE in threads deprecated errors events; do
		mv  "${pkgdir}/usr/share/man/man3/${_FILE}.3" "${pkgdir}/usr/share/man/man3/coin-${_FILE}.3"
	done
}

package_coin-docs() {
	pkgdesc='A high-level 3D graphics toolkit on top of OpenGL (docs)'
	arch=(any)
	depends=()

	cd Coin-${pkgver}/html

	make DESTDIR="${pkgdir}" install-html
}
