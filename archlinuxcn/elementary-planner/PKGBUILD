# Maintainer: Mark Wagie <mark dot wagie at tutanota dot com>
# Contributor: Jonas 'cherti' Große Sundrup <aur@letopolis.de>
pkgname=elementary-planner
_app_id=com.github.alainm23.planner
pkgver=3.0.2
pkgrel=1
pkgdesc="Task manager with Todoist support"
arch=('x86_64')
url="https://useplanner.com"
license=('GPL3')
depends=('elementary-icon-theme' 'evolution-data-server' 'granite'
         'gtk-theme-elementary' 'libgee' 'libhandy' 'libpeas' 'libsoup' 'webkit2gtk')
makedepends=('gobject-introspection' 'meson' 'vala' )
checkdepends=('appstream')
provides=('planner')
conflicts=('planner')
source=("planner-$pkgver.tar.gz::https://github.com/alainm23/planner/archive/$pkgver.tar.gz")
sha256sums=('51c6cde71ba79a6e9aa780d4dc80068c89c16d530853b92903f6680ceb539417')

build() {
  arch-meson planner-$pkgver build
  meson compile -C build
}

check() {

# No tests defined
#  meson test -C build --print-errorlogs

  desktop-file-validate build/data/${_app_id}.desktop
  appstreamcli validate build/data/${_app_id}.appdata.xml
}

package() {
  meson install -C build --destdir "$pkgdir"

  ln -s /usr/bin/${_app_id} "$pkgdir/usr/bin/planner"
}
