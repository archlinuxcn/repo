# Maintainer: Mark Wagie <mark dot wagie at proton dot me>
# Co-Maintainer: Thomas Schoenauer <t.schoenauer@hgs-wt.at>
# Contributor: Roey Darwish Dror <roey.ghost@gmail.com>
pkgname=topgrade
pkgver=16.9.0
pkgrel=2
pkgdesc="Upgrade all the things"
arch=('x86_64' 'aarch64')
url="https://topgrade-rs.github.io"
license=('GPL-3.0-or-later')
depends=('libgcc')
makedepends=('cargo')
source=("$pkgname-$pkgver.tar.gz::https://github.com/topgrade-rs/topgrade/archive/refs/tags/v$pkgver.tar.gz")
sha256sums=('d6e8376c6363545ce8994703c33f18d50fb4f8c689a2bc196bed159010c9cf03')

prepare() {
  cd "$pkgname-$pkgver"
  export RUSTUP_TOOLCHAIN=stable
  cargo fetch --locked --target "$(rustc --print host-tuple)"
}

build() {
  cd "$pkgname-$pkgver"
  export RUSTUP_TOOLCHAIN=stable
  export CARGO_TARGET_DIR=target
  cargo build --frozen --release

  # Generate completions
  for shell in bash fish zsh; do
    ./"target/release/$pkgname" --gen-completion "${shell}" > "$pkgname.${shell}"
  done

  # Generate man page
  ./"target/release/$pkgname" --gen-manpage > "$pkgname.1"
}

check() {
  cd "$pkgname-$pkgver"
  export RUSTUP_TOOLCHAIN=stable
  cargo test --frozen
}

package() {
  cd "$pkgname-$pkgver"
  install -Dm755 "target/release/$pkgname" -t "$pkgdir/usr/bin/"
  install -Dm644 "$pkgname.1" -t "$pkgdir/usr/share/man/man1/"
  install -Dm644 "$pkgname.bash" "$pkgdir/usr/share/bash-completion/completions/$pkgname"
  install -Dm644 "$pkgname.fish" -t "$pkgdir/usr/share/fish/vendor_completions.d/"
  install -Dm644 "$pkgname.zsh" "$pkgdir/usr/share/zsh/site-functions/_$pkgname"
  install -Dm644 config.example.toml -t "$pkgdir/usr/share/doc/$pkgname/"
}
