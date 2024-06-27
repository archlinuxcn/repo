# Maintainer: KokaKiwi <kokakiwi+aur [at] kokakiwi dot com>
# Contributor: Mike Yuan <me@yhndnzj.com>

pkgname=ast-grep
pkgver=0.24.1
pkgrel=1
pkgdesc='A fast and polyglot tool for code structural search, lint, rewriting at large scale'
arch=('x86_64')
url='https://ast-grep.github.io/'
license=('MIT')
depends=('gcc-libs')
makedepends=('cargo')
checkdepends=('python')
source=("$pkgname-$pkgver.tar.gz::https://github.com/ast-grep/ast-grep/archive/$pkgver.tar.gz")
sha256sums=('51c4c8823de87f8069e122500c185c51b97828a98ce01e7a3a16949e9c676eae')
b2sums=('9d4db05a9faf9ce151038a420042187f907ea87eff800bd04edd265c4d13e787f2590cbae9cc289de599dea377763d16025325170d930340191f6366a2770fcc')
options=('!lto')

export RUSTUP_TOOLCHAIN=${RUSTUP_TOOLCHAIN:-stable}

prepare() {
    cd "$pkgname-$pkgver"

    cargo fetch --locked --target "$CARCH-unknown-linux-gnu"
}

build() {
    cd "$pkgname-$pkgver"

    CARGO_TARGET_DIR=target \
    cargo build --frozen --release --all-features --package ast-grep
}

check() {
    cd "$pkgname-$pkgver"

    RUSTFLAGS="$RUSTFLAGS -C debug-assertions" cargo test --frozen --all-features
}

package() {
    cd "$pkgname-$pkgver"

    install -Dm0755 -t "$pkgdir/usr/bin" \
        target/release/ast-grep
    ln -sf ast-grep "$pkgdir/usr/bin/asg"

    install -Dm0644 -t "$pkgdir/usr/share/licenses/$pkgname" \
        LICENSE
}
