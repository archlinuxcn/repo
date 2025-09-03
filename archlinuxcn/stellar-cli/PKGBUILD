# Maintainer: Xeonacid <h.dwwwwww@gmail.com>

pkgname=stellar-cli
pkgver=23.1.1
pkgrel=1
pkgdesc='Command-line multi-tool for running and deploying Stellar contracts on the Stellar network'
url='https://stellar.org'
arch=(x86_64)
license=(Apache-2.0)
depends=(glibc gcc-libs systemd-libs openssl dbus)
makedepends=(git cargo clang)
source=(git+https://github.com/stellar/$pkgname#tag=v$pkgver)
sha512sums=('e001e8e255c050fbbf53efdb2ab00cddbc30c74e8ad3437cfd968d1ad64ca086124f1a360a9d3a8a8e794a3ff1ad3491f27a80a459032722eaa7f8f88962c0b4')
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
