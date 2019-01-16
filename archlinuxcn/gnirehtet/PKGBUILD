# Maintainer: Shreyansh Khajanchi <shreyansh_k@live.com>

_commit=3104563fb915454565ac9c5cf613d7aca5ca5cb0
pkgname=gnirehtet
pkgver=2.3
pkgrel=0
pkgdesc="Gnirehtet provides reverse tethering for Android"
arch=('x86_64')
url="https://github.com/Genymobile/gnirehtet"
license=('Apache-2.0')
depends=('android-tools')
makedepends=('rust' 'patch')
source=(
	"https://github.com/Genymobile/${pkgname}/archive/${_commit}.tar.gz"
	"https://github.com/Genymobile/${pkgname}/releases/download/v${pkgver}/gnirehtet-rust-linux64-v${pkgver}.zip"
	"patch.diff"
)
sha256sums=(
	'6d2036c617d5e0f746ee43a6a7930712ba05613f1c3f2653665b9dc7d39e7b26'
	'561d77e94d65ecf2d919053e5da6109b8cceb73bffedea71cd4e51304ccaa3d3'
	'SKIP'
)

prepare() {
	cp patch.diff "$srcdir/gnirehtet-${_commit}/relay-rust/src/"
	cd "$srcdir/gnirehtet-${_commit}/relay-rust/src/"
	patch -p0 -i patch.diff
}

build() {
	cd "$srcdir/gnirehtet-${_commit}/relay-rust"
	cargo build --release
}

package() {
	mkdir --parents "$pkgdir/usr/share/gnirehtet"
	cp "$srcdir/gnirehtet-rust-linux64/gnirehtet.apk" "$pkgdir/usr/share/gnirehtet"
	mkdir --parents "$pkgdir/usr/bin"
	cp "$srcdir/gnirehtet-${_commit}/relay-rust/target/release/gnirehtet" "$pkgdir/usr/bin"
}
