# Maintainer: Simon Hauser <Simon-Hauser@outlook.de>
# Contributor: Jean Lucas <jean@4ray.co>

pkgname=spotify-tui
pkgver=0.23.0
pkgrel=1
pkgdesc='Spotify client for the terminal written in Rust'
arch=(x86_64)
url=https://github.com/Rigellute/spotify-tui
license=(MIT)
depends=(openssl libxcb)
makedepends=(cargo python)
source=($pkgname-$pkgver.tar.gz::$url/archive/v$pkgver.tar.gz)
sha512sums=('0a1bc953fa8187accf6b78459b8900b513afd984e898f83742a700bee3942a921cbae6a1f9cd7883390ea322bac26e2c78b9a85b787b716a01c423b03d77b2b6')

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
