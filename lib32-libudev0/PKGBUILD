# Maintainer: Maxime Gauduin <alucryd@archlinux.org>
# Contributor: jdarch <jda.cloud+archlinux@gmail.com>

pkgname=lib32-libudev0
pkgver=182
pkgrel=2
pkgdesc='Dynamic library to access udev device information (legacy)'
arch=('x86_64')
url='https://www.kernel.org/pub/linux/utils/kernel/hotplug/udev/udev.html'
license=('GPL')
depends=('lib32-glibc')
makedepends=('gcc-multilib' 'gperf' 'lib32-kmod' 'lib32-util-linux' 'usbutils')
source=("https://www.kernel.org/pub/linux/utils/kernel/hotplug/udev-${pkgver}.tar.xz")
sha256sums=('adb8892f3b8e4b7163703ed4a545774721a3d55a1062de001f08c477c03d97ab')

prepare() {
  cd udev-${pkgver}

  autoreconf -fi

  sed 's/input.h/input-event-codes.h/' -i Makefile.in
  sed '20a#include <stdint.h>' -i src/mtd_probe/mtd_probe.h
}

build() {
  cd udev-${pkgver}

  export CC='gcc -m32'
  export CXX='g++ -m32'
  export PKG_CONFIG_PATH='/usr/lib32/pkgconfig'

  ./configure \
    --prefix='/usr' \
    --libdir='/usr/lib32' \
    --libexecdir='/usr/lib32/udev' \
    --sysconfdir='/etc' \
    --disable-gudev \
    --disable-introspection \
    --with-systemdsystemunitdir='/usr/lib32/systemd/system'
  make LIBS='-lrt'
}

package() {
  cd udev-${pkgver}

  make DESTDIR="${pkgdir}" install
  rm -rf "${pkgdir}"/{etc,usr/{bin,include,lib32/{libudev.so,pkgconfig,udev,systemd},share}}
}

# vim: ts=2 sw=2 et:
