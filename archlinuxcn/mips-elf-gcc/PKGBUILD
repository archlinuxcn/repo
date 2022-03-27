# Maintainer:  Angelo ELias Dalzotto <angelodalzotto97@gmail.com>

_target=mips-elf
pkgname=$_target-gcc
pkgver=11.2.0
pkgrel=1
#_snapshot=8-20180427
pkgdesc='The GNU Compiler Collection - cross compiler for MIPS ELF (bare-metal) target'
arch=('i686' 'x86_64')
url='https://gcc.gnu.org/'
license=(GPL)
depends=($_target-binutils libmpc)
replaces=('cross-mips-elf-gcc')
conflicts=('cross-mips-elf-gcc')
options=('!ccache' '!distcc' '!emptydirs' '!libtool' '!strip')
source=(https://ftp.gnu.org/gnu/gcc/gcc-$pkgver/gcc-$pkgver.tar.xz{,.sig})
sha256sums=('d08edc536b54c372a1010ff6619dd274c0f1603aa49212ba20f7aa2cda36fa8b'
			'6bb782c64994e655abd5cf596ed7879cc52e5bcb0352be636ea9eec7caa98837')
validpgpkeys=('13975A70E63C361C73AE69EF6EEB81F8981C74C7')	# Richard Guenther <richard.guenther@gmail.com>

prepare() {
	cd gcc-$pkgver

	echo $pkgver > gcc/BASE-VER

	# hack! - some configure tests for header files using "$CPP $CPPFLAGS"
 	sed -i "/ac_cpp=/s/\$CPPFLAGS/\$CPPFLAGS -O2/" {libiberty,gcc}/configure

 	mkdir -p "$srcdir"/build-gcc
}

build() {
	cd "$srcdir"/gcc-$pkgver
	
	./configure \
		--target=$_target \
		--prefix=/usr \
		--with-sysroot=/usr/$_target \
		--enable-languages=c,c++ \
		--enable-plugins \
		--disable-nls \
		--disable-threads \
		--disable-multilib \
		--disable-shared \
		--with-gnu-as \
		--with-gnu-ld \
		--without-headers 
	
	make all-gcc "inhibit_libc=true"
}

package() {
	cd $srcdir/gcc-$pkgver
	
	make DESTDIR=${pkgdir} install-gcc
	
	# remove these files as they are already in the system
	# (with native gcc)
	rm -Rf $pkgdir/usr/share/{man,info}
}