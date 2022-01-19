# Maintainer: George Rawlinson <grawlinson@archlinux.org>

pkgname=cargo-make
pkgver=0.35.8
pkgrel=1
pkgdesc="Rust task runner and build tool"
arch=('x86_64')
url="https://github.com/sagiegurari/cargo-make"
license=('Apache')
depends=('gcc-libs' 'openssl')
makedepends=('rust')
options=('!lto')
source=("$pkgname-$pkgver.tar.gz::$url/archive/$pkgver.tar.gz")
sha512sums=('ff0b3812e7b8031b73f27ef901b15704ac451b6b6eea7f04bd1ed30e909c25a8385de9015162faa3abe41d7e257852893919acf24f3b4be0a5657deb0965783d')
b2sums=('c6761ddea59fc31f138478a4d153578c4e692908316e11e11eb74e82c3ce6cc9e31cd5eede8960ef7a75167c6ad514d37d0c80b7e4aea314d2aca7d3435ff5e5')

prepare() {
  # download dependencies
  cd "$pkgname-$pkgver"
  cargo fetch --target "$CARCH-unknown-linux-gnu"
}

build() {
  cd "$pkgname-$pkgver"
  cargo build --release --frozen
}

package() {
  cd "$pkgname-$pkgver"

  # binary
  install -vDm755 -t "$pkgdir/usr/bin" target/release/{cargo-make,makers}

  # license
  install -vDm644 -t "$pkgdir/usr/share/licenses/$pkgname" LICENSE

  # documentation
  install -vDm644 -t "$pkgdir/usr/share/doc/$pkgname" *.md

  # shell auto-completion
  install -vDm644 extra/shell/makers-completion.bash "$pkgdir/usr/share/bash-completion/completions/makers"
}
