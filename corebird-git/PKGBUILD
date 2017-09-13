# Maintainer: Fabio Loli <loli_fabio@protonmail.com>
# Contributor: Baedert

pkgname=corebird-git
epoch=1
pkgver=1.6.r58.gde21b6a9
pkgrel=1
pkgdesc="Native Gtk+ Twitter Client"
arch=('i686' 'x86_64')
license=('GPL')
url="https://corebird.baedert.org/"
depends=('gtk3'
         'rest'
         'libgee'
         'sqlite3'
         'intltool'
         'gst-plugins-good'
         'gst-plugins-bad'
         'gst-libav'
         'gspell')
makedepends=('vala' 'git' 'automake')
provides=('corebird')
conflicts=('corebird')
source=("${pkgname}::git+https://github.com/baedert/corebird")
sha1sums=('SKIP')

pkgver() {
  cd ${pkgname}
  git describe --long --tags | sed 's/\([^-]*-g\)/r\1/;s/-/./g'
}

build() {
  cd ${pkgname}
  # Add --disable-video here if you don't like the gstreamer deps
  ./autogen.sh --prefix=/usr
  make
}

package() {
  cd ${pkgname}
  make DESTDIR=$pkgdir install
}
