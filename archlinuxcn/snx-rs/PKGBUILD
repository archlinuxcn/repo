# Maintainer: Zdeněk Biberle <zdenek at biberle dot net>
pkgname=snx-rs
pkgver=4.7.0
pkgrel=1
pkgdesc="Rust client for Checkpoint VPN tunnels"
arch=(x86_64)
url=https://github.com/ancwrd1/snx-rs
license=(AGPL-3.0-only)
depends=(gcc-libs glibc openssl glib2 gdk-pixbuf2 gtk4)
makedepends=(cargo imagemagick)
checkdepends=(iproute2)
source=(
  "$pkgname-$pkgver.tar.gz::https://github.com/ancwrd1/$pkgname/archive/refs/tags/v$pkgver.tar.gz"
  fix-executable-path.patch
  fix-desktop-file.patch
)
sha256sums=('c1d12654669fbc306d84b26ddc57e2a616f8c3e2346bb89ff6238e342101273f'
            'fdd298a90c9890c29bc016596a57c6055ded0c672e51a77a47c7f738c2673d11'
            '0609b65d09e1120f1f6038d3b2bfa6ba86e801a807a452c57dec640fa2fced04')
_icon_sizes=(16 20 22 24 32 36 40 48 64 72 96 128 192 256)

prepare() {
  cd "$pkgname-$pkgver"
  patch --forward --strip=1 --input="$srcdir/fix-executable-path.patch"
  patch --forward --strip=1 --input="$srcdir/fix-desktop-file.patch"
  export RUSTUP_TOOLCHAIN=stable
  cargo fetch --locked --target "$CARCH-unknown-linux-gnu"
}

build() {
  cd "$pkgname-$pkgver"
  export RUSTUP_TOOLCHAIN=stable
  export CARGO_TARGET_DIR=target
  cargo build --frozen --release

  # Make sure that the source icon we're using has the expected size
  local source_icon=assets/icons/light/network-vpn.png
  test "$(magick identify -format "%wx%h" "$source_icon")" = 256x256
  # And now resize it to all the other sizes
  for size in "${_icon_sizes[@]}" ; do
    magick "$source_icon" -resize "${size}x$size" "assets/icons/$size.png"
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
  install -Dm0644 -t "$pkgdir/usr/lib/systemd/system/" assets/snx-rs.service
  install -Dm0644 -t "$pkgdir/usr/share/applications/" assets/snx-rs-gui.desktop
  for size in "${_icon_sizes[@]}" ; do
    install -Dm0644 -T "assets/icons/$size.png" "$pkgdir/usr/share/icons/hicolor/${size}x$size/apps/snx-rs-gui.png"
  done
}
