# Maintainer: Fabio Loli <loli_fabio@protonmail.com>
# Contributor: Baedert

pkgname=corebird-git
epoch=1
pkgver=1.7.1.r2.g8e64ad47
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
         'gspell'
         'noto-fonts-emoji')
makedepends=('vala' 'git' 'meson')
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

  meson builddir --prefix=/usr -D VIDEO=yes -D SPELLCHECK=yes
  ninja -C builddir
}

package() {
  cd ${pkgname}

  DESTDIR="${pkgdir}" ninja -C builddir install
}
