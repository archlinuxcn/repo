# Maintainer: Horror Proton <107091537+horror-proton@users.noreply.github.com>
pkgname=maa-cli
pkgver=0.7.7
pkgrel=2
pkgdesc="A simple CLI for MAA by Rust."
arch=('x86_64' 'aarch64')
url="https://github.com/MaaAssistantArknights/maa-cli"
license=('AGPL-3.0-only')
depends=('gcc-libs' 'libgit2' 'openssl' 'zip')
makedepends=('cargo' 'git')
optdepends=(
  'maa-assistant-arknights: for preinstalled maa core'
  'git: alternative git backend'
)
source=("$url/archive/refs/tags/v${pkgver}.tar.gz")
md5sums=('37bb15f5b0eaf018bebcbb6e9172d726')
sha256sums=('c1a0a6ff6fd83c2aa8a6c66cc6b6afe9d877c6eecb9004905172ae0741b698eb')
options=(!lto)

prepare() {
	cd "$srcdir/maa-cli-$pkgver"
	export RUSTUP_TOOLCHAIN=stable
	cargo fetch --locked --target "$CARCH-unknown-linux-gnu"
}

build() {
	cd "$srcdir/maa-cli-$pkgver"
	export RUSTUP_TOOLCHAIN=stable
	export CARGO_TARGET_DIR=target

	export MAA_EXTRA_SHARE_NAME=maa-assistant-arknights
	cargo build --frozen --release --no-default-features --features=core_installer,git2
}

check() {
	cd "$srcdir/maa-cli-$pkgver"
	export RUSTUP_TOOLCHAIN=stable
	cargo test --frozen --all-features
}

package() {
	cd "$srcdir/maa-cli-$pkgver"
	install -Dm0755 -t "$pkgdir/usr/bin/" "target/release/maa"
	mkdir -p "$pkgdir/usr/share"
	# ln -s maa-assistant-arknights "$pkgdir/usr/share/maa"

	install -Dm644 <("$pkgdir"/usr/bin/maa complete bash) "$pkgdir/usr/share/bash-completion/completions/maa"
	install -Dm644 <("$pkgdir"/usr/bin/maa complete zsh) "$pkgdir/usr/share/zsh/site-functions/_maa"
	install -Dm644 <("$pkgdir"/usr/bin/maa complete fish) "$pkgdir/usr/share/fish/vendor_completions.d/maa.fish"

	mkdir -p "$pkgdir/usr/share/man/man1"
	"$pkgdir/usr/bin/maa" mangen --path "$pkgdir/usr/share/man/man1"
}
