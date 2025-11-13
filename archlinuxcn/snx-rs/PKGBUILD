# Maintainer: Zdeněk Biberle <zdenek at biberle dot net>
pkgname=snx-rs
pkgver=4.9.0
pkgrel=1
pkgdesc="Rust client for Checkpoint VPN tunnels"
arch=(x86_64)
url=https://github.com/ancwrd1/snx-rs
license=(AGPL-3.0-only)
depends=(gcc-libs glibc openssl glib2 gdk-pixbuf2 gtk4)
makedepends=(cargo imagemagick)
checkdepends=(iproute2)
source=("$pkgname-$pkgver.tar.gz::https://github.com/ancwrd1/$pkgname/archive/refs/tags/v$pkgver.tar.gz")
sha256sums=('0b16663437f8086ec9f9b957b582a9621bfb6c47bf91dffff6370cabba3ea852')
_icon_sizes=(16 20 22 24 32 36 40 48 64 72 96 128 192 256)

prepare() {
  cd "$pkgname-$pkgver"
  export RUSTUP_TOOLCHAIN=stable
  cargo fetch --locked --target "$CARCH-unknown-linux-gnu"
}

build() {
  cd "$pkgname-$pkgver"
  export RUSTUP_TOOLCHAIN=stable
  export CARGO_TARGET_DIR=target
  cargo build --frozen --release

  # Make sure that the source icon we're using has the expected size
  local source_icon=apps/snx-rs-gui/assets/icons/light/network-vpn.png
  test "$(magick identify -format "%wx%h" "$source_icon")" = 256x256
  # And now resize it to all the other sizes
  for size in "${_icon_sizes[@]}" ; do
    magick "$source_icon" -resize "${size}x$size" "apps/snx-rs-gui/assets/icons/$size.png"
  done
}

check() {
  cd "$pkgname-$pkgver"
  export RUSTUP_TOOLCHAIN=stable
  cargo test --frozen -- --skip platform::linux::tests::test_xfrm_check
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
  for size in "${_icon_sizes[@]}" ; do
    install -Dm0644 -T "apps/snx-rs-gui/assets/icons/$size.png" "$pkgdir/usr/share/icons/hicolor/${size}x$size/apps/snx-rs-gui.png"
  done
}
