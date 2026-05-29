# Maintainer: Kimiblock Moe
# Maintainer: JohanChane

pkgname=clashtui
pkgdesc="Mihomo (Clash.Meta) TUI Client"
url="https://github.com/JohanChane/clashtui"
license=("MIT")
arch=("x86_64" "aarch64")
pkgver=0.3.1
pkgrel=1
makedepends=("rust" "git")
depends=("gcc-libs" "glibc" "mihomo")
source=("source::git+https://github.com/JohanChane/clashtui.git#tag=v${pkgver}")
md5sums=('e5faf2caa12fadb30baa1c2a148bf3f9')
provides=("clashtui")
options=(!lto)

function prepare() {
	cd source
	export RUSTUP_TOOLCHAIN=stable
	cargo fetch --target "$CARCH-unknown-linux-gnu"
}

function build() {
	cd source
	export RUSTUP_TOOLCHAIN=stable
	export CARGO_TARGET_DIR=target
	cargo build --release --frozen --all-features --locked
}

function check() {
	cd source
	export RUSTUP_TOOLCHAIN=stable
	cargo test --release --frozen --all-features --locked
}

function package() {
	cd source
	install -Dm755 "target/release/clashtui" "${pkgdir}/usr/bin/clashtui"
	install -Dm644 "LICENSE" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
