# Maintainer: KokaKiwi <kokakiwi+aur [at] kokakiwi dot com>
# Contributor: Mike Yuan <me@yhndnzj.com>

pkgname=ast-grep
pkgver=0.22.6
pkgrel=1
pkgdesc='A fast and polyglot tool for code structural search, lint, rewriting at large scale'
arch=('x86_64')
url='https://ast-grep.github.io/'
license=('MIT')
depends=('gcc-libs')
makedepends=('cargo')
checkdepends=('python')
source=("$pkgname-$pkgver.tar.gz::https://github.com/ast-grep/ast-grep/archive/$pkgver.tar.gz")
sha256sums=('d7b247c6f868c4df3cf9563092480cd863e94fc633471b621ad89784b83aaf89')
b2sums=('66c30111ee5b53524ffc4ceabc74b58717f150dbafa7a6eca562f8e2c1f186a87a30bd070e26369ba10e1b68013334556d87e2944c5f20b700fee543c4eadc33')
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
