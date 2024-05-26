# Maintainer: Carl Smedstad <carl.smedstad at protonmail dot com>
# Contributor: danb (danb) <danb (at) hasi.it>

pkgname=avizo
pkgver=1.3
pkgrel=1
pkgdesc="A neat notification daemon"
url="https://github.com/misterdanb/avizo"
arch=(x86_64)
license=(GPL-3.0-only)
depends=(
  alsa-utils
  cairo
  dbus
  glib2
  glibc
  gobject-introspection
  gtk-layer-shell
  gtk3
)
makedepends=(
  meson
  ninja
  vala
)
optdepends=(
  'brightnessctl: for helper script lightctl'
  'light: for helper script lightctl'
  'pamixer: for helper script volumectl'
)

source=("$pkgname-$pkgver.tar.gz::$url/archive/refs/tags/$pkgver.tar.gz")
sha256sums=('2b1f5817a916e518b0c10c4c94a3678a5054b879eb32c10b5d1425faa6387127')

_archive="$pkgname-$pkgver"

build() {
  cd "$_archive"

  arch-meson . build
  meson compile -C build
}

# No tests available.

package() {
  cd "$_archive"

  meson install -C build --destdir "$pkgdir"
}
