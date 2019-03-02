# Maintainer:  Marcin Wieczorek <marcin@marcin.co>
# Contributor: Andrejs Mivreņiks <gim at fastmail dot fm>
# Contributor: Janne Haapsaari <haaja@iki.fi>
# Contributor: maus25 <mirko378@gmail.com>

pkgname=gnome-shell-pomodoro
pkgver=0.14.0
pkgrel=1
pkgdesc='A time management utility for GNOME based on the pomodoro technique'
arch=('i686' 'x86_64')
url='https://github.com/codito/gnome-pomodoro'
license=('GPL3')
depends=('gnome-desktop' 'gstreamer' 'gobject-introspection' 'libpeas' 'appstream-glib' 'gom')
makedepends=('intltool' 'vala' 'gnome-common' 'docbook2x' 'perl-xml-sax-expat')
changelog='NEWS'
source=("$pkgname-$pkgver.tar.gz::https://github.com/codito/gnome-pomodoro/archive/$pkgver.tar.gz")
sha256sums=('c29b8e3931637ca5afc36135083ea4ae906af3dfe6aa4b441f85e6d39cab98d0')

prepare() {
  cd "$srcdir/gnome-pomodoro-$pkgver"
  ./autogen.sh --prefix=/usr --datadir=/usr/share
}

build() {
  cd "$srcdir/gnome-pomodoro-$pkgver"
  make
}

package() {
  cd "$srcdir/gnome-pomodoro-$pkgver"
  make DESTDIR="$pkgdir" install
}
