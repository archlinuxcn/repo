# Maintainer: Sven-Hendrik Haase <svenstaro@gmail.com>

pkgname=wasmer
pkgver=1.0.0
pkgrel=1
pkgdesc="Universal Binaries Powered by WebAssembly"
arch=('x86_64')
url="https://github.com/wasmerio/wasmer"
license=(MIT)
depends=('gcc-libs')
makedepends=('rust' 'cmake' 'python' 'libxkbcommon')
checkdepends=('llvm')
source=("$pkgname-$pkgver.tar.gz::https://github.com/wasmerio/wasmer/archive/${pkgver}.tar.gz")
sha512sums=('5869f5b1a111389a8442abb9edd03d38417df46188e88b65b90ac7dc3752bbc4f2d7a6031402d68f80f96ed9ec630345769ec0849a445845e55c2381945b44e5')

build() {
  cd "$pkgname-$pkgver"

  cargo build --all --release --locked
}

check() {
  cd "$pkgname-$pkgver"

  cargo test --release --locked
}

package() {
  cd "$pkgname-$pkgver"

  install -Dm755 target/release/wasmer "$pkgdir"/usr/bin/wasmer
  for header in wasm.h wasmer_wasm.h wasmer.h wasmer.hh; do
    install -Dm644 "lib/c-api/"$header "$pkgdir"/usr/include/$header
  done

  install -Dm755 target/release/libwasmer_c_api.so "$pkgdir/usr/lib/libwasmer.so.$pkgver"
  local _shortver="${pkgver%.*}"
  local _majorver="${_shortver%.*}"
  ln -s "libwasmer.so.$pkgver" "$pkgdir/usr/lib/libwasmer.so.$_shortver"
  ln -s "libwasmer.so.$pkgver" "$pkgdir/usr/lib/libwasmer.so.$_majorver"
  ln -s "libwasmer.so.$pkgver" "$pkgdir/usr/lib/libwasmer.so"

  install -Dm644 LICENSE "$pkgdir"/usr/share/licenses/$pkgname/LICENSE
}

# vim:set ts=2 sw=2 et:
