# Maintainer: Andrew Sun <adsun701 at gmail dot com>
# Contributor: orumin <dev@orum.in>

_basename=libevdev
pkgname="lib32-$_basename"
pkgver=1.9.1
pkgrel=1
pkgdesc="Wrapper library for evdev devices (32-bit)"
arch=('x86_64')
url="https://www.freedesktop.org/wiki/Software/libevdev/"
license=(custom:X11)
depends=('lib32-glibc' "$_basename")
makedepends=('python2' 'gcc-multilib' 'lib32-check' 'valgrind' 'doxygen' 'lib32-gcc-libs')
#checkdepends=('kmod')
source=(https://www.freedesktop.org/software/$_basename/$_basename-$pkgver.tar.xz)
sha512sums=('7d845ce2279d2e2ef12437f6218550265ea0c85e5b6c0d116aff09787b73626b338fe3084baff060085d393688b5ae3d33772689e0581684eff257af01c4c645')

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
