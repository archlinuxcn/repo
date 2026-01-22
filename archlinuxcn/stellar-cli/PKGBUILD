# Maintainer: Xeonacid <h.dwwwwww@gmail.com>

pkgname=stellar-cli
pkgver=25.0.0
pkgrel=1
pkgdesc='Command-line multi-tool for running and deploying Stellar contracts on the Stellar network'
url='https://stellar.org'
arch=(x86_64)
license=(Apache-2.0)
depends=(glibc gcc-libs systemd-libs openssl dbus)
makedepends=(git cargo clang)
source=(git+https://github.com/stellar/$pkgname#tag=v$pkgver)
sha512sums=('de68af2e659a8fcfa84ff88a6f31fbef24514d78c64b432476b53b16ddd05edfa7b64c9ee0ccdf857a4e686ace5171b704c7e16953c5cf92dd6db5a32e6374ed')
# https://github.com/briansmith/ring/issues/1444
options=(!lto)

prepare() {
  cd $pkgname
  export RUSTUP_TOOLCHAIN=stable
  cargo fetch --locked --target "$(rustc -vV | sed -n 's/host: //p')"
  mkdir completions
}

build() {
  cd $pkgname
  export RUSTUP_TOOLCHAIN=stable
  export CARGO_TARGET_DIR=target
  cargo build --frozen --release -p stellar-cli
  local _completion="target/release/stellar completion"
  $_completion --shell bash > "completions/stellar"
  $_completion --shell fish > "completions/stellar.fish"
  $_completion --shell zsh  > "completions/_stellar"
}

package() {
  cd $pkgname
  install -Dm755 "target/release/stellar" -t "$pkgdir/usr/bin/"
  install -Dm644 README.md FULL_HELP_DOCS.md -t "$pkgdir/usr/share/doc/$pkgname"
  install -Dm644 "completions/stellar" -t "$pkgdir/usr/share/bash-completion/completions/"
  install -Dm644 "completions/stellar.fish" -t "$pkgdir/usr/share/fish/vendor_completions.d/"
  install -Dm644 "completions/_stellar" -t "$pkgdir/usr/share/zsh/site-functions/"
}
