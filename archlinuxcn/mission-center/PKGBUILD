# Maintainer: Mark Wagie <mark dot wagie at proton dot me>
pkgname=mission-center
pkgver=0.3.3
pkgrel=1
pkgdesc="Monitor your CPU, Memory, Disk, Network and GPU usage"
arch=('x86_64')
url="https://gitlab.com/mission-center-devs/mission-center"
license=('GPL3')
depends=('dmidecode' 'libadwaita' 'nvtop')
makedepends=('blueprint-compiler' 'cargo' 'meson')
checkdepends=('appstream-glib')
options=('!lto')
source=("$url/-/archive/v$pkgver/$pkgname-v$pkgver.tar.gz")
sha256sums=('e0c54fffc8b588e906ea8aa6976af0c435879bb3db6d3e2c4e0aeb13c7fbd753')

prepare() {
  cd "$pkgname-v$pkgver"
  export CARGO_HOME="$srcdir/cargo-home"
  export RUSTUP_TOOLCHAIN=stable
  cargo fetch --target "$CARCH-unknown-linux-gnu"
}

build() {
  export CARGO_HOME="$srcdir/cargo-home"
  export RUSTUP_TOOLCHAIN=stable
  arch-meson "$pkgname-v$pkgver" build
  meson compile -C build
}

check() {
  meson test -C build --print-errorlogs || :
}

package() {
  meson install -C build --no-rebuild --destdir "$pkgdir"
}
