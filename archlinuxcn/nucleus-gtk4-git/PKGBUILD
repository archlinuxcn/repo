# Maintainer: Mumi Jim <echo "=02bj5yav9Gb0V3bA1Waq9VatVXb" | rev | base64 -d>
# Co-Maintainer: Misaka13514 <Misaka13514 at gmail dot com>
# This package name is used to distinguish it from another package name with a different function, nucleus-bin.

pkgname="nucleus-gtk4-git"
_pkgname=${pkgname%-git}
_appname="nucleus"
pkgver=1.r36.g72b9de27
pkgrel=1
pkgdesc="Chemistry educational software written in Python"
arch=(any)
url="https://codeberg.org/lo-vely/nucleus"
license=('GPL-3.0-or-later')
depends=('gtk4' 'libadwaita' 'python-gobject' 'python')
makedepends=('blueprint-compiler' 'git' 'meson' 'ninja')
provides=("${_pkgname}" "${_appname}")
conflicts=("${_pkgname}" "${_appname}")
source=("git+$url.git")
sha256sums=('SKIP')

pkgver() {
  cd "${srcdir}/${_appname}"
  git describe --long --tags --abbrev=8 | sed 's/^v//;s/\([^-]*-g\)/r\1/;s/-/./g'
}

prepare() {
  cd "${srcdir}/${_appname}"
  meson subprojects download
}

build() {
  cd "${srcdir}/${_appname}"
  arch-meson . build
  meson compile -C build
}

check() {
  cd "${srcdir}/${_appname}"
  meson test -C build
}

package() {
  cd "${srcdir}/${_appname}"
  meson install -C build --destdir "$pkgdir"
}
