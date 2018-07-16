# Maintainer: Shreyansh Khajanchi <shreyansh_k@live.com>

_commit=497eb83b4a90c89ed683210524473a2adc84e2cb
pkgname=gnirehtet
pkgver=2.2.1
pkgrel=0
pkgdesc="Gnirehtet provides reverse tethering for Android"
arch=('x86_64')
url="https://github.com/Genymobile/gnirehtet"
license=('Apache-2.0')
depends=('android-tools')
makedepends=('rust')
source=(
	"https://github.com/Genymobile/${pkgname}/archive/${_commit}.tar.gz"
	"https://github.com/Genymobile/${pkgname}/releases/download/v${pkgver}/gnirehtet-rust-linux64-v${pkgver}.zip"
	"patch.diff"
)
sha256sums=(
	'decd9be989777859bb4f315169f5d1007bdf5c9f0bb9d6249b955a698ba3d314'
	'7ecb04bc7e2a223773dc9be66efafd39bb6cfb16b5cc4ccbe252f997c003bf6c'
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
