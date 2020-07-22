# Maintainer: Sven-Hendrik Haase <svenstaro@gmail.com>

pkgname=wasmer
pkgver=0.17.1
pkgrel=1
pkgdesc="Universal Binaries Powered by WebAssembly"
arch=('x86_64')
url="https://github.com/wasmerio/wasmer"
license=(MIT)
depends=('gcc-libs')
makedepends=('rust' 'cmake' 'python' 'git')
checkdepends=('llvm')
source=("git+https://github.com/wasmerio/wasmer.git#tag=${pkgver}")
sha512sums=('SKIP')

build() {
  cd "$srcdir/$pkgname"

  git submodule update --init --recursive
  cargo build --release --locked
}

check() {
  cd "$srcdir/$pkgname"

  cargo test --release --locked
}

package() {
  cd "$srcdir/$pkgname"

  install -Dm755 target/release/wasmer "$pkgdir"/usr/bin/wasmer
  install -Dm644 LICENSE "$pkgdir"/usr/share/licenses/$pkgname/LICENSE
}

# vim:set ts=2 sw=2 et:
