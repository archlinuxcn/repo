# Maintainer: Wesley Moore <wes@wezm.net>
pkgname=fnm
pkgver=1.34.0
pkgrel=1
pkgdesc="Fast and simple Node.js version manager, built with Rust"
arch=('x86_64')
url="https://github.com/Schniz/fnm"
license=('GPL3')
depends=('xz' 'bzip2' 'gcc-libs')
makedepends=('cargo')
conflicts=('fnm-bin')
source=("$pkgname-$pkgver.tar.gz::$url/archive/v$pkgver.tar.gz")
sha256sums=('6ee954538e0af38b53004ea8834e8fec6b36d22711b67132888d1cbdbb06a09d')
options=('!lto')

build() {
  cd "$pkgname-$pkgver"
  CARGO_TARGET_DIR=target cargo build --release --locked
}

package() {
  install -Dm755 "$srcdir/$pkgname-$pkgver/target/release/$pkgname" "$pkgdir/usr/bin/$pkgname"

  mkdir -p \
    "$pkgdir"/usr/share/bash-completion/completions \
    "$pkgdir"/usr/share/fish/vendor_completions.d \
    "$pkgdir"/usr/share/zsh/site-functions
  "$pkgdir/usr/bin/$pkgname" completions --shell bash > "$pkgdir"/usr/share/bash-completion/completions/$pkgname
  "$pkgdir/usr/bin/$pkgname" completions --shell fish > "$pkgdir"/usr/share/fish/vendor_completions.d/$pkgname.fish
  "$pkgdir/usr/bin/$pkgname" completions --shell zsh > "$pkgdir"/usr/share/zsh/site-functions/_$pkgname
}
