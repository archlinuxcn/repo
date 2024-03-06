# Maintainer: Carl Smedstad <carl.smedstad at protonmail dot com>

pkgname=satty
_pkgname=Satty
pkgver=0.11.2
pkgrel=1
pkgdesc="A Screenshot Annotation Tool inspired by Swappy and Flameshot"
url="https://github.com/gabm/satty"
arch=(x86_64)
license=(MPL-2.0)
depends=(
  cairo
  gcc-libs
  gdk-pixbuf2
  glib2
  glibc
  gtk4
  hicolor-icon-theme
  libadwaita
  pango
)
makedepends=(cargo)
source=("$pkgname-$pkgver.tar.gz::$url/archive/v$pkgver.tar.gz")
sha256sums=('9d906eedce48663718ce428bb2a74e9cfeb49378c51af443f76bf483cf109ad2')

_archive="$_pkgname-$pkgver"

prepare() {
  cd "$_archive"

  export RUSTUP_TOOLCHAIN=stable
  cargo fetch --locked --target "$(rustc -vV | sed -n 's/host: //p')"
}

build() {
  cd "$_archive"

  export RUSTUP_TOOLCHAIN=stable
  export CARGO_TARGET_DIR=target
  cargo build --frozen --release --all-features
}

package() {
  cd "$_archive"

  install -Dm755 -t "$pkgdir/usr/bin" target/release/satty

  install -Dm644 completions/_satty \
    "$pkgdir/usr/share/zsh/site-functions/_satty"
  install -Dm644 completions/satty.bash \
    "$pkgdir/usr/share/bash-completion/completions/satty"
  install -Dm644 completions/satty.fish \
    "$pkgdir/usr/share/fish/vendor_completions.d/satty.fish"
  install -Dm644 completions/satty.nu \
    "$pkgdir/usr/share/nushell/completions/satty.nu"
  install -Dm644 completions/satty.elv \
    "$pkgdir/usr/share/elvish/lib/satty.elv"

  install -Dm644 -t "$pkgdir/usr/share/applications" satty.desktop
  install -Dm644 -t "$pkgdir/usr/share/icons/hicolor/scalable/apps" assets/satty.svg

  install -Dm644 -t "$pkgdir/usr/share/doc/$pkgname" README.md
  cp -a -t "$pkgdir/usr/share/doc/$pkgname" assets
}
