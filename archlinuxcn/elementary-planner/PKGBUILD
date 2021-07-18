# Maintainer: Mark Wagie <mark dot wagie at tutanota dot com>
# Contributor: Jonas 'cherti' Große Sundrup <aur@letopolis.de>
pkgname=elementary-planner
pkgver=2.7
pkgrel=1
pkgdesc="Task manager with Todoist support"
arch=('x86_64')
url="https://useplanner.com"
license=('GPL3')
depends=('elementary-icon-theme' 'evolution-data-server' 'granite'
         'gtk-theme-elementary' 'libgee' 'libhandy' 'libpeas' 'libsoup' 'webkit2gtk' )
makedepends=('meson' 'vala' 'gobject-introspection')
makedepends=('meson' 'vala' 'gobject-introspection')
provides=('planner')
conflicts=('planner')
source=("planner-$pkgver.tar.gz::https://github.com/alainm23/planner/archive/$pkgver.tar.gz")
sha256sums=('cd34953867a91b2992aa4eafddc5093a695d1e6096571ade75640dddcc425d69')

build() {
	arch-meson planner-$pkgver build
	meson compile -C build
}

package() {
	DESTDIR="$pkgdir" meson install -C build

	ln -s /usr/bin/com.github.alainm23.planner "$pkgdir/usr/bin/planner"
}
