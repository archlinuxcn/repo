# Maintainer: KokaKiwi <kokakiwi+aur [at] kokakiwi dot com>
# Contributor: Mike Yuan <me@yhndnzj.com>

pkgname=ast-grep
pkgver=0.22.5
pkgrel=1
pkgdesc='A fast and polyglot tool for code structural search, lint, rewriting at large scale'
arch=('x86_64')
url='https://ast-grep.github.io/'
license=('MIT')
depends=('gcc-libs')
makedepends=('cargo')
checkdepends=('python')
source=("$pkgname-$pkgver.tar.gz::https://github.com/ast-grep/ast-grep/archive/$pkgver.tar.gz")
sha256sums=('7e0eda7879a045277faf524e0d8f37905e9c05e2b2013893809e136378a24e9c')
b2sums=('e9af951b8d66bd6c3194c194f60245304b4b767c0645d2d74d55a31596f34ad3e91ed20ac16262724cc2251f8746543167e8b47c2e29194b15331e7a16446806')
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
