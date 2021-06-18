# Maintainer: Sven-Hendrik Haase <svenstaro@gmail.com>
# Maintainer: Julius Michaelis <gitter@liftm.de.de>

pkgname=wasmer
pkgver=2.0.0
pkgrel=1
pkgdesc="Universal Binaries Powered by WebAssembly"
arch=('x86_64')
url="https://github.com/wasmerio/wasmer"
license=(MIT)
depends=('libffi' 'zlib' 'ncurses')
makedepends=('rust' 'cmake' 'python' 'libxkbcommon' 'llvm')
source=("$pkgname-$pkgver.tar.gz::https://github.com/wasmerio/wasmer/archive/${pkgver}.tar.gz")
sha512sums=('c02b97075212a496a4c30a9cfcd6b8ef89cb08bf3e5f9f20bf5f83c63bedb5744e4976ee3641310f6a44d911d670285c8b67c3cb9725acdd632ef5f8880ba4b9')
options=('staticlibs')

wasmer_env() {
  export ENABLE_LLVM=1
  export ENABLE_CRANELIFT=1
  export ENABLE_SINGLEPASS=1
  export WASMER_INSTALL_PREFIX=/usr
}

build() {
  cd "$pkgname-$pkgver"

  wasmer_env
  make all
}

check() {
  cd "$pkgname-$pkgver"

  wasmer_env
  make test-packages # test-compilers bugs... Needs investigation
  # Check if we can run a basic binary
  target/release/wasmer run tests/wasi-wast/wasi/snapshot1/hello.wasm &>/dev/null
}

package() {
  cd "$pkgname-$pkgver"

  wasmer_env
  DESTDIR="$pkgdir/usr/" make install
}

# vim:set ts=2 sw=2 et:
