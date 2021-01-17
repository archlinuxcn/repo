# Maintainer: Sven-Hendrik Haase <svenstaro@gmail.com>

pkgname=wasmer
pkgver=1.0.1
pkgrel=1
pkgdesc="Universal Binaries Powered by WebAssembly"
arch=('x86_64')
url="https://github.com/wasmerio/wasmer"
license=(MIT)
depends=('gcc-libs')
makedepends=('rust' 'cmake' 'python' 'libxkbcommon')
checkdepends=('llvm')
source=("$pkgname-$pkgver.tar.gz::https://github.com/wasmerio/wasmer/archive/${pkgver}.tar.gz")
sha512sums=('5b96f84d6f1a00ef02bb1e2398706d1095276682d15d2c87a9a72571363c9ec3a1728beeb4d533adaa0ac9023cb54efc0fdd819982a4624c63b0e52010b8619e')

build() {
  cd "$pkgname-$pkgver"

  cargo build --all --release --locked --features "cranelift llvm singlepass"
}

check() {
  cd "$pkgname-$pkgver"

  cargo test --release --locked --manifest-path lib/cli/Cargo.toml --features "cranelift llvm singlepass" --bin wasmer
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
