# Maintainer: ARKye03 <rafa03-dev@proton.me>

pkgname=icon-browser-git
pkgver=r14.036b062 # Can't be empty, will be set dynamically
pkgrel=2
pkgdesc="Browse system installed icon themes"
arch=(x86_64)
license=('MIT')
url="https://github.com/Aylur/icon-browser"
depends=(
	gtk4
	glib2
	gjs
)
makedepends=(
	git
	gobject-introspection
	meson
	ninja
	npm
	esbuild
	desktop-file-utils
	libadwaita
)
source=("$pkgname::git+$url")
sha256sums=('SKIP')

pkgver() {
	cd "$pkgname" || exit
	printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short=7 HEAD)"
}

build() {
	cd "$pkgname" || exit
	npm install
	arch-meson --prefix /usr build
	meson compile -C build
}

package() {
	cd "$pkgname" || exit
	meson install -C build --destdir "$pkgdir"
}
