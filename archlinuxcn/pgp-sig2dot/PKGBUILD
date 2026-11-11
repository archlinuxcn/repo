# Maintainer: Cryolitia <cryolitia at archlinuxcn dot org>>
pkgname=pgp-sig2dot
pkgver=0.4.4
pkgrel=3
pkgdesc="OpenPGP sign party tool —— Visualize the Web of Trust"
arch=('x86_64')
url="https://github.com/cryolitia/pgp-sig2dot"
license=('MIT')
depends=('curl' 'bash' 'libgcc' 'glibc' 'gmp' 'nettle3')
makedepends=('cargo' 'clang')
optdepends=('graphviz: for generating visualizations')
source=("pgp-sig2dot-v$pkgver.tar.gz::$url/archive/refs/tags/v$pkgver.tar.gz"
        "pgp-sig2dot-graphviz")
sha256sums=('a5c120ba717a9029614c4c55f2b88c2ab6d148061d471e0eab7264a20174c8ce'
            '75d9e150bba5c48b16ed97c83af9a6df7e12647b2c5df7dc61e51ebf67f1f2f3')
options=('!lto')

prepare() {
	cd "$srcdir/$pkgname-$pkgver"
	export RUSTUP_TOOLCHAIN=stable
	cargo fetch --locked --target "$CARCH-unknown-linux-gnu"
}

build() {
	# Compatibility with Arch Linux's Nettle3 library
	export PKG_CONFIG_PATH="/usr/lib/nettle3/pkgconfig${PKG_CONFIG_PATH:+:$PKG_CONFIG_PATH}"
	export RUSTFLAGS="-L native=/usr/lib/nettle3${RUSTFLAGS:+ $RUSTFLAGS}"
	
	cd "$srcdir/$pkgname-$pkgver"
	export RUSTUP_TOOLCHAIN=stable
	export CARGO_TARGET_DIR=target

	cargo build --frozen --release --features map42
}

package() {
	cd "$srcdir/$pkgname-$pkgver"
	install -Dm0755 -t "$pkgdir/usr/bin/" "target/release/pgp-sig2dot"

	install -Dm644 <("$pkgdir"/usr/bin/pgp-sig2dot cli complete bash) "$pkgdir/usr/share/bash-completion/completions/pgp-sig2dot"
	install -Dm644 <("$pkgdir"/usr/bin/pgp-sig2dot cli complete zsh) "$pkgdir/usr/share/zsh/site-functions/_pgp-sig2dot"
    install -Dm644 <("$pkgdir"/usr/bin/pgp-sig2dot cli complete fish) "$pkgdir/usr/share/fish/vendor_completions.d/pgp-sig2dot.fish"
    
	mkdir -p "$pkgdir/usr/share/man/man1"
	"$pkgdir/usr/bin/pgp-sig2dot" cli manpage --path "$pkgdir/usr/share/man/man1"

    install -Dm755 -t "$pkgdir/usr/bin/" "$srcdir/pgp-sig2dot-graphviz"
    install -Dm644 "$srcdir/$pkgname-$pkgver/LICENSE" -t "$pkgdir/usr/share/licenses/$pkgname"
}
