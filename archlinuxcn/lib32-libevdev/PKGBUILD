# Maintainer: Andrew Sun <adsun701@gmail.com>
# Contributor: orumin <dev@orum.in>

_basename=libevdev
pkgname="lib32-$_basename"
pkgver=1.8.0
pkgrel=1
pkgdesc="Wrapper library for evdev devices (32-bit)"
arch=('x86_64')
url="https://www.freedesktop.org/wiki/Software/libevdev/"
license=(custom:X11)
depends=('lib32-glibc' "$_basename")
makedepends=('python2' 'gcc-multilib' 'lib32-check' 'valgrind' 'doxygen' 'lib32-gcc-libs')
#checkdepends=('kmod')
source=(https://www.freedesktop.org/software/$_basename/$_basename-$pkgver.tar.xz)
sha512sums=('8d285632f4fe87c01e81f94e514bec4e37fed4bc44d6d38b9297dba1114e42f6ed8d143fc05f3d0e8d51b08b659e34481dc4c65f60421c54e2f3e11efbafdeb4')

build() {
  cd $_basename-$pkgver

  export CC='gcc -m32'
  export CXX='g++ -m32'
  export PKG_CONFIG_PATH='/usr/lib32/pkgconfig'

  ./configure --prefix=/usr \
    --disable-static \
    --libdir=/usr/lib32 
  make
}

check() {
  cd $_basename-$pkgver
  # test suite requires root access and needs to load uinput module
  # that's not possible in our chroot
  #modprobe uinput
  make check || /bin/true
}

package() {
  cd $_basename-$pkgver
  make DESTDIR="$pkgdir" install
  rm -rf ${pkgdir}/usr/{bin,share,include}
}
