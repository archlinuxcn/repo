# Maintainer: Cryolitia <cryolitia at archlinuxcn dot org>>
pkgname=pgp-sig2dot
pkgver=0.4.3
pkgrel=2
pkgdesc="OpenPGP sign party tool —— Visualize the Web of Trust"
arch=('x86_64')
url="https://github.com/cryolitia/pgp-sig2dot"
license=('MIT')
depends=('curl' 'bash' 'bzip2' 'gcc-libs' 'glibc' 'gmp' 'nettle' 'openssl')
makedepends=('cargo' 'clang')
optdepends=('graphviz: for generating visualizations')
source=("pgp-sig2dot-v$pkgver.tar.gz::$url/archive/refs/tags/v$pkgver.tar.gz"
        "pgp-sig2dot-graphviz")
sha256sums=('050c38a7ab10fbdd7e01c8638248ec262d47512e55b69352155a7a78e125badf'
            '75d9e150bba5c48b16ed97c83af9a6df7e12647b2c5df7dc61e51ebf67f1f2f3')

prepare() {
	cd "$srcdir/$pkgname-$pkgver"
	export RUSTUP_TOOLCHAIN=stable
	cargo fetch --locked --target "$CARCH-unknown-linux-gnu"
}

build() {
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
