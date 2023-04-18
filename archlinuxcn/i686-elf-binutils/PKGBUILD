# Maintainer: randomnobody <nobody "at" 420blaze "dot" it>
# Contributor: Finlay Maroney <finman292004@protonmail.com>

_target=i686-elf
pkgname=$_target-binutils
pkgver=2.40
pkgrel=1
pkgdesc='A set of programs to assemble and manipulate binary and object files for the i686-elf target'
arch=(i686 x86_64)
url='https://www.gnu.org/software/binutils/'
license=('GPL')
depends=(zlib libelf)
options=(!emptydirs !docs)
source=(https://mirrors.kernel.org/gnu/binutils/binutils-$pkgver.tar.xz{,.sig})
sha256sums=('0f8a4c272d7f17f369ded10a4aca28b8e304828e95526da482b0ccc4dfc9d8e1'
            'SKIP')
validpgpkeys=(3A24BC1E8FB409FA9F14371813FCEF89DD9E3C4F) # Nick Clifton (Chief Binutils Maintainer) <nickc@redhat.com>
_basedir=binutils-$pkgver

prepare() {
  cd $_basedir

  mkdir $srcdir/binutils-build
}

build() {
  cd binutils-build

  $srcdir/$_basedir/configure \
    --target=$_target \
    --with-sysroot \
    --prefix=/usr \
    --bindir=/usr/bin \
    --libdir=/usr/lib/i686-elf/ \
    --disable-nls \
    --disable-werror

  make
}

check() {
  cd binutils-build

  # do not abort on errors - manually check log files
  make -k check
}

package() {
  cd binutils-build

  make DESTDIR="$pkgdir" install

  rm -r ${pkgdir}/usr/share/{info,man}
}
