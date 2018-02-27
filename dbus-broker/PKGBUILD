# Maintainer: David Herrmann <dh.herrmann@gmail.com>
# Maintainer: Jan Alexander Steffens (heftig) <jan.steffens@gmail.com>

pkgname=dbus-broker
pkgver=11
pkgrel=1

pkgdesc='Linux D-Bus Message Broker'
arch=('i686' 'x86_64')
url='https://github.com/bus1/dbus-broker'
license=('Apache')
depends=('libsystemd' 'expat' 'glib2')
makedepends=('git' 'meson' 'systemd' 'python-docutils')

source=("https://github.com/bus1/dbus-broker/releases/download/v$pkgver/$pkgname-$pkgver.tar.xz")
sha256sums=('6cad2a5ed3dc66b7727c5507f0b7a343374f91bffc2b2b12b579b62e9a71f9e9')

prepare() {
  rm -Rf build
  mkdir build
}

build() {
  cd build
  CFLAGS="$CFLAGS -Wno-unused-parameter"
  CFLAGS="$CFLAGS -Wno-maybe-uninitialized"
  arch-meson ../$pkgname-$pkgver
  ninja
}

check() {
  cd build
  meson test
}

package() {
  cd build
  DESTDIR="$pkgdir" ninja install
}

# vim:set sw=2 et:
