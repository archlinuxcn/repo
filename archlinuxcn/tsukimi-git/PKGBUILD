# Maintainer: Eikano <lcuoin@gmail.com>
# Maintainer: Merrkry <merrkry@tsubasa.moe>
_pkgname="tsukimi"
pkgname="${_pkgname}-git"
pkgver=26.8.4.r1635.g71ec30
pkgrel=1
epoch=1
pkgdesc='A simple third-party Emby client'
arch=('x86_64')
url="https://github.com/tsukinaha/tsukimi"
license=('GPL-3.0-or-later')
provides=('tsukimi')
conflicts=('tsukimi')
depends=(
	'mpv'
	'ffmpeg'
	'libadwaita'
	'gstreamer'
	'gtk4'
)
makedepends=(
	'cargo'
	'git'
	'meson'
	'blueprint-compiler'
)
source=(
	git+https://github.com/tsukinaha/tsukimi.git
)
sha256sums=(
	'SKIP'
)
options=(!lto)

pkgver() {
	cd "${_pkgname}"
	echo $(grep -oPm1 '^version = "\K[^"]+' crates/tsukimi/Cargo.toml).r$(git rev-list --count HEAD).g$(git describe --long --tags --abbrev=7 | tail -c 7)
}

build() {
	arch-meson "${srcdir}/${_pkgname}" build
	meson compile -C build
}

package() {
	meson install -C build --no-rebuild --destdir "$pkgdir"
}
