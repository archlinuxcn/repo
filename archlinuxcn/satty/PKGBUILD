# Maintainer: Carl Smedstad <carsme@archlinux.org>

pkgname=satty
_pkgname=Satty
pkgver=0.14.0
pkgrel=1
pkgdesc="A Screenshot Annotation Tool inspired by Swappy and Flameshot"
url="https://github.com/gabm/satty"
arch=(x86_64)
license=(MPL-2.0)
depends=(
  cairo
  fontconfig
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
sha256sums=('3118784377da9254fbccf5fe85b7622aa6ed0054a4c9d977bc72ac817e2c1f96')

prepare() {
  cd $_pkgname-$pkgver

  export RUSTUP_TOOLCHAIN=stable
  cargo fetch --locked --target "$(rustc -vV | sed -n 's/host: //p')"
}

build() {
  cd $_pkgname-$pkgver

  export RUSTUP_TOOLCHAIN=stable
  export CARGO_TARGET_DIR=target
  cargo build --frozen --release --all-features
}

package() {
  cd $_pkgname-$pkgver

  install -vDm755 -t "$pkgdir/usr/bin" target/release/satty

  install -vDm644 completions/_satty \
    "$pkgdir/usr/share/zsh/site-functions/_satty"
  install -vDm644 completions/satty.bash \
    "$pkgdir/usr/share/bash-completion/completions/satty"
  install -vDm644 completions/satty.fish \
    "$pkgdir/usr/share/fish/vendor_completions.d/satty.fish"
  install -vDm644 completions/satty.nu \
    "$pkgdir/usr/share/nushell/completions/satty.nu"
  install -vDm644 completions/satty.elv \
    "$pkgdir/usr/share/elvish/lib/satty.elv"

  install -vDm644 -t "$pkgdir/usr/share/applications" satty.desktop
  install -vDm644 -t "$pkgdir/usr/share/icons/hicolor/scalable/apps" assets/satty.svg

  install -vDm644 -t "$pkgdir/usr/share/doc/$pkgname" README.md
  cp -va -t "$pkgdir/usr/share/doc/$pkgname" assets
}
