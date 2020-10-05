# Maintainer: Simon Hauser <Simon-Hauser@outlook.de>
# Contributor: Jean Lucas <jean@4ray.co>

pkgname=spotify-tui
pkgver=0.22.0
pkgrel=1
pkgdesc='Spotify client for the terminal written in Rust'
arch=(x86_64)
url=https://github.com/Rigellute/spotify-tui
license=(MIT)
depends=(openssl libxcb)
makedepends=(cargo python)
source=($pkgname-$pkgver.tar.gz::$url/archive/v$pkgver.tar.gz)
sha512sums=('9d641d7a01945fbaec40778167a4abcc7777c64283e9e42144e46e1d2e34a824a96ad51cda28681216ce6320fb32b75e9b49879f8414f25b0ea8dddb3319d73c')

build() {
  cd $pkgname-$pkgver
  cargo build --release --target-dir "target/"
}

package() {
  cd $pkgname-$pkgver
  install -D target/release/spt -t "$pkgdir"/usr/bin
  install -Dm 644 README.md -t "$pkgdir"/usr/share/doc/$pkgname
  install -Dm 644 LICENSE -t "$pkgdir"/usr/share/licenses/$pkgname
}
