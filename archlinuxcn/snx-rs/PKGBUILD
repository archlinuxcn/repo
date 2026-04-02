# Maintainer: Zdeněk Biberle <zdenek at biberle dot net>
pkgname=snx-rs
pkgver=5.2.4
pkgrel=1
pkgdesc="Rust client for Checkpoint VPN tunnels"
arch=(x86_64)
url=https://github.com/ancwrd1/snx-rs
license=(AGPL-3.0-only)
depends=(gcc-libs glibc openssl glib2 gdk-pixbuf2 gtk4 sqlite webkitgtk-6.0)
makedepends=(cargo imagemagick)
checkdepends=(iproute2)
source=("$pkgname-$pkgver.tar.gz::https://github.com/ancwrd1/$pkgname/archive/refs/tags/v$pkgver.tar.gz")
sha256sums=('d88655f6d9fbae655a62682445f7f4143aafa32ac9ca2a602591ed983982a338')

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
  # At runtime, libappindicator-sys loads either libayatana-appindicator3.so
  # or libappindicator3.so to do its thing. These come from the
  # libayatana-appindicator and libappindicator-gtk3 packages.
  # Either one works, but as libappindicator-gtk3 seems to be on its way
  # out, I've chosen to depend on libayatana-appindicator.
  depends+=(libayatana-appindicator systemd iproute2)
  cd "$pkgname-$pkgver"
  install -Dm0755 -t "$pkgdir/usr/bin/" target/release/{snx-rs,snxctl,snx-rs-gui}
  install -Dm0644 -t "$pkgdir/usr/lib/systemd/system/" package/snx-rs.service
  install -Dm0644 -t "$pkgdir/usr/share/applications/" package/snx-rs-gui.desktop
}
