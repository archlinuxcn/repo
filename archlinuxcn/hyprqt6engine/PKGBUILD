# Maintainer: Sola <archlinux+aur@sola.love>

pkgname="hyprqt6engine"
pkgver=0.1.0
pkgrel=2
pkgdesc="QT6 Theme Provider for Hyprland"
arch=('x86_64' 'aarch64')
url="https://github.com/hyprwm/hyprqt6engine"
license=('BSD-3-Clause')

depends=(
	hyprlang
	hyprutils
	qt6-base
)
makedepends=(
	cmake
	git
	ninja
)

source=("$pkgname-$pkgver.tar.gz::$url/archive/v$pkgver.tar.gz"
	"01-fix-guiprivate-not-found.patch::$url/pull/4.patch")
sha256sums=('e52692168faa51a53e6f05c12114e79ead76787045668c65d41225a13a318f62'
	'8dd8537d255be9ed0e04a96eeaa683b7ca54c93f16e98d5ec83c357b99991e03')

prepare() {
	cd "$pkgname-$pkgver" || return 1
	patch -Np1 -i ../01-fix-guiprivate-not-found.patch
}

build() {
	local cmake_options=(
		-B build
		-S "$pkgname-$pkgver"
		-G Ninja
		-W no-dev
		-D CMAKE_BUILD_TYPE=None
		-D CMAKE_INSTALL_PREFIX=/usr
	)
	cmake "${cmake_options[@]}"
	cmake --build build
}

package() {
	DESTDIR="$pkgdir" cmake --install build
	install -Dm644 "$pkgname-$pkgver/LICENSE" -t "$pkgdir/usr/share/licenses/$pkgname/"
}
