# Maintainer: CupricReki
# Maintainer: feschber

pkgname=lan-mouse-git
_pkgname=lan-mouse
pkgver=0.10.0.r42.ge46fe60b3e
pkgrel=1
pkgdesc="Software KVM Switch / mouse & keyboard sharing software for Local Area Networks"
url="https://github.com/feschber/lan-mouse"
license=("GPL-3.0-only")
arch=(any)
provides=("$_pkgname=${pkgver/\.r*/}")
conflicts=("$_pkgname")
source=("$_pkgname"::"git+https://github.com/ferdinandschober/$_pkgname.git")
sha256sums=('SKIP')
depends=(libadwaita gtk4 libx11 libxtst glib2 glibc gcc-libs hicolor-icon-theme)
makedepends=(git cargo rust desktop-file-utils)
options=('!lto')

pkgver() {
  cd "$_pkgname"
  git describe --abbrev=10 --long --tags --match 'v*' | sed 's/^v//;s/\([^-]*-g\)/r\1/;s/-/./g'
}

prepare() {
  cd "$_pkgname"
  cargo fetch --locked --target "$CARCH-unknown-linux-gnu"
}

build() {
  cd "$_pkgname"
  export RUSTUP_TOOLCHAIN=stable
  export CARGO_TARGET_DIR=target
  cargo build --frozen --release --all-features
}

check() {
  cd "$_pkgname"
  export RUSTUP_TOOLCHAIN=stable
  cargo test --frozen --all-features
}

package() {
  cd "$_pkgname"

  desktop-file-install -m 644 --dir "$pkgdir/usr/share/applications/" "de.feschber.LanMouse.desktop"

  install -Dm0644 -t "$pkgdir/usr/share/icons/hicolor/scalable/apps" "lan-mouse-gtk/resources/de.feschber.LanMouse.svg"
  install -Dm0755 -t "$pkgdir/usr/bin/" "target/release/$_pkgname"
  install -Dm0644 -t "$pkgdir/usr/share/licenses/$_pkgname" LICENSE
}
