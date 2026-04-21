# Maintainer: Zdeněk Biberle <zdenek at biberle dot net>
pkgname=snx-rs
pkgver=6.0.0
pkgrel=1
pkgdesc="Rust client for Checkpoint VPN tunnels"
arch=(x86_64)
url=https://github.com/ancwrd1/snx-rs
license=(AGPL-3.0-only)
depends=(fontconfig glib2 glibc gtk4 libgcc openssl sqlite webkitgtk-6.0)
makedepends=(cargo)
source=("$pkgname-$pkgver.tar.gz::https://github.com/ancwrd1/$pkgname/archive/refs/tags/v$pkgver.tar.gz")
sha256sums=('87e6d024c2862f3501e142d775eef41f19c9e9296ba8e994e19fcad9ae2fbeaf')

prepare() {
  cd "$pkgname-$pkgver"
  export RUSTUP_TOOLCHAIN=stable
  cargo fetch --locked --target "$CARCH-unknown-linux-gnu"
}

build() {
  cd "$pkgname-$pkgver"
  export RUSTUP_TOOLCHAIN=stable
  export CARGO_TARGET_DIR=target
  cargo build --frozen --release --features mobile-access
}

check() {
  cd "$pkgname-$pkgver"
  export RUSTUP_TOOLCHAIN=stable
  cargo test --frozen --features mobile-access -- --skip platform::linux::tests::test_xfrm_check
}

package() {
  cd "$pkgname-$pkgver"
  install -Dm0755 -t "$pkgdir/usr/bin/" target/release/{snx-rs,snxctl,snx-rs-gui}
  install -Dm0644 -t "$pkgdir/usr/lib/systemd/system/" package/snx-rs.service
  install -Dm0644 -t "$pkgdir/usr/share/applications/" package/snx-rs-gui.desktop
}
