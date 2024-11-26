# Maintainer: KokaKiwi <kokakiwi+aur [at] kokakiwi dot com>
# Contributor: Mike Yuan <me@yhndnzj.com>

pkgname=ast-grep
pkgver=0.30.1
pkgrel=1
pkgdesc='A fast and polyglot tool for code structural search, lint, rewriting at large scale'
arch=('x86_64')
url='https://ast-grep.github.io/'
license=('MIT')
depends=('gcc-libs')
makedepends=('cargo')
checkdepends=('python')
source=("$pkgname-$pkgver.tar.gz::https://github.com/ast-grep/ast-grep/archive/$pkgver.tar.gz")
sha256sums=('c24654868d99a7e6b2db7ee13e88d46ac5206a0f3cab1bd7cd1d8ce4a274c990')
b2sums=('245d9ed4d47b5a29153beabc0624ef62261376d694016faf151008f83722ad779d68b03b195c5e04f8e58f3b35e5d28b5547a4554601bb3d3ddc695ba32e9d87')
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
