# Maintainer: Xeonacid <h.dwwwwww@gmail.com>

pkgname=anchor
pkgver=0.31.0
pkgrel=1
pkgdesc='⚓ Solana Sealevel Framework'
arch=(x86_64)
url='https://www.anchor-lang.com'
license=(Apache-2.0)
depends=(cargo gcc-libs glibc nodejs yarn)
makedepends=(git)
source=("git+https://github.com/coral-xyz/$pkgname.git#tag=v$pkgver")
sha256sums=('1c0b2fb558cf074f1166a48b50cced26d307cf4dff9a7446fc32cb9d2a4a233d')
options=(!lto)

prepare() {
    cd $pkgname
    export RUSTUP_TOOLCHAIN=stable
    # Fix `time` compile error
    cargo update -p time
    cargo fetch --locked --target "$(rustc -vV | sed -n 's/host: //p')"
}

build() {
    cd $pkgname
    export RUSTUP_TOOLCHAIN=stable
    export CARGO_TARGET_DIR=target
    cargo build --frozen --release -p $pkgname-cli
}

check() {
    cd $pkgname
    export RUSTUP_TOOLCHAIN=stable
    cargo test --frozen -p $pkgname-cli
}

package() {
    cd $pkgname
    install -Dm0755 -t "$pkgdir/usr/bin/" "target/release/$pkgname"
    install -Dm644 LICENSE -t "$pkgdir/usr/share/licenses/$pkgname"
    install -Dm644 README.md -t "$pkgdir/usr/share/doc/$pkgname"
}
