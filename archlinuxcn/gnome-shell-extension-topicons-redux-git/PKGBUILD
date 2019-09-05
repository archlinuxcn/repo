# Maintainer: Jianfeng Zhang <swordfeng123@gmail.com>

pkgname=gnome-shell-extension-topicons-redux-git
_projectName=TopIcons-Redux
pkgver=6+0+g5008e48
pkgrel=1
pkgdesc='TopIcons Redux is a fork of TopIcons Plus'
arch=('any')
url="https://gitlab.com/pop-planet/${_projectName}"
license=('GPL')
depends=('gnome-shell')
makedepends=('git')
provides=('gnome-shell-extension-topicons-redux')
conflicts=('gnome-shell-extension-topicons-redux')
groups=('gnome-shell-extensions')
source=("git+https://gitlab.com/pop-planet/${_projectName}.git")
sha256sums=('SKIP')

pkgver() {
	cd "${_projectName}"
	git describe --tags --long | sed 's/^v//; s/-/+/g'
}

build() {
	cd "${_projectName}"
	make build
}

package() {
	cd "${_projectName}"
	local uuid=$(grep -Po '(?<="uuid": ")[^"]*' _build/metadata.json)
	local destdir="$pkgdir/usr/share/gnome-shell/extensions/$uuid"
	install -dm755 "$destdir"
	cp -r _build/* "$destdir"
}
