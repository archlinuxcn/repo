# Maintainer: Xeonacid <h.dwwwwww@gmail.com>
# Contributor: Oliver Nordbjerg <hi@notbjerg.me>

pkgname=foundry
pkgver=1.3.2
pkgrel=1
pkgdesc="A blazing fast, portable and modular toolkit for Ethereum application development written in Rust."
arch=(x86_64)
url="https://getfoundry.sh"
license=(MIT Apache-2.0)
depends=(bzip2 gcc-libs glibc libusb)
makedepends=(git cargo)
provides=(forge cast anvil chisel)
source=("git+https://github.com/foundry-rs/foundry.git#tag=v$pkgver")
sha256sums=('cdfdb59a1729a3a1a4d2ac89e6fb5e4922fba3322809cff2f9e11d01ede2d4e0')
options=(!lto)

prepare() {
    cd $pkgname
    export RUSTUP_TOOLCHAIN=stable
    cargo fetch --locked --target "$(rustc -vV | sed -n 's/host: //p')"
}

build() {
    cd $pkgname
    export RUSTUP_TOOLCHAIN=stable
    export CARGO_TARGET_DIR=target
    cargo build --frozen --release --bin anvil --bin cast --bin chisel --bin forge
}

package() {
    cd $pkgname
    install -Dm755 target/release/{anvil,cast,chisel,forge} -t $pkgdir/usr/bin
    install -Dm644 LICENSE-MIT LICENSE-APACHE -t "$pkgdir/usr/share/licenses/$pkgname"
}
