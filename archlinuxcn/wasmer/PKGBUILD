# Maintainer: Sven-Hendrik Haase <svenstaro@gmail.com>
# Maintainer: Julius Michaelis <gitter@liftm.de.de>

pkgname=wasmer
pkgver=1.0.2
pkgrel=3
pkgdesc="Universal Binaries Powered by WebAssembly"
arch=('x86_64')
url="https://github.com/wasmerio/wasmer"
license=(MIT)
depends=('gcc-libs')
makedepends=('rust' 'cmake' 'python' 'libxkbcommon' 'llvm')
source=("$pkgname-$pkgver.tar.gz::https://github.com/wasmerio/wasmer/archive/${pkgver}.tar.gz")
sha512sums=('f8058cbd5a8a807cd84b4a839c87ff76dae5475c655e804b27262cd5cb22ddb6c43da3a01b6cdbed29502afc38aa9ee589022f67fab27b189453f2500478c4a9')
options=('staticlibs')

build() {
  cd "$pkgname-$pkgver"
  cargo build --release --locked --manifest-path lib/c-api/Cargo.toml --no-default-features --features deprecated,wat,jit,native,object-file,cranelift,wasi
  cargo build --release --locked --manifest-path lib/cli/Cargo.toml --features "cranelift llvm singlepass" --bin wasmer
}

check() {
  cd "$pkgname-$pkgver"

  cargo test --release --locked --manifest-path lib/cli/Cargo.toml --features "cranelift llvm singlepass" --bin wasmer
  # Check if we can run a basic binary
  target/release/wasmer run tests/wasi-wast/wasi/snapshot1/hello.wasm &>/dev/null
}

package() {
  cd "$pkgname-$pkgver"

  install -Dm755 target/release/wasmer "$pkgdir"/usr/bin/wasmer
  for header in wasm.h wasmer_wasm.h wasmer.h wasmer.hh; do
    install -Dm644 "lib/c-api/"$header "$pkgdir"/usr/include/$header
  done

  install -Dm755 target/release/libwasmer_c_api.so "$pkgdir/usr/lib/libwasmer.so.$pkgver"
  install -Dm755 target/release/libwasmer_c_api.a "$pkgdir/usr/lib/libwasmer.a"
  local _shortver="${pkgver%.*}"
  local _majorver="${_shortver%.*}"
  ln -s "libwasmer.so.$pkgver" "$pkgdir/usr/lib/libwasmer.so.$_shortver"
  ln -s "libwasmer.so.$pkgver" "$pkgdir/usr/lib/libwasmer.so.$_majorver"
  ln -s "libwasmer.so.$pkgver" "$pkgdir/usr/lib/libwasmer.so"

  install -Dm644 LICENSE "$pkgdir"/usr/share/licenses/$pkgname/LICENSE

  env WASMER_DIR=/usr "$pkgdir"/usr/bin/wasmer config --pkg-config | install -Dm644 /dev/stdin "$pkgdir"/usr/lib/pkgconfig/wasmer.pc
}

# vim:set ts=2 sw=2 et:
