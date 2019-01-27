# Maintainer: Andrew Sun <adsun701@gmail.com>
# Contributor: orumin <dev@orum.in>

_basename=libevdev
pkgname="lib32-$_basename"
pkgver=1.6.0
pkgrel=1
pkgdesc="Wrapper library for evdev devices (32-bit)"
arch=('x86_64')
url="http://www.freedesktop.org/wiki/Software/libevdev/"
license=(custom:X11)
depends=('lib32-glibc' "$_basename")
makedepends=('python2' 'lib32-gcc-libs' 'lib32-check' 'valgrind' 'doxygen')
#checkdepends=('kmod')
source=(https://www.freedesktop.org/software/$_basename/$_basename-$pkgver.tar.xz)
sha512sums=('73046da447773716c9f0c9f511f3a0a6ababcf92a146eba363014afcbdb465f4c3cd8be0917f2f01561a72f24f20fe8ecd333467437d9d85c03afcb433d05060')

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
