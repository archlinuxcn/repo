# Maintainer: Patrick Northon <northon_patrick3@yahoo.ca>
# Contributor: Maxime Gauduin <alucryd@archlinux.org>
# Contributor: Jan Alexander Steffens (heftig) <heftig@archlinux.org>

pkgname=lib32-orc
pkgver=0.4.44
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
b2sums=('9a8a076322f2d3933bd731f21b0bf5b7c0aeec4426fdaa92b8e74d625c495aab2a0f976a58cbc7e1fbbae901999c9f27088ea3bd2b5d024f4e079c4874484c74')
validpgpkeys=(
  'D637032E45B8C6585B9456565D2EEE6F6F349D7C' # Tim-Philipp Müller <tim@centricular.com>
)

build() {
  arch-meson orc build --cross-file lib32 -D hotdoc=disabled -D orc-target=avx,sse,mmx,altivec,neon,mips,c64x,riscv,lsx,lasx
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
