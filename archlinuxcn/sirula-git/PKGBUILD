# Maintainer: Carlo Abelli <carlo@abelli.me>

pkgname=sirula-git
_pkgname=sirula
pkgver=r59.bf216d7
pkgrel=2
pkgdesc='An app launcher for wayland'
url='https://github.com/DorianRudolph/sirula'
arch=('x86_64')
license=('GPL3')
provides=('sirula')
conflicts=('sirula')
makedepends=('cargo' 'git')
depends=('gtk-layer-shell')
source=("$_pkgname::git+https://github.com/DorianRudolph/sirula.git")
sha256sums=('SKIP')

pkgver() {
  cd "$_pkgname"

  printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
}

prepare() {
  cd "$_pkgname"

  export RUSTUP_TOOLCHAIN=stable
  cargo fetch --locked --target "$CARCH-unknown-linux-gnu"
}

build() {
  cd "$_pkgname"

  export RUSTUP_TOOLCHAIN=stable
  export CARGO_TARGET_DIR=target
  cargo build --frozen --release --all-features
}

package() {
  cd "$_pkgname"

  install -Dm755 -t "$pkgdir/usr/bin" "target/release/$_pkgname"
}
