# Maintainer: Wesley Moore <wes@wezm.net>
pkgname=fnm
pkgver=1.35.0
pkgrel=1
pkgdesc="Fast and simple Node.js version manager, built with Rust"
arch=('x86_64')
url="https://github.com/Schniz/fnm"
license=('GPL3')
depends=('xz' 'bzip2' 'gcc-libs')
makedepends=('cargo')
conflicts=('fnm-bin')
source=("$pkgname-$pkgver.tar.gz::$url/archive/v$pkgver.tar.gz" "completions-panic.patch::$url/pull/1010/commits/a1f9f14a0ab7221b52ed2f563e50aa7b5a7e842e.patch")
sha256sums=('31b29e4534f17240ae576c9b726498bf551f1c14b3a0fb3ecc9f4aa95843d27a' '573e43881b65ff64a6b2fb569c10cc447c80a42da8e05ae7867e5b42c3d9db57')
options=('!lto')

prepare() {
  cd "$pkgname-$pkgver"
  patch --strip=1 --input=$srcdir/completions-panic.patch
}

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
