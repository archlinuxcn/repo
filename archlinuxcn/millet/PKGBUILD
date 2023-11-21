# Maintainer: Cooper Pierce <cppierce@andrew.cmu.edu>
pkgname=millet
pkgver=0.12.6
pkgrel=1
pkgdesc="Language server implementation for Standard ML"
url="https://github.com/azdavis/millet"
arch=('x86_64')
license=(APACHE MIT)
makedepends=('cargo')
source=("$pkgname-$pkgver.tgz::${url}/archive/refs/tags/v${pkgver}.tar.gz")
md5sums=('bab4f5c68f781eeaa7a94a4ce593501d')

build() {
    cd "$pkgname-$pkgver"
    # Doesn't use xtask to avoid building the VSCode extension
    cargo build --release --locked
}

package() {
    cd "$pkgname-$pkgver"
    install -Dm755 "target/release/millet-ls" "$pkgdir/usr/bin/millet"
    install -Dm644 "LICENSE-MIT.md" "$pkgdir/usr/share/licenses/${pkgname}/LICENSE-MIT"
}

check() {
    cd "$pkgname-$pkgver"

    # Doesn't use xtask because some checks require we're in a git repo (rely
    # on git grep), and this also requires the installer to have xtask
    # installed.
    cargo fmt -- --check
    cargo clippy
    # Ignores tests starting with repo. These tests assume we're in a git repo
    # (we're not, here, since this is a source tarball), and test for things
    # like changelog entries existing.
    cargo test --locked -- --skip repo
}
