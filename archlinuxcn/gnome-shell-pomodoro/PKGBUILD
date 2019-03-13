# Maintainer:  Marcin Wieczorek <marcin@marcin.co>
# Contributor: Andrejs Mivreņiks <gim at fastmail dot fm>
# Contributor: Janne Haapsaari <haaja@iki.fi>
# Contributor: maus25 <mirko378@gmail.com>

pkgname=gnome-shell-pomodoro
pkgver=0.14.0
pkgrel=2
pkgdesc='A time management utility for GNOME based on the pomodoro technique'
arch=('i686' 'x86_64')
url='https://github.com/codito/gnome-pomodoro'
license=('GPL3')
depends=('gnome-desktop' 'gstreamer' 'gobject-introspection' 'libpeas' 'appstream-glib' 'gom')
makedepends=('intltool' 'vala' 'gnome-common' 'docbook2x' 'perl-xml-sax-expat')
changelog='NEWS'
source=("$pkgname-$pkgver.tar.gz::https://github.com/codito/gnome-pomodoro/archive/$pkgver.tar.gz"
        "issue390.patch::https://github.com/codito/gnome-pomodoro/commit/6557fafe7b74875a37e1172cd3eb15ec0e6af6f8.patch"
        "issue379.patch::https://github.com/codito/gnome-pomodoro/commit/0c249f36b66e85ee5132cabb23aad4747fc5545d.patch"
        "issue388.patch::https://github.com/codito/gnome-pomodoro/commit/23b0e344fe939a41d6ecc874b49403fa4e03566d.patch")
sha256sums=('c29b8e3931637ca5afc36135083ea4ae906af3dfe6aa4b441f85e6d39cab98d0'
            '4c38c8b1030b877afe8bdd92115517923fa8debdaf06adf8161ea2a8b08844c3'
            '7ab9a0f289b1f2ae25cc206fee2003c25a3d29b452ddd9a721c4c9546a4fad83'
            '56616288bd63c58dce79a035988f7013f2f36330063c345326794de1dc274a82')

prepare() {
  cd "$srcdir/gnome-pomodoro-$pkgver"
  ./autogen.sh --prefix=/usr --datadir=/usr/share
  patch -Np1 -i ../issue390.patch
  patch -Np1 -i ../issue379.patch
  patch -Np1 -i ../issue388.patch
}

build() {
  cd "$srcdir/gnome-pomodoro-$pkgver"
  make
}

package() {
  cd "$srcdir/gnome-pomodoro-$pkgver"
  make DESTDIR="$pkgdir" install
}
