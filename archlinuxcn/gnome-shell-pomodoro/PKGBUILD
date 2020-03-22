# Maintainer:  Marcin Wieczorek <marcin@marcin.co>
# Contributor: Pranav Jerry <libreinator@disroot.org>
# Contributor: Andrejs Mivreņiks <gim at fastmail dot fm>
# Contributor: Janne Haapsaari <haaja@iki.fi>
# Contributor: maus25 <mirko378@gmail.com>

pkgname=gnome-shell-pomodoro
pkgver=0.16.1
pkgrel=1
pkgdesc='A time management utility for GNOME based on the pomodoro technique'
arch=('i686' 'x86_64')
url='https://github.com/codito/gnome-pomodoro'
license=('GPL3')
depends=('gnome-desktop' 'gstreamer' 'gobject-introspection' 'libpeas' 'appstream-glib' 'gom')
makedepends=('git' 'intltool' 'vala' 'gnome-common' 'docbook2x' 'perl-xml-sax-expat' 'xorgproto')
changelog='NEWS'
source=("gnome-pomodoro::git+https://github.com/codito/gnome-pomodoro.git#branch=gnome-3.36")
sha256sums=('SKIP')

prepare() {
  cd "$srcdir/gnome-pomodoro"
  ./autogen.sh --prefix=/usr --datadir=/usr/share
}

build() {
  cd "$srcdir/gnome-pomodoro"
  make
}

package() {
  cd "$srcdir/gnome-pomodoro"
  make DESTDIR="$pkgdir" install
}
