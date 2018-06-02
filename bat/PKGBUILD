# Maintainer: Wesley Moore <wes@wezm.net>

pkgname=bat
pkgver=0.4.1
pkgrel=1
pkgdesc='A cat(1) clone with syntax highlighting and Git integration'
arch=('x86_64')
url=https://github.com/sharkdp/bat
license=('MIT' 'APACHE')
makedepends=('rust' 'cmake')
depends=('curl' 'libssh2' 'oniguruma')
conflicts=('bacula-bat')
source=("$pkgname-$pkgver.tar.gz::$url/archive/v$pkgver.tar.gz")
sha256sums=('3ae66854da59d691b8740672708a2e7f2f240c76e8a00283f59a6e39127e4583')

build() {
  cd $pkgname-$pkgver
  cargo build --release
}

# Check disabled for now. See:
# https://github.com/sharkdp/bat/issues/161
# check() {
#   cd $pkgname-$pkgver
#   cargo test --release
# }

package() {
  cd $pkgname-$pkgver
  install -Dm755 target/release/$pkgname "$pkgdir"/usr/bin/$pkgname
  #install -Dm644 doc/$pkgname.1 "$pkgdir"/usr/share/man/man1/$pkgname.1
  install -Dm644 LICENSE-APACHE "$pkgdir"/usr/share/licenses/$pkgname/LICENSE-APACHE
  install -Dm644 LICENSE-MIT "$pkgdir"/usr/share/licenses/$pkgname/LICENSE-MIT
}
