# Maintainer: Angelo Elias Dalzotto <angelodalzotto97@gmail.com>

_target="mips-elf"
pkgname=$_target-binutils
pkgver=2.39
pkgrel=1
pkgdesc="A set of programs to assemble and manipulate binary and object files for the MIPS ELF (bare-metal) architecture"
arch=('i686' 'x86_64')
url="http://www.gnu.org/software/binutils/"
license=('GPL')
depends=('zlib')
replaces=('cross-mips-elf-binutils')
conflicts=('cross-mips-elf-binutils')
provides=('cross-mips-elf-binutils')
source=(https://ftp.gnu.org/gnu/binutils/binutils-$pkgver.tar.bz2{,.sig})
sha256sums=('da24a84fef220102dd24042df06fdea851c2614a5377f86effa28f33b7b16148'
            'SKIP')
validpgpkeys=('3A24BC1E8FB409FA9F14371813FCEF89DD9E3C4F')	# Nick Clifton (Chief Binutils Maintainer) <nickc@redhat.com>

prepare() {
	cd binutils-$pkgver
	sed -i "/ac_cpp=/s/\$CPPFLAGS/\$CPPFLAGS -O2/" libiberty/configure
}


build() {
	cd binutils-$pkgver
	
	./configure --target=$_target \
				--with-sysroot=/usr/$_target \
				--prefix=/usr \
				--with-gnu-as \
				--with-gnu-ld \
				--disable-nls \
				--enable-ld=default \
				--enable-gold \
				--enable-plugins \
				--enable-deterministic-archives

	make
}

package() {
	cd binutils-$pkgver
	
	make DESTDIR="$pkgdir" install
	
	# Remove file conflicting with host binutils and manpages for MS Windows tools
	rm "$pkgdir"/usr/share/man/man1/mips-elf-{dlltool,windres,windmc}*
	rm "$pkgdir"/usr/lib/bfd-plugins/libdep.so

	# Remove info documents that conflict with host version
 	rm -r "$pkgdir"/usr/share/info
}
