# Maintainer: Zdeněk Biberle <zdenek at biberle dot net>
pkgbase=snx-rs
pkgname=(snx-rs-headless snx-rs)
pkgver=6.5.1
pkgrel=1
pkgdesc="Rust client for Checkpoint VPN tunnels"
arch=(x86_64)
url=https://github.com/ancwrd1/snx-rs
license=(AGPL-3.0-only)
makedepends=(cargo gtk4 webkitgtk-6.0)
source=("$pkgbase-$pkgver.tar.gz::https://github.com/ancwrd1/$pkgbase/archive/refs/tags/v$pkgver.tar.gz")
sha256sums=('2a45296fb4fa4f45a15bc5624c8d4ab1265d27c7d6c9e9e373f765d3cb34e37d')

prepare() {
  cd "$pkgbase-$pkgver"
  export RUSTUP_TOOLCHAIN=stable
  cargo fetch --locked --target "$CARCH-unknown-linux-gnu"
}

build() {
  cd "$pkgbase-$pkgver"
  export RUSTUP_TOOLCHAIN=stable
  export CARGO_TARGET_DIR=target
  cargo build --frozen --release --features mobile-access
}

check() {
  cd "$pkgbase-$pkgver"
  export RUSTUP_TOOLCHAIN=stable
  cargo test --frozen --features mobile-access -- --skip platform::linux::tests::test_xfrm_check
}

package_snx-rs-headless() {
  depends=(glibc libgcc openssl sqlite)
  conflicts=("snx-rs<6.0.6-2")
  replaces=("snx-rs<6.0.6-2")

  cd "$pkgbase-$pkgver"
  install -Dm0755 -t "$pkgdir/usr/bin/" target/release/{snx-rs,snxctl}
  install -Dm0644 -t "$pkgdir/usr/lib/systemd/system/" package/snx-rs.service
}

package_snx-rs() {
  depends=(snx-rs-headless fontconfig glib2 glibc gtk4 hicolor-icon-theme libgcc openssl webkitgtk-6.0)

  cd "$pkgbase-$pkgver"
  install -Dm0755 -t "$pkgdir/usr/bin/" target/release/snx-rs-gui
  install -Dm0644 -t "$pkgdir/usr/share/applications/" package/snx-rs-gui.desktop
  install -Dm0644 -t "$pkgdir/usr/share/icons/hicolor/symbolic/apps/" package/icons/snx-rs-*
}
