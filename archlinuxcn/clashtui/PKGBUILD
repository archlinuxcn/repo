# Maintainer: Kimiblock Moe
# Maintainer: JohanChane

pkgname=clashtui
pkgdesc="Mihomo (Clash.Meta) TUI Client"
url="https://github.com/JohanChane/clashtui"
license=("MIT")
arch=("any")
pkgver=0.2.3
pkgrel=1
makedepends=("rust" "cargo" "git")
depends=("gcc-libs" "glibc")
source=("git+https://github.com/JohanChane/clashtui.git#tag=v${pkgver}")
md5sums=("SKIP")
provides=("clashtui")
options=(!lto)

function prepare() {
	cd "${srcdir}/clashtui/clashtui"
	export RUSTUP_TOOLCHAIN=stable
	cargo fetch --target "$CARCH-unknown-linux-gnu"
}

function build() {
	cd "${srcdir}/clashtui/clashtui"
	export RUSTUP_TOOLCHAIN=stable
	export CARGO_TARGET_DIR=target
	cargo build --release --frozen --all-features --locked
}

function check() {
	cd "${srcdir}/clashtui/clashtui"
	export RUSTUP_TOOLCHAIN=stable
	cargo test --release --frozen --all-features --locked
}

function package() {
	install -Dm755 "${srcdir}/clashtui/clashtui/target/release/clashtui" "${pkgdir}/usr/bin/clashtui"
	install -Dm644 "${srcdir}/clashtui/LICENSE" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
