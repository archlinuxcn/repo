# Maintainer:
# Contributor: Adam Harvey <adam@adamharvey.name>

: ${RUSTUP_TOOLCHAIN:=stable}
: ${CARGO_TARGET_DIR:=target}
export CARGO_TARGET_DIR RUSTUP_TOOLCHAIN

_pkgname="tuc"
pkgname="$_pkgname"
pkgver=1.2.0
pkgrel=1
pkgdesc="A more powerful alternative to cut"
url="https://github.com/riquito/tuc"
license=('GPL-3.0-or-later')
arch=("x86_64" "aarch64")

depends=(
  'gcc-libs'
  'glibc'
)
makedepends=(
  'cargo'
)

_pkgsrc="$_pkgname-$pkgver"
_pkgext="tar.gz"
source=("$_pkgsrc.$_pkgext"::"$url/archive/refs/tags/v$pkgver.$_pkgext")
sha256sums=('bb6d16772ed0728f396d32066d391206420497a4f902071b0229790a8c844307')

prepare() {
  cd "$_pkgsrc"
  cargo fetch --locked --target "$CARCH-unknown-linux-gnu"
}

build() {
  cd "$_pkgsrc"
  cargo build --frozen --release --all-features
}

check() {
  cd "$_pkgsrc"
  cargo test --frozen --all-features
}

package() {
  cd "$_pkgsrc"
  install -Dm755 "target/release/$_pkgname" -t "$pkgdir/usr/bin/"
  install -Dm644 "doc/tuc.1" -t "$pkgdir/usr/share/man/man1/"
}
