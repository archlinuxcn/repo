# Maintainer: OriginCode <origincoder@yahoo.com>
_pkgname=bilibili-live-helper
pkgname=bilibili-live-helper-git
entryname="Bilibili Live Helper"
pkgver=r30.5ede513
pkgrel=1
pkgdesc="A Helper for Bilibili Live."
arch=('x86_64')
url="https://github.com/pandaGao/bilibili-live-helper"
install=${pkgname}.install
license=('MIT')
depends=('libxtst' 'gtk2' 'libxss' 'nss' 'gconf' 'alsa-lib')
makedepends=('git' 'npm')
provides=('bilibili-live-helper')
conflicts=('bilibili-live-helper')
source=('git+https://github.com/pandaGao/bilibili-live-helper' "${entryname}.desktop" "${_pkgname}.ico")
md5sums=('SKIP' 'SKIP' 'SKIP')

prepare() {
	cd "$srcdir/$_pkgname"
	git checkout develop
}

pkgver() {
	cd "$srcdir/$_pkgname"
	printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
}

build() {
	cd "$srcdir/$_pkgname"
	npm run-script build
	cd builds
	mv Bilibili直播弹幕库-linux-x64 ${_pkgname}
	cd ${_pkgname}
	mv Bilibili直播弹幕库 ${_pkgname}
}

package() {
	install -d "${pkgdir}/opt/${_pkgname}"
	cp -r ${srcdir}/${_pkgname}/builds/${_pkgname}/* "${pkgdir}/opt/${_pkgname}"
	install -Dm755 ./"${entryname}.desktop" "${pkgdir}/usr/share/applications/${entryname}.desktop"
	install -Dm444 ./"${_pkgname}.ico" "${pkgdir}/usr/share/icons/hicolor/128x128/${_pkgname}.ico"
}
