# Maintainer: Mark Wagie <mark dot wagie at proton dot me>
# Co-Maintainer: Thomas Schoenauer <t.schoenauer@hgs-wt.at>
# Contributor: Roey Darwish Dror <roey.ghost@gmail.com>
pkgname=topgrade
pkgver=16.4.2
pkgrel=1
pkgdesc="Upgrade all the things"
arch=('x86_64' 'aarch64')
url="https://topgrade-rs.github.io"
license=('GPL-3.0-or-later')
depends=('gcc-libs')
makedepends=('cargo')
source=("$pkgname-$pkgver.tar.gz::https://github.com/topgrade-rs/topgrade/archive/refs/tags/v$pkgver.tar.gz")
sha256sums=('e5a5727b0b33463c913992e05607aecd3157f469c283673f8eca992e9b9c535c')

prepare() {
  cd "$pkgname-$pkgver"
  export RUSTUP_TOOLCHAIN=stable
  cargo fetch --locked --target "$(rustc -vV | sed -n 's/host: //p')"
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
