# Maintainer: Wesley Moore <wes@wezm.net>

pkgname=bat
pkgver=0.2.2
pkgrel=1
pkgdesc='A cat(1) clone with syntax highlighting and Git integration'
arch=('x86_64')
url=https://github.com/sharkdp/bat
license=('MIT' 'APACHE')
makedepends=('rust' 'cmake')
depends=('curl' 'libssh2' 'oniguruma')
conflicts=('bacula-bat')
source=("$pkgname-$pkgver.tar.gz::$url/archive/v$pkgver.tar.gz")
sha512sums=('3a3e586f311fabfbc160999fc2bb2ab9e1ea0e5622b284325c4bc16e4c34cf7d0e51ae5cd3f5e6314dcaa2b983f541dfce7f0646d58a201a4bcf23a91af183c3')

build() {
  cd $pkgname-$pkgver
  cargo build --release
}

check() {
  cd $pkgname-$pkgver
  cargo test --release
}

package() {
  cd $pkgname-$pkgver
  install -Dm755 target/release/$pkgname "$pkgdir"/usr/bin/$pkgname
  #install -Dm644 doc/$pkgname.1 "$pkgdir"/usr/share/man/man1/$pkgname.1
  install -Dm644 LICENSE-APACHE "$pkgdir"/usr/share/licenses/$pkgname/LICENSE-APACHE
  install -Dm644 LICENSE-MIT "$pkgdir"/usr/share/licenses/$pkgname/LICENSE-MIT
}
