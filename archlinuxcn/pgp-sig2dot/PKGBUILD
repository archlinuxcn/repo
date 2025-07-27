# Maintainer: Cryolitia <cryolitia at archlinuxcn dot org>>
pkgname=pgp-sig2dot
pkgver=0.2.0
pkgrel=1
pkgdesc="OpenPGP sign party tool —— Visualize the Web of Trust"
arch=('x86_64')
url="https://github.com/cryolitia/pgp-sig2dot"
license=('MIT')
depends=('curl' 'bash' 'bzip2' 'gcc-libs' 'glibc' 'gmp' 'nettle' 'sqlite' 'openssl' 'graphviz')
makedepends=('cargo' 'clang')
source=("$url/archive/refs/tags/v$pkgver.tar.gz"
        "pgp-sig2dot-graphviz")
sha256sums=('37df21df9fa4a89f6146e55ffc8684048c034bed3b8abab53d9f4a8a27840f38'
            'SKIP')

prepare() {
	cd "$srcdir/$pkgname-$pkgver/rust-part"
	export RUSTUP_TOOLCHAIN=stable
	cargo fetch --locked --target "$CARCH-unknown-linux-gnu"
}

build() {
	cd "$srcdir/$pkgname-$pkgver/rust-part"
	export RUSTUP_TOOLCHAIN=stable
	export CARGO_TARGET_DIR=target

	cargo build --frozen --release
}

package() {
	cd "$srcdir/$pkgname-$pkgver/rust-part"
	install -Dm0755 -t "$pkgdir/usr/bin/" "target/release/pgp-sig2dot"

	install -Dm644 <("$pkgdir"/usr/bin/pgp-sig2dot gen complete bash) "$pkgdir/usr/share/bash-completion/completions/pgp-sig2dot"
	install -Dm644 <("$pkgdir"/usr/bin/pgp-sig2dot gen complete zsh) "$pkgdir/usr/share/zsh/site-functions/_pgp-sig2dot"
    install -Dm644 <("$pkgdir"/usr/bin/pgp-sig2dot gen complete fish) "$pkgdir/usr/share/fish/vendor_completions.d/pgp-sig2dot.fish"
    
	mkdir -p "$pkgdir/usr/share/man/man1"
	"$pkgdir/usr/bin/pgp-sig2dot" gen man --path "$pkgdir/usr/share/man/man1"

    install -Dm755 -t "$pkgdir/usr/bin/" "$srcdir/pgp-sig2dot-graphviz"
    install -Dm644 "$srcdir/$pkgname-$pkgver/LICENSE" -t "$pkgdir/usr/share/licenses/$pkgname"
}
