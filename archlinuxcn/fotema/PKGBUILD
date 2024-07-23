# Maintainer: Mark Wagie <mark dot wagie at proton dot me>
pkgname=fotema
pkgver=1.9.5
pkgrel=1
pkgdesc="Photo gallery for Linux"
arch=('x86_64')
url="https://github.com/blissd/fotema"
license=('CC0-1.0 AND CC-BY-2.0 AND CC-BY-4.0 AND CC-BY-NC-SA-4.0 AND CC-BY-SA-4.0 AND GFDL-1.3-or-later AND GPL-3.0-or-later')
depends=(
  'ffmpeg'
  'glycin'
  'libadwaita'
  'libheif'
  'libshumate'
)
makedepends=(
  'cargo'
  'clang'
  'gtk3'
  'meson'
  'mold'
)
source=("$pkgname-$pkgver.tar.gz::$url/archive/refs/tags/v$pkgver.tar.gz"
        'i18n.patch')
sha256sums=('21c8bbc3955f33c36e329fb8d30623e2725eec4084f7067d35c35a742ee37c07'
            'ebe2f2c74ca282a918c748e7e1e08b0e8f3ec964244746c299211df38e7da396')

prepare() {
  cd "$pkgname-$pkgver"
  export CARGO_HOME="$srcdir/cargo-home"
  export RUSTUP_TOOLCHAIN=stable
  cargo fetch --target "$(rustc -vV | sed -n 's/host: //p')"

  # Correct i18n path
  patch -Np1 meson.build <../i18n.patch
}

build() {
  export CARGO_HOME="$srcdir/cargo-home"
  export RUSTUP_TOOLCHAIN=stable
  RUSTFLAGS="-C link-arg=-fuse-ld=mold"
  arch-meson "$pkgname-$pkgver" build
  meson compile -C build
}

check() {
  meson test -C build --print-errorlogs
}

package() {
  meson install -C build --no-rebuild --destdir "$pkgdir"

  cd "$pkgname-$pkgver"
  install -Dm644 LICENSES/* -t "$pkgdir/usr/share/licenses/$pkgname/"
}
