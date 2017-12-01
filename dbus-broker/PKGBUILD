# Maintainer: David Herrmann <dh.herrmann@gmail.com>
# Maintainer: Jan Alexander Steffens (heftig) <jan.steffens@gmail.com>

pkgname=dbus-broker
pkgver=9
pkgrel=1

pkgdesc='Linux D-Bus Message Broker'
arch=('i686' 'x86_64')
url='https://github.com/bus1/dbus-broker'
license=('Apache')
depends=('libsystemd' 'expat' 'glib2')
makedepends=('git' 'meson' 'systemd' 'python-docutils')

source=("https://github.com/bus1/dbus-broker/releases/download/v$pkgver/$pkgname-$pkgver.tar.xz")
sha256sums=('f1ef696e751d4d09fc5729b8ef3ce0d3c12c333136ab50f4f8c52bde48eb06e8')

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
