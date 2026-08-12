# Maintainer: lhl <lhl@randomfoo.net>

pkgname=amdtop
pkgver=0.2.6
pkgrel=1
pkgdesc='A btop/nvitop-style system monitor for AMD GPUs, CPUs, and XDNA NPUs'
arch=('x86_64')
url='https://github.com/lhl/amdtop'
license=('Apache-2.0')
depends=('glibc' 'libdrm' 'libgcc')
makedepends=('cargo')
source=(
  "$pkgname-$pkgver.tar.gz::https://static.crates.io/crates/$pkgname/$pkgname-$pkgver.crate"
)
b2sums=('7f90eda512442d2c1f5848fd72045fc702dda3fa96c8e89f3d2dd4af87370e474c61f0f32eca3d33f67ad622526713806de4147061592f01ea338fb3c4b5219c')

prepare() {
  cd "$pkgname-$pkgver"
  export RUSTUP_TOOLCHAIN=stable
  cargo fetch --locked --target "$CARCH-unknown-linux-gnu"
}

build() {
  cd "$pkgname-$pkgver"
  export RUSTUP_TOOLCHAIN=stable
  export CARGO_TARGET_DIR=target
  cargo build --frozen --release --all-features
}

check() {
  cd "$pkgname-$pkgver"
  export RUSTUP_TOOLCHAIN=stable
  export CARGO_TARGET_DIR=target
  cargo test --frozen --all-targets --all-features
}

package() {
  cd "$pkgname-$pkgver"
  install -Dm0755 "target/release/$pkgname" "$pkgdir/usr/bin/$pkgname"
  install -Dm0644 LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
  install -Dm0644 NOTICE "$pkgdir/usr/share/licenses/$pkgname/NOTICE"
  install -Dm0644 THIRD_PARTY.md "$pkgdir/usr/share/licenses/$pkgname/THIRD_PARTY.md"
}
