# Maintainer: Amin Vakil <info at aminvakil dot com>
# Contributor: XZS <d dot f dot fischer at web dot de>
# Contributor: Llewelyn Trahaearn <WoefulDerelict at GMail dot com>
# Contributor: Janne Haapsaari <haaja@iki.fi>
# Contributor: Christopher Krooß <didi2002 at web.de>

_srcname=dash-to-dock
pkgname=gnome-shell-extension-dash-to-dock-git
pkgver=70.r0.g8dbf454
pkgrel=1
pkgdesc="move the dash out of the overview transforming it in a dock"
arch=('any')
url="https://micheleg.github.io/dash-to-dock/"
_giturl="git+https://github.com/micheleg/dash-to-dock/"
license=('GPL')
depends=('gnome-shell')
makedepends=('git' 'sassc')
conflicts=('gnome-shell-extension-dash-to-dock')
provides=('gnome-shell-extension-dash-to-dock')
source=("git+https://github.com/micheleg/${_srcname}.git")
sha256sums=('SKIP')

pkgver() {
  cd "${_srcname}"
  git describe --long --tags 2>/dev/null | sed 's/[^[:digit:]]*\(.\+\)-\([[:digit:]]\+\)-g\([[:xdigit:]]\{7\}\)/\1.r\2.g\3/;t;q1'
  [ ${PIPESTATUS[0]} -eq 0 ] || \
printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
}

build() {
  export SASS=sassc
  cd "${_srcname}"
  make VERSION="$pkgver" _build
}

package() {
  cd "${_srcname}"
  make
  make DESTDIR=${pkgdir} install
}
