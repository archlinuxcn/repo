# Maintainer: Viachaslau Khalikin <viachaslavic'at'outlook'dot'com>

pkgname=xpm-pixbuf-git
pkgver=r1530.d290a0c
pkgrel=1
pkgdesc="Utilities for rendering XPM icons to a GdkPixbuf (devel branch)"
url="https://gitlab.gnome.org/ZanderBrown/xpm-pixbuf.git"
arch=('x86_64')
license=('LGPL-2.0-or-later')
depends=('glib2' 'glibc' 'gdk-pixbuf2')
makedepends=('git' 'meson')
provides=('xpm-pixbuf')
conflicts=('xpm-pixbuf')
source=("$pkgname::git+$url")
b2sums=('SKIP')

pkgver() {
  cd "$pkgname"
  printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
}

build() {
  arch-meson ${pkgname} build
  meson compile -C build
}

package() {
  meson install -C build --destdir "$pkgdir"
  install -Dm 644 $pkgname/COPYING "$pkgdir/usr/share/licenses/$pkgname/COPYING"
}

# vim:set ft=sh ts=2 sw=2 et:
