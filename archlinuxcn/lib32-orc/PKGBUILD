# Maintainer: Patrick Northon <northon_patrick3@yahoo.ca>
# Contributor: Maxime Gauduin <alucryd@archlinux.org>
# Contributor: Jan Alexander Steffens (heftig) <heftig@archlinux.org>

pkgname=lib32-orc
pkgver=0.4.42
pkgrel=1
pkgdesc="Optimized Inner Loop Runtime Compiler (32-bit)"
url="https://gstreamer.freedesktop.org/modules/orc.html"
arch=(x86_64)
license=(BSD-3-Clause)
depends=(
  'lib32-gcc-libs'
  'lib32-glibc'
  'orc'
)
makedepends=(
  'git'
  'meson'
  'valgrind'
)
source=("git+https://gitlab.freedesktop.org/gstreamer/orc.git?signed#tag=$pkgver")
b2sums=('65b8fc3a403fb0eeb89edf865f8631bc56997149ef8e09a6a20a5e36a2fea84ab1b5cc7e916e0016d3e49cdc188957279f16baba615648bc7c7dbaf7f57e791a')
validpgpkeys=(
  'D637032E45B8C6585B9456565D2EEE6F6F349D7C' # Tim-Philipp Müller <tim@centricular.com>
)

build() {
  arch-meson orc build --cross-file lib32 -D hotdoc=disabled
  meson compile -C build
}

check() {
  meson test -C build --print-errorlogs
}

package() {
  provides=(liborc{,-test}-${pkgver%.*}.so)

  meson install -C build --destdir "$pkgdir"
  rm -r "$pkgdir"/usr/{bin,include}
  install -Dt "$pkgdir/usr/share/licenses/$pkgname" -m644 orc/COPYING
}

# vim:set sw=2 sts=-1 et:
