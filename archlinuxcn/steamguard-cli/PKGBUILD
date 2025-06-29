# Maintainer: Thorben Günther <echo YWRtaW5AeGVucm94Lm5ldAo= | base64 -d>

pkgname=steamguard-cli
_pkgname=steamguard
pkgver=0.17.1
pkgrel=1
pkgdesc="A linux utility for generating 2FA codes for Steam and managing Steam trade confirmations."
arch=('x86_64')
url='https://github.com/dyc3/steamguard-cli'
license=('GPL3')
makedepends=('cargo')
source=("$pkgname-$pkgver.tar.gz::https://github.com/dyc3/$pkgname/archive/refs/tags/v$pkgver.tar.gz")
sha256sums=('dc02e2a40c5bfc8f28195c99a9575ef10c1fe67f3075d402091e81f53440626d')
options=(!lto)

prepare() {
    cd "$srcdir/$pkgname-$pkgver"
    cargo fetch --locked --target "$CARCH-unknown-linux-gnu"
}

build() {
    cd "$srcdir/$pkgname-$pkgver"
    export RUSTUP_TOOLCHAIN=stable
    export CARGO_TARGET_DIR=target
    cargo build --frozen --release --all-features

    # completion
    "target/release/$_pkgname" completion --shell bash >"$srcdir/$pkgname-$pkgver/$pkgname"
    "target/release/$_pkgname" completion --shell zsh >"$srcdir/$pkgname-$pkgver/_$_pkgname"
}

check() {
    cd "$srcdir/$pkgname-$pkgver"
    export RUSTUP_TOOLCHAIN=stable
    cargo test --frozen --all-features
}

package() {
    cd "$srcdir/$pkgname-$pkgver"
    # NOTE: Install as steamguard, otherwise completions won't work
    install -Dm0755 "target/release/$_pkgname" "$pkgdir/usr/bin/$_pkgname"
    install -Dm0644 "$pkgname" "$pkgdir/usr/share/bash-completion/completions/$_pkgname"
    install -Dm0644 -t "$pkgdir/usr/share/zsh/site-functions/" "_$_pkgname"
}
