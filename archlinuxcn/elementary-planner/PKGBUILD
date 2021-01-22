# Maintainer: Mark Wagie <mark dot wagie at tutanota dot com>
# Contributor: Jonas 'cherti' Große Sundrup <aur@letopolis.de>
pkgname=elementary-planner
pkgver=2.6.9
pkgrel=1
pkgdesc="Task manager with Todoist support"
arch=('x86_64')
url="https://useplanner.com"
license=('GPL3')
depends=('libsoup' 'granite' 'webkit2gtk' 'evolution-data-server'
         'libpeas' 'gtk-theme-elementary' 'elementary-icon-theme')
makedepends=('meson' 'vala' 'gobject-introspection')
provides=('planner')
conflicts=('planner')
source=("planner-$pkgver.tar.gz::https://github.com/alainm23/planner/archive/$pkgver.tar.gz")
sha256sums=('40520c9ade68300089494b085ae4cd1ce076606b58d528df57f911fd4fdcdb74')

build() {
	arch-meson planner-$pkgver build
	meson compile -C build
}

package() {
	DESTDIR="$pkgdir" meson install -C build

	ln -s /usr/bin/com.github.alainm23.planner "$pkgdir/usr/bin/planner"
}
