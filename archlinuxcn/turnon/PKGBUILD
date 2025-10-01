# Maintainer: Kimiblock Moe

pkgname=turnon
pkgdesc="Turn on devices in your local network"
url="https://codeberg.org/swsnr/turnon"
license=("EUPL-1.2")
arch=("x86_64" "aarch64")
pkgver=2.9.3
pkgrel=1
makedepends=("rust" "cargo" "git" "blueprint-compiler" "just")
depends=(libadwaita gtk4 hicolor-icon-theme graphene dconf gcc-libs glib2 glibc)
source=("git+https://codeberg.org/swsnr/turnon.git#tag=v${pkgver}")
md5sums=('0bf1f23969644cb815fe7b58dfb0f262')

function prepare() {
	cd "${srcdir}/turnon"
	export RUSTUP_TOOLCHAIN=stable
	cargo fetch --target "$CARCH-unknown-linux-gnu"
	#sed -i 's|@# Compile settings schemas after installation||g' justfile
	#sed -i 's|glib-compile-schemas --strict '{{DESTPREFIX}}/share/glib-2.0/schemas'||g' justfile
}

function build() {
	cd "${srcdir}/turnon"
	export RUSTUP_TOOLCHAIN=stable
	export CARGO_TARGET_DIR=target
	just APPID=de.swsnr.turnon compile
	env cargo build --release --locked
#	env make msgfmt
}

function check() {
	cd "${srcdir}/turnon"
	export RUSTUP_TOOLCHAIN=stable
	env cargo test --frozen --all-features
}

function package() {
	cd "${srcdir}/turnon"
	#make DESTPREFIX="${pkgdir}/usr" install
	just APPID=de.swsnr.turnon DESTPREFIX="$pkgdir/usr" install
	install -Dm644 LICENSE -t "$pkgdir/usr/share/licenses/$pkgname/"
	ln -s "/usr/bin/${_app_id}" "$pkgdir/usr/bin/$pkgname"
	rm "${pkgdir}/usr/share/glib-2.0/schemas/gschemas.compiled"
}



