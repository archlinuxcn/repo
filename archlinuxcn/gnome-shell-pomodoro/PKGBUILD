# Maintainer: Liam Timms <timms5000@gmail.com>
# Contributor: gj545rndmu <6zogm6z2nh at bljvf anonbox net>
# Contributor: Pranav Jerry <libreinator@disroot.org>
# Contributor:  Marcin Wieczorek <marcin@marcin.co>
# Contributor: Andrejs Mivreņiks <gim at fastmail dot fm>
# Contributor: Janne Haapsaari <haaja@iki.fi>
# Contributor: maus25 <mirko378@gmail.com>

pkgname=gnome-shell-pomodoro
pkgver=0.25.1
pkgrel=1
pkgdesc='A time management utility for GNOME based on the pomodoro technique'
arch=('i686' 'x86_64')
url='https://github.com/gnome-pomodoro/gnome-pomodoro'
license=('GPL3')
depends=('gobject-introspection' 'glib2' 'gom' 'gtk3' 'cairo' 'glibc' 'libpeas' 'sqlite' 'gstreamer' 'libcanberra')
makedepends=('meson' 'vala')
source=("$pkgname-$pkgver.tar.gz::https://github.com/gnome-pomodoro/gnome-pomodoro/archive/$pkgver.tar.gz")
sha256sums=('dc661cddafd359a90192642e51d84e55c353ec7e0918ca3359b1c6f4d4b66de1')

prepare() {
  cd "$srcdir/gnome-pomodoro-$pkgver"
}

build() {
  cd "$srcdir/gnome-pomodoro-$pkgver"
  arch-meson build
  meson compile -C build
}

package() {
  cd "$srcdir/gnome-pomodoro-$pkgver"
  meson install -C build --destdir "$pkgdir"
}

