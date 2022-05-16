# Maintainer: drakkan <nicola dot murino at gmail dot com>
# Contributor: XZS <d dot f dot fischer at web dot de>
# Contributor: Carl George < arch at cgtx dot us >
# Contributor: Janne Haapsaari <haaja@iki.fi>
# Contributor: Christopher Krooß <didi2002 at web.de>

pkgname=gnome-shell-extension-dash-to-dock
_pkgname=dash-to-dock
pkgver=72
pkgrel=2
epoch=1
pkgdesc="Move the dash out of the overview transforming it in a dock"
arch=('any')
url="https://micheleg.github.io/dash-to-dock/"
license=('GPL')
depends=('gnome-shell')
makedepends=('intltool' 'gettext' 'git' 'sassc')
_commit=fc795c52b7f973eee065547c4d3eb92a6cbada4a
source=("git+https://github.com/micheleg/dash-to-dock.git#commit=$_commit"
  "1720.patch")
sha256sums=('SKIP'
  'f9f1c15e6e1cdfa027478f35ded42fdbb438b7f98650f9f54c9145a36cdd6fa3')

pkgver() {
  cd "${srcdir}"/${_pkgname}
  git describe --tags | sed 's/^extensions\.gnome\.org-v//g' | sed 's/-/+/g'
}

prepare() {
  cd "${srcdir}"/${_pkgname}
  # https://github.com/micheleg/dash-to-dock/pull/1720
  patch -Np1 -i ../1720.patch
}

build() {
  cd "${srcdir}"/${_pkgname}
  make
}

package() {
  cd "${srcdir}"/${_pkgname}
  make DESTDIR="${pkgdir}" VERSION="${pkgver}" install
}

# vim:set ts=2 sw=2 et:
