# Maintainer: orhun <orhunparmaksiz@gmail.com>
# Contributor: Simon Hauser <Simon-Hauser@outlook.de>
# Contributor: Jean Lucas <jean@4ray.co>
# Contributor: XenHat <aur@xenh.at>

# https://github.com/orhun/pkgbuilds

pkgname=spotify-tui
pkgver=0.25.0
pkgrel=3
pkgdesc="Spotify client for the terminal written in Rust"
arch=('x86_64')
url="https://github.com/Rigellute/spotify-tui"
license=('MIT')
depends=('gcc-libs' 'openssl' 'libxcb')
makedepends=('cargo' 'python')
source=("$pkgname-$pkgver.tar.gz::$url/archive/v$pkgver.tar.gz"
	"rspotify-0.10.0.tar.gz::https://crates.io/api/v1/crates/rspotify/0.10.0/download"
	"Cargo.toml.patch"
	"Cargo.lock.patch"
	"0001-Add-Collection-SearchType.patch")
sha512sums=('92a2ab53059b7d58e502a732f16a8eb725e19ea2e13c4f63dd64e3f0d62a3999f6b6b338c396db734f6ee9d63459da15e69b392f945c8f967d794447ac5ff8a4'
            '48db0018e65b516c34f8f31828178b361e701099850e043708f02754d4251e010f95aea6b49b5104263cb52ee815e9a25f6f371be202446975b3191c3f570daa'
            '42e31bc3931f36c621000b17b5599ed42da0211e6543cb30c98a3140fdd02e1c607d04f09bde259c9039bfde5cc783f4cb92d3e60d302f37f7dfddeec8f46cbf'
            'ec91345bacda9848246926fa7d0cabdebcaf4e88a1e2b1f3cb78cdb471e4e0f7ca22d3640f837a34fac2cedc6da2e133e33a8992923a47d74fba0801a84111ca'
            '89a1efdc38e14c7a32268fb8ac8c2235d9ae6d888d516a55bbc34933e881fe35d107d8feffe7a572b203e8ac2a553c7c4f4862af4dd3b7ea1391d4fb9ff1dca0')

prepare() {
  cd "$srcdir/rspotify-0.10.0"
  patch -p1 -i "$srcdir/0001-Add-Collection-SearchType.patch"

  cd "$srcdir/$pkgname-$pkgver"
  for patch in 'Cargo.toml.patch' 'Cargo.lock.patch'; do
    patch -p0 -i "$srcdir/$patch"
  done
  cargo update
  cargo fetch --locked --target "$CARCH-unknown-linux-gnu"
}

build() {
  cd "$pkgname-$pkgver"
  export RUSTUP_TOOLCHAIN=stable
  export CARGO_TARGET_DIR=target
  cargo build --release
  ./target/release/spt --completions bash > target/release/spt-completion.bash
  ./target/release/spt --completions zsh > target/release/spt-completion.zsh
  ./target/release/spt --completions fish > target/release/spt-completion.fish
}

check() {
  cd "$pkgname-$pkgver"
  export RUSTUP_TOOLCHAIN=stable
  cargo test
}

package() {
  cd "$pkgname-$pkgver"
  install -Dm 755 "target/release/spt" -t "$pkgdir/usr/bin"
  install -Dm 644 README.md -t "$pkgdir/usr/share/doc/$pkgname"
  install -Dm 644 LICENSE -t "$pkgdir/usr/share/licenses/$pkgname"
  install -Dm 644 target/release/spt-completion.bash "$pkgdir/usr/share/bash-completion/completions/spt"
  install -Dm 644 target/release/spt-completion.zsh "$pkgdir/usr/share/zsh/site-functions/_spt"
  install -Dm 644 target/release/spt-completion.fish "$pkgdir/usr/share/fish/vendor_completions.d/spt.fish"
}
