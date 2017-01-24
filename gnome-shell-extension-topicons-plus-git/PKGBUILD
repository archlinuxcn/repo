# Maintainer: Justin Dray <justin@dray.be>
# Contributor: surefire@cryptomile.net

pkgname=gnome-shell-extension-topicons-plus-git
pkgver=19.r0.g7cd6989
pkgrel=1
pkgdesc="Shows legacy tray icons on top."
arch=('any')
url="https://extensions.gnome.org/extension/1031/topicons/"
license=('GPL')
depends=('gnome-shell')
makedepends=('git')
conflicts=('gnome-shell-extension-topicons-plus')
provides=('gnome-shell-extension-topicons-plus')
groups=('gnome-shell-extensions')
source=("git+https://github.com/phocean/TopIcons.git")
sha256sums=('SKIP')

pkgver() {
	cd TopIcons
	git describe --long | sed 's/^v//;s/\([^-]*-g\)/r\1/;s/-/./g'
}

build() {
	cd TopIcons
	make build
}

package() {
	cd TopIcons
	local uuid=$(grep -Po '(?<="uuid": ")[^"]*' _build/metadata.json)
	local destdir="$pkgdir/usr/share/gnome-shell/extensions/$uuid"

	install -dm755 "$destdir"

	cp -r _build/* "$destdir"
}
